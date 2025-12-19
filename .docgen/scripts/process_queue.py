#!/usr/bin/env python3
"""
Process the frontmatter generation queue.
Pulls pending jobs, calls Ollama, updates files with frontmatter.
"""

import os
import re
import sqlite3
import subprocess
import argparse
import time
from pathlib import Path
from datetime import datetime


class QueueProcessor:
    def __init__(self, db_path, ollama_model='llama3.2', delay=2, dry_run=False):
        self.db_path = db_path
        self.ollama_model = ollama_model
        self.delay = delay  # Delay between jobs (seconds)
        self.dry_run = dry_run
        self.stats = {
            'processed': 0,
            'completed': 0,
            'failed': 0,
            'skipped': 0
        }

    def get_next_job(self):
        """Get next pending job from queue (ordered by priority)"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, file_path, prompt, retries, max_retries
            FROM processing_queue
            WHERE status = 'pending'
            ORDER BY priority DESC, created_at ASC
            LIMIT 1
        """)

        job = cursor.fetchone()
        conn.close()

        if job:
            return {
                'id': job[0],
                'file_path': job[1],
                'prompt': job[2],
                'retries': job[3],
                'max_retries': job[4]
            }
        return None

    def mark_processing(self, job_id):
        """Mark job as currently processing"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE processing_queue
            SET status = 'processing', started_at = ?
            WHERE id = ?
        """, (datetime.utcnow().isoformat(), job_id))

        conn.commit()
        conn.close()

    def mark_completed(self, job_id):
        """Mark job as successfully completed"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE processing_queue
            SET status = 'completed', completed_at = ?, error_message = NULL
            WHERE id = ?
        """, (datetime.utcnow().isoformat(), job_id))

        conn.commit()
        conn.close()

    def mark_failed(self, job_id, error_message, should_retry=True):
        """Mark job as failed, optionally retry"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Get current retry count
        cursor.execute("SELECT retries, max_retries FROM processing_queue WHERE id = ?", (job_id,))
        retries, max_retries = cursor.fetchone()

        if should_retry and retries < max_retries:
            # Increment retry counter and reset to pending
            cursor.execute("""
                UPDATE processing_queue
                SET status = 'pending', retries = retries + 1, error_message = ?
                WHERE id = ?
            """, (error_message, job_id))
            print(f"  ⟳ Retry {retries + 1}/{max_retries} scheduled")
        else:
            # Mark as permanently failed
            cursor.execute("""
                UPDATE processing_queue
                SET status = 'failed', completed_at = ?, error_message = ?
                WHERE id = ?
            """, (datetime.utcnow().isoformat(), error_message, job_id))
            print(f"  ✗ Permanently failed after {retries} retries")

        conn.commit()
        conn.close()

    def call_ollama(self, prompt):
        """Call Ollama with the prompt"""
        try:
            result = subprocess.run(
                ['ollama', 'run', self.ollama_model, prompt],
                capture_output=True,
                text=True,
                timeout=300,  # 5 minute timeout
                check=True
            )
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            raise Exception(f"Ollama timeout after 300 seconds")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Ollama error: {e.stderr}")
        except FileNotFoundError:
            raise Exception("Ollama not found - is it installed?")

    def extract_frontmatter_from_response(self, response):
        """Extract YAML frontmatter block from Ollama response"""
        # Look for content between --- markers
        pattern = r'---\s*\n(.*?)\n---'
        match = re.search(pattern, response, re.DOTALL)

        if match:
            return f"---\n{match.group(1)}\n---"

        # If no markers, check if entire response looks like YAML
        if response.strip().startswith('categories:') or response.strip().startswith('tags:'):
            return f"---\n{response.strip()}\n---"

        raise ValueError("Could not find valid frontmatter in response")

    def has_frontmatter(self, content):
        """Check if content already has frontmatter"""
        return content.strip().startswith('---')

    def add_frontmatter_to_file(self, file_path, frontmatter):
        """Add or replace frontmatter in file"""
        # Read existing content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove existing frontmatter if present
        if self.has_frontmatter(content):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                body = '---'.join(parts[2:]).lstrip()
            else:
                body = content
        else:
            body = content.lstrip()

        # Combine new frontmatter with body
        new_content = f"{frontmatter}\n\n{body}"

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

    def process_job(self, job):
        """Process a single job"""
        job_id = job['id']
        file_path = job['file_path']

        print(f"\n[{job_id}] {file_path}")

        # Check if file exists
        if not Path(file_path).exists():
            self.mark_failed(job_id, f"File not found: {file_path}", should_retry=False)
            self.stats['failed'] += 1
            return False

        try:
            # Mark as processing
            self.mark_processing(job_id)

            if self.dry_run:
                print(f"  [DRY RUN] Would call Ollama with prompt")
                print(f"  Prompt preview: {job['prompt'][:100]}...")
                self.mark_completed(job_id)
                self.stats['completed'] += 1
                return True

            # Call Ollama
            print(f"  → Calling Ollama ({self.ollama_model})...")
            response = self.call_ollama(job['prompt'])

            # Extract frontmatter from response
            print(f"  → Parsing response...")
            frontmatter = self.extract_frontmatter_from_response(response)

            # Update file
            print(f"  → Updating file...")
            self.add_frontmatter_to_file(file_path, frontmatter)

            # Mark as completed
            self.mark_completed(job_id)
            self.stats['completed'] += 1

            print(f"  ✓ Completed successfully")
            return True

        except Exception as e:
            print(f"  ✗ Error: {e}")
            self.mark_failed(job_id, str(e))
            self.stats['failed'] += 1
            return False

    def get_queue_stats(self):
        """Get current queue statistics"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT status, COUNT(*)
            FROM processing_queue
            GROUP BY status
        """)

        stats = dict(cursor.fetchall())
        conn.close()

        return {
            'pending': stats.get('pending', 0),
            'processing': stats.get('processing', 0),
            'completed': stats.get('completed', 0),
            'failed': stats.get('failed', 0)
        }

    def run(self, max_jobs=None):
        """Process queue until empty or max_jobs reached"""
        print(f"=== Queue Processor Starting ===")
        print(f"Model: {self.ollama_model}")
        print(f"Delay: {self.delay}s between jobs")
        print(f"Dry run: {self.dry_run}")
        print()

        # Show initial queue stats
        stats = self.get_queue_stats()
        print(f"Queue status:")
        print(f"  Pending: {stats['pending']}")
        print(f"  Processing: {stats['processing']}")
        print(f"  Completed: {stats['completed']}")
        print(f"  Failed: {stats['failed']}")

        if stats['pending'] == 0:
            print("\n✓ Queue is empty!")
            return

        print(f"\nStarting processing...\n")

        jobs_processed = 0
        while True:
            # Get next job
            job = self.get_next_job()

            if not job:
                print("\n✓ Queue exhausted!")
                break

            # Process job
            self.process_job(job)
            jobs_processed += 1
            self.stats['processed'] += 1

            # Check if max_jobs reached
            if max_jobs and jobs_processed >= max_jobs:
                print(f"\n⚠ Max jobs ({max_jobs}) reached")
                break

            # Delay before next job
            if self.delay > 0:
                time.sleep(self.delay)

        # Final stats
        print(f"\n=== Processing Complete ===")
        print(f"Processed: {self.stats['processed']}")
        print(f"Completed: {self.stats['completed']}")
        print(f"Failed: {self.stats['failed']}")

        # Show remaining queue
        stats = self.get_queue_stats()
        if stats['pending'] > 0:
            print(f"\nRemaining in queue: {stats['pending']}")


def main():
    parser = argparse.ArgumentParser(description='Process frontmatter generation queue')
    parser.add_argument('--db', default='.docgen/docs.db', help='Database path')
    parser.add_argument('--model', default='llama3.2', help='Ollama model to use')
    parser.add_argument('--delay', type=float, default=2, help='Delay between jobs (seconds)')
    parser.add_argument('--max-jobs', type=int, help='Max number of jobs to process')
    parser.add_argument('--dry-run', action='store_true', help='Simulate processing without calling Ollama')

    args = parser.parse_args()

    processor = QueueProcessor(args.db, args.model, args.delay, args.dry_run)
    processor.run(args.max_jobs)


if __name__ == '__main__':
    main()
