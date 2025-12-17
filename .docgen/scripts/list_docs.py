#!/usr/bin/env python3
"""List all documents in the database"""

import sqlite3
import argparse

def list_documents(db_path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT d.id, d.path, d.title, d.prompt_template, d.type
        FROM documents d
        ORDER BY d.path
    """)

    print(f"\n{'ID':<5} {'Path':<50} {'Template':<20} {'Title'}")
    print("-" * 100)

    for row in cursor.fetchall():
        print(f"{row['id']:<5} {row['path']:<50} {row['prompt_template']:<20} {row['title']}")

    # Count
    cursor.execute("SELECT COUNT(*) FROM documents")
    count = cursor.fetchone()[0]
    print(f"\nTotal: {count} documents\n")

    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='List documents in database')
    parser.add_argument('--db', default='.docgen/docs.db', help='Path to database')
    args = parser.parse_args()

    list_documents(args.db)
