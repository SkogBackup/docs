#!/usr/bin/env python3
"""
SkogAI Documentation Generator
Reads from database, generates docs via Ollama, adds frontmatter, saves to folders
"""

import sqlite3
import json
import subprocess
import os
from datetime import datetime
from pathlib import Path
import argparse

class DocGenerator:
    def __init__(self, db_path, output_dir, ollama_model="llama3.2"):
        self.db_path = db_path
        self.output_dir = Path(output_dir)
        self.ollama_model = ollama_model
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def get_documents(self, doc_id=None):
        """Fetch documents from database"""
        cursor = self.conn.cursor()
        if doc_id:
            cursor.execute("SELECT * FROM documents WHERE id = ?", (doc_id,))
            return [cursor.fetchone()]
        else:
            cursor.execute("SELECT * FROM documents ORDER BY path")
            return cursor.fetchall()

    def get_tags_for_doc(self, doc_id):
        """Get all tags for a document"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT t.name FROM tags t
            JOIN document_tags dt ON t.id = dt.tag_id
            WHERE dt.document_id = ?
        """, (doc_id,))
        return [row[0] for row in cursor.fetchall()]

    def get_categories_for_doc(self, doc_id):
        """Get all categories for a document"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT c.name FROM categories c
            JOIN document_categories dc ON c.id = dc.category_id
            WHERE dc.document_id = ?
        """, (doc_id,))
        return [row[0] for row in cursor.fetchall()]

    def load_prompt_template(self, template_name):
        """Load a prompt template from .docgen/prompts/"""
        template_path = Path(__file__).parent.parent / "prompts" / f"{template_name}.txt"
        with open(template_path, 'r') as f:
            return f.read()

    def call_ollama(self, prompt):
        """Call Ollama API to generate content"""
        try:
            result = subprocess.run(
                ['ollama', 'run', self.ollama_model, prompt],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Error calling Ollama: {e}")
            return None

    def generate_frontmatter(self, doc, tags, categories):
        """Generate YAML frontmatter for document"""
        timestamp = datetime.now().isoformat()

        frontmatter = "---\n"
        if categories:
            frontmatter += "categories:\n"
            for cat in categories:
                frontmatter += f"- {cat}\n"
        else:
            frontmatter += "categories: []\n"

        if tags:
            frontmatter += "tags:\n"
            for tag in tags:
                frontmatter += f"- {tag}\n"
        else:
            frontmatter += "tags: []\n"

        frontmatter += f"permalink: {doc['path']}\n"
        frontmatter += f"title: {doc['title']}\n"
        frontmatter += f"type: {doc['type']}\n"
        frontmatter += f"generated_at: {timestamp}\n"
        frontmatter += "---\n\n"

        return frontmatter

    def generate_document(self, doc):
        """Generate a single document"""
        print(f"Generating: {doc['path']}")

        # Get metadata
        tags = self.get_tags_for_doc(doc['id'])
        categories = self.get_categories_for_doc(doc['id'])

        # Load prompt template
        prompt_template = self.load_prompt_template(doc['prompt_template'])

        # Fill in template with doc content/context
        prompt = prompt_template.replace("{input_context}", doc['content'] or "")
        prompt = prompt.replace("{title}", doc['title'])
        prompt = prompt.replace("{agent_name}", doc['title'])

        # Generate content via Ollama
        generated_content = self.call_ollama(prompt)

        if not generated_content:
            print(f"  ✗ Failed to generate content for {doc['path']}")
            return False

        # Add frontmatter
        frontmatter = self.generate_frontmatter(doc, tags, categories)
        full_content = frontmatter + generated_content

        # Write to file
        output_path = self.output_dir / doc['path']
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w') as f:
            f.write(full_content)

        print(f"  ✓ Generated: {output_path}")
        return True

    def generate_all(self, doc_id=None):
        """Generate all documents or a specific one"""
        docs = self.get_documents(doc_id)

        total = len(docs)
        success = 0

        for doc in docs:
            if self.generate_document(doc):
                success += 1

        print(f"\nGenerated {success}/{total} documents")

    def close(self):
        self.conn.close()


def main():
    parser = argparse.ArgumentParser(description='Generate SkogAI documentation')
    parser.add_argument('--db', default='.docgen/docs.db', help='Path to SQLite database')
    parser.add_argument('--output', default='generated', help='Output directory')
    parser.add_argument('--model', default='llama3.2', help='Ollama model to use')
    parser.add_argument('--doc-id', type=int, help='Generate specific document by ID')

    args = parser.parse_args()

    gen = DocGenerator(args.db, args.output, args.model)
    try:
        gen.generate_all(args.doc_id)
    finally:
        gen.close()


if __name__ == "__main__":
    main()
