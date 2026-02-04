import argparse
import csv
import json
import sqlite3
import subprocess
from pathlib import Path


TABLES = [
    "authority_reference",
    "evidence_item",
    "money_flow",
    "field_validation",
]


def get_repo_root() -> Path:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            text=True,
        ).strip()
        return Path(out)
    except Exception:
        return Path(__file__).resolve().parents[2]


def list_columns(conn: sqlite3.Connection, table: str) -> list[str]:
    cur = conn.cursor()
    return [r[1] for r in cur.execute(f"PRAGMA table_info({table})").fetchall()]


def export_table_json(conn: sqlite3.Connection, table: str, out_path: Path, limit: int | None) -> int:
    cols = [c for c in list_columns(conn, table) if c != "_raw_json"]
    cur = conn.cursor()
    sql = f"SELECT {', '.join(cols)} FROM {table}" + (" LIMIT ?" if limit else "")
    rows = cur.execute(sql, (limit,) if limit else ()).fetchall()

    items = [dict(zip(cols, r)) for r in rows]
    out_path.write_text(json.dumps(items, indent=2), encoding="utf-8")
    return len(items)


def export_table_csv(conn: sqlite3.Connection, table: str, out_path: Path, limit: int | None) -> int:
    cols = [c for c in list_columns(conn, table) if c != "_raw_json"]
    cur = conn.cursor()
    sql = f"SELECT {', '.join(cols)} FROM {table}" + (" LIMIT ?" if limit else "")
    rows = cur.execute(sql, (limit,) if limit else ()).fetchall()

    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        w.writerows(rows)
    return len(rows)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Export clearlane.db tables to JSON/CSV for a static dashboard (no Ollama)."
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Output directory (default: interface/reports/dashboard_data)",
    )
    parser.add_argument(
        "--format",
        choices=["json", "csv", "both"],
        default="both",
        help="Export format",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional row limit per table (default: no limit)",
    )
    args = parser.parse_args(argv)

    repo_root = get_repo_root()
    db_path = repo_root / "interface" / "db" / "clearlane.db"
    out_dir = (
        Path(args.out)
        if args.out is not None
        else (repo_root / "interface" / "reports" / "dashboard_data")
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    if not db_path.exists():
        print("DB missing. Run: python interface/db/build_db.py --rebuild")
        return 2

    conn = sqlite3.connect(f"file:{db_path.as_posix()}?mode=ro", uri=True)
    try:
        index = {
            "db": str(db_path),
            "tables": {},
        }
        for table in TABLES:
            cols = [c for c in list_columns(conn, table) if c != "_raw_json"]
            table_info = {
                "columns": cols,
                "json": None,
                "csv": None,
                "rows": None,
            }

            row_count = int(conn.execute(f"SELECT COUNT(1) FROM {table}").fetchone()[0])
            table_info["rows"] = row_count

            if args.format in {"json", "both"}:
                json_path = out_dir / f"{table}.json"
                exported = export_table_json(conn, table, json_path, args.limit)
                table_info["json"] = json_path.name
                table_info["exported_rows"] = exported

            if args.format in {"csv", "both"}:
                csv_path = out_dir / f"{table}.csv"
                exported = export_table_csv(conn, table, csv_path, args.limit)
                table_info["csv"] = csv_path.name
                table_info["exported_rows"] = exported

            index["tables"][table] = table_info

        (out_dir / "index.json").write_text(json.dumps(index, indent=2), encoding="utf-8")
        print(f"Wrote: {out_dir}")
        print("Wrote: index.json")
        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
