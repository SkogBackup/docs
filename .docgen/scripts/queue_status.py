#!/usr/bin/env python3
"""
Check status of the frontmatter generation queue.
Shows pending, processing, completed, and failed jobs.
"""

import sqlite3
import argparse
from datetime import datetime
from pathlib import Path


def format_timestamp(ts_str):
    """Format timestamp for display"""
    if not ts_str:
        return 'N/A'
    try:
        ts = datetime.fromisoformat(ts_str)
        return ts.strftime('%Y-%m-%d %H:%M:%S')
    except:
        return ts_str


def show_summary(db_path):
    """Show summary statistics"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get counts by status
    cursor.execute("""
        SELECT status, COUNT(*)
        FROM processing_queue
        GROUP BY status
    """)

    stats = dict(cursor.fetchall())
    total = sum(stats.values())

    print("=== Queue Summary ===")
    print(f"Total jobs: {total}")
    print(f"  Pending:    {stats.get('pending', 0)}")
    print(f"  Processing: {stats.get('processing', 0)}")
    print(f"  Completed:  {stats.get('completed', 0)}")
    print(f"  Failed:     {stats.get('failed', 0)}")

    # Calculate progress
    if total > 0:
        completed = stats.get('completed', 0)
        progress = (completed / total) * 100
        print(f"\nProgress: {progress:.1f}% ({completed}/{total})")

    conn.close()


def show_pending(db_path, limit=10):
    """Show pending jobs"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, file_path, priority, created_at
        FROM processing_queue
        WHERE status = 'pending'
        ORDER BY priority DESC, created_at ASC
        LIMIT ?
    """, (limit,))

    jobs = cursor.fetchall()

    if not jobs:
        print("\n✓ No pending jobs")
        conn.close()
        return

    print(f"\n=== Pending Jobs (showing up to {limit}) ===")
    for job_id, file_path, priority, created_at in jobs:
        priority_str = f"[P{priority}]" if priority != 0 else ""
        print(f"  [{job_id}] {priority_str} {file_path}")
        print(f"        Queued: {format_timestamp(created_at)}")

    # Show total pending
    cursor.execute("SELECT COUNT(*) FROM processing_queue WHERE status = 'pending'")
    total_pending = cursor.fetchone()[0]

    if total_pending > limit:
        print(f"\n  ... and {total_pending - limit} more")

    conn.close()


def show_processing(db_path):
    """Show currently processing jobs"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, file_path, started_at
        FROM processing_queue
        WHERE status = 'processing'
        ORDER BY started_at ASC
    """)

    jobs = cursor.fetchall()

    if not jobs:
        conn.close()
        return

    print(f"\n=== Currently Processing ===")
    for job_id, file_path, started_at in jobs:
        print(f"  [{job_id}] {file_path}")
        print(f"        Started: {format_timestamp(started_at)}")

    conn.close()


def show_failed(db_path, limit=10):
    """Show failed jobs"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, file_path, retries, max_retries, error_message, completed_at
        FROM processing_queue
        WHERE status = 'failed'
        ORDER BY completed_at DESC
        LIMIT ?
    """, (limit,))

    jobs = cursor.fetchall()

    if not jobs:
        conn.close()
        return

    print(f"\n=== Failed Jobs (showing up to {limit}) ===")
    for job_id, file_path, retries, max_retries, error_msg, failed_at in jobs:
        print(f"  [{job_id}] {file_path}")
        print(f"        Failed: {format_timestamp(failed_at)} (after {retries} retries)")
        if error_msg:
            print(f"        Error: {error_msg[:100]}")

    conn.close()


def show_completed(db_path, limit=10):
    """Show recently completed jobs"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, file_path, completed_at
        FROM processing_queue
        WHERE status = 'completed'
        ORDER BY completed_at DESC
        LIMIT ?
    """, (limit,))

    jobs = cursor.fetchall()

    if not jobs:
        conn.close()
        return

    print(f"\n=== Recently Completed (showing {limit}) ===")
    for job_id, file_path, completed_at in jobs:
        print(f"  [{job_id}] {file_path}")
        print(f"        Completed: {format_timestamp(completed_at)}")

    conn.close()


def reset_stuck_jobs(db_path):
    """Reset jobs stuck in 'processing' status back to 'pending'"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE processing_queue
        SET status = 'pending', started_at = NULL
        WHERE status = 'processing'
    """)

    count = cursor.rowcount
    conn.commit()
    conn.close()

    if count > 0:
        print(f"\n✓ Reset {count} stuck job(s) from 'processing' to 'pending'")
    else:
        print("\n✓ No stuck jobs found")


def clear_completed(db_path):
    """Remove completed jobs from queue"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM processing_queue WHERE status = 'completed'")

    count = cursor.rowcount
    conn.commit()
    conn.close()

    if count > 0:
        print(f"\n✓ Cleared {count} completed job(s) from queue")
    else:
        print("\n✓ No completed jobs to clear")


def main():
    parser = argparse.ArgumentParser(description='Check frontmatter generation queue status')
    parser.add_argument('--db', default='.docgen/docs.db', help='Database path')
    parser.add_argument('--pending', action='store_true', help='Show pending jobs')
    parser.add_argument('--processing', action='store_true', help='Show processing jobs')
    parser.add_argument('--failed', action='store_true', help='Show failed jobs')
    parser.add_argument('--completed', action='store_true', help='Show completed jobs')
    parser.add_argument('--all', action='store_true', help='Show all job types')
    parser.add_argument('--limit', type=int, default=10, help='Limit results per category')
    parser.add_argument('--reset-stuck', action='store_true', help='Reset stuck jobs from processing to pending')
    parser.add_argument('--clear-completed', action='store_true', help='Remove completed jobs from queue')

    args = parser.parse_args()

    # Check if database exists
    if not Path(args.db).exists():
        print(f"Error: Database not found at {args.db}")
        print("Initialize the queue by enqueueing some files first.")
        return

    # Show summary
    show_summary(args.db)

    # Show details based on flags
    if args.all or args.pending:
        show_pending(args.db, args.limit)

    if args.all or args.processing:
        show_processing(args.db)

    if args.all or args.failed:
        show_failed(args.db, args.limit)

    if args.all or args.completed:
        show_completed(args.db, args.limit)

    # Operations
    if args.reset_stuck:
        reset_stuck_jobs(args.db)

    if args.clear_completed:
        clear_completed(args.db)

    # If no flags, show basic info
    if not any([args.pending, args.processing, args.failed, args.completed, args.all, args.reset_stuck, args.clear_completed]):
        print("\nUse --all to see detailed status, or --help for more options")


if __name__ == '__main__':
    main()
