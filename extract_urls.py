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
    args = parser.parse_args()

    print("Search phrase: https://bangs.tristanhavelick.com/")

    try:
        conn = sqlite3.connect(args.db_path)
        cursor = conn.cursor()
        sql = "SELECT datetime(last_visit_date/1000000, 'unixepoch') AS visit_date, url FROM moz_places WHERE url LIKE 'https://bangs.tristanhavelick.com/%' ORDER BY last_visit_date DESC;"
        cursor.execute(sql)
        for visit_date, url in cursor.fetchall():
            print(f"{visit_date}\t{url}")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
