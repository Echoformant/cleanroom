import argparse
import sqlite3
import subprocess
import sys
from pathlib import Path

from tabulate import tabulate


def get_repo_root() -> Path:
    try:
        out = subprocess.check_output([
            "git",
            "rev-parse",
            "--show-toplevel",
        ], text=True).strip()
        return Path(out)
    except Exception:
        return Path(__file__).resolve().parents[2]


def list_tables(conn: sqlite3.Connection) -> list[str]:
    cur = conn.cursor()
    return [
        r[0]
        for r in cur.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type='table' AND name NOT LIKE 'sqlite_%' "
            "ORDER BY name"
        ).fetchall()
    ]


def table_columns(conn: sqlite3.Connection, table: str) -> list[str]:
    cur = conn.cursor()
    return [r[1] for r in cur.execute(f"PRAGMA table_info({table})").fetchall()]


def table_row_count(conn: sqlite3.Connection, table: str) -> int:
    cur = conn.cursor()
    return int(cur.execute(f"SELECT COUNT(1) FROM {table}").fetchone()[0])


def sample_rows(conn: sqlite3.Connection, table: str, limit: int) -> tuple[list[str], list[tuple]]:
    cols = table_columns(conn, table)

    # Keep samples readable: prefer pk + editor_status + amount/fiscal_year/date-ish columns if present.
    preferred = []
    for c in cols:
        if c.endswith("_id"):
            preferred.append(c)
    for c in ["editor_status", "fiscal_year", "issue_date", "event_date", "amount", "fund_type"]:
        if c in cols and c not in preferred:
            preferred.append(c)

    # Fill remaining up to 8 columns.
    for c in cols:
        if c == "_raw_json":
            continue
        if c not in preferred:
            preferred.append(c)
        if len(preferred) >= 8:
            break

    if not preferred:
        preferred = [c for c in cols if c != "_raw_json"][:8]

    cur = conn.cursor()
    rows = cur.execute(
        f"SELECT {', '.join(preferred)} FROM {table} LIMIT {int(limit)}"
    ).fetchall()
    return preferred, rows


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Inspect interface/db/clearlane.db without Ollama")
    parser.add_argument("--samples", type=int, default=5, help="Sample rows per table")
    args = parser.parse_args(argv)

    repo_root = get_repo_root()
    db_path = repo_root / "interface" / "db" / "clearlane.db"
    if not db_path.exists():
        print("DB missing. Run: python interface/db/build_db.py --rebuild")
        return 2

    conn = sqlite3.connect(f"file:{db_path.as_posix()}?mode=ro", uri=True)
    try:
        tables = list_tables(conn)
        if not tables:
            print("No tables found.")
            return 0

        print("TABLES")
        summary_rows = []
        for t in tables:
            summary_rows.append((t, table_row_count(conn, t), ", ".join(table_columns(conn, t))))
        print(tabulate(summary_rows, headers=["table", "rows", "columns"], tablefmt="github"))

        for t in tables:
            print("\nSAMPLE:", t)
            cols, rows = sample_rows(conn, t, args.samples)
            if not rows:
                print("(no rows)")
                continue
            print(tabulate(rows, headers=cols, tablefmt="github"))

        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
