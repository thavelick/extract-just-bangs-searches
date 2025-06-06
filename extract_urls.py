#!/usr/bin/env python3
"""Extract URLs from a Firefox places.sqlite database using a LIKE query."""

import argparse
import sqlite3
import sys

def main():
    parser = argparse.ArgumentParser(
        description="Extract URLs from a Firefox places.sqlite database using a LIKE query."
    )
    parser.add_argument(
        "db_path", help="Path to the Firefox places.sqlite database file."
    )
    parser.add_argument(
        "query", help="Search query for the URL (will be used in a LIKE clause)."
    )
    args = parser.parse_args()

    print(f"Search phrase: {args.query}")

    try:
        conn = sqlite3.connect(args.db_path)
        cursor = conn.cursor()
        sql = "SELECT url FROM moz_places WHERE url LIKE ? ORDER BY last_visit_date DESC;"
        pattern = f"%{args.query}%"
        cursor.execute(sql, (pattern,))
        for row in cursor.fetchall():
            print(row[0])
    except sqlite3.Error as e:
        print(f"SQLite error: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
