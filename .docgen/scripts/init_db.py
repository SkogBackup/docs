#!/usr/bin/env python3
"""
Initialize the documentation database
"""

import sqlite3
import argparse
from pathlib import Path

def init_database(db_path, schema_path):
    """Initialize database with schema"""
    conn = sqlite3.connect(db_path)

    # Read and execute schema
    with open(schema_path, 'r') as f:
        schema = f.read()

    conn.executescript(schema)
    conn.commit()

    print(f"✓ Database initialized: {db_path}")
    return conn

def add_document(conn, path, title, doc_type, content, prompt_template, categories=None, tags=None):
    """Add a document to the database"""
    cursor = conn.cursor()

    # Insert document
    cursor.execute("""
        INSERT INTO documents (path, title, type, content, prompt_template)
        VALUES (?, ?, ?, ?, ?)
    """, (path, title, doc_type, content, prompt_template))

    doc_id = cursor.lastrowid

    # Add categories
    if categories:
        for cat_name in categories:
            cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES (?)", (cat_name,))
            cursor.execute("SELECT id FROM categories WHERE name = ?", (cat_name,))
            cat_id = cursor.fetchone()[0]
            cursor.execute("INSERT INTO document_categories (document_id, category_id) VALUES (?, ?)",
                         (doc_id, cat_id))

    # Add tags
    if tags:
        for tag_name in tags:
            cursor.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", (tag_name,))
            cursor.execute("SELECT id FROM tags WHERE name = ?", (tag_name,))
            tag_id = cursor.fetchone()[0]
            cursor.execute("INSERT INTO document_tags (document_id, tag_id) VALUES (?, ?)",
                         (doc_id, tag_id))

    conn.commit()
    print(f"  ✓ Added: {path}")
    return doc_id

def load_sample_data(conn):
    """Load sample documents based on existing structure"""
    print("\nAdding sample documents...")

    # Claude profile
    add_document(
        conn,
        path="agents/claude/profile.md",
        title="Claude Profile",
        doc_type="note",
        content="Claude is an AI agent in the SkogAI ecosystem. Role: Archaeologist, Lore Keeper, Orchestrator.",
        prompt_template="agent-profile",
        categories=["agents", "claude"],
        tags=["agent", "claude", "profile"]
    )

    # Sample memory block
    add_document(
        conn,
        path="agents/claude/memory-blocks/sample-memory.md",
        title="Sample Memory Block",
        doc_type="note",
        content="A memory block capturing a significant event in SkogAI history.",
        prompt_template="memory-block",
        categories=["agents", "claude", "memory"],
        tags=["memory", "history", "claude"]
    )

    # Sample technical doc
    add_document(
        conn,
        path="docs/technical/sample-tech-doc.md",
        title="Sample Technical Documentation",
        doc_type="note",
        content="Technical documentation for a SkogAI system component.",
        prompt_template="notation-doc",
        categories=["technical"],
        tags=["documentation", "technical"]
    )

    print("✓ Sample data loaded\n")

def main():
    parser = argparse.ArgumentParser(description='Initialize documentation database')
    parser.add_argument('--db', default='.docgen/docs.db', help='Path to SQLite database')
    parser.add_argument('--schema', default='.docgen/schema.sql', help='Path to schema file')
    parser.add_argument('--sample-data', action='store_true', help='Load sample data')

    args = parser.parse_args()

    # Ensure directory exists
    Path(args.db).parent.mkdir(parents=True, exist_ok=True)

    conn = init_database(args.db, args.schema)

    if args.sample_data:
        load_sample_data(conn)

    conn.close()

if __name__ == "__main__":
    main()
