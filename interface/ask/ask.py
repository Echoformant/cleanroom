import os
import sqlite3
import subprocess
import sys
from pathlib import Path

from tabulate import tabulate


DISALLOWED_TOKENS = [
    "insert",
    "update",
    "delete",
    "drop",
    "alter",
    "attach",
    "detach",
    "pragma",
    "vacuum",
    "create",
]


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


def load_prompt(prompt_path: Path) -> str:
    return prompt_path.read_text(encoding="utf-8")


def build_schema_context(conn: sqlite3.Connection) -> str:
    cur = conn.cursor()
    tables = [row[0] for row in cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
    ).fetchall()]
    lines = []
    for table in tables:
        cols = [r[1] for r in cur.execute(f"PRAGMA table_info({table})").fetchall()]
        lines.append(f"{table}: " + ", ".join(cols))
    return "\n".join(lines)


def select_model() -> str:
    return os.environ.get("OLLAMA_MODEL", "phi3")


def run_ollama(model: str, prompt: str) -> str:
    ollama_bin = os.environ.get("OLLAMA_BIN", "ollama")
    result = subprocess.run(
        [ollama_bin, "run", model, prompt],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode != 0:
        sys.stderr.write(f"ollama run failed (exit {result.returncode}): {result.stderr}\n")
        sys.exit(5)
    sql = result.stdout.strip()
    if not sql:
        sys.stderr.write("ollama returned empty output.\n")
        sys.exit(5)
    return sql


def enforce_sql_safety(sql: str) -> str:
    trimmed = sql.strip()
    lowered = trimmed.lower()
    if not trimmed.lower().startswith("select"):
        print("Rejected SQL by safety gate.")
        print(trimmed)
        sys.exit(3)
    if ";" in trimmed:
        print("Rejected SQL by safety gate.")
        print(trimmed)
        sys.exit(3)
    for token in DISALLOWED_TOKENS:
        if token in lowered:
            print("Rejected SQL by safety gate.")
            print(trimmed)
            sys.exit(3)
    return trimmed


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    if not args:
        print("Usage: python interface/ask/ask.py \"your question\"")
        sys.exit(1)
    question = " ".join(args)

    repo_root = get_repo_root()
    db_path = repo_root / "interface" / "db" / "clearlane.db"
    prompt_path = repo_root / "interface" / "ask" / "schema_prompt.txt"

    if not db_path.exists():
        print("DB missing. Run: python interface/db/build_db.py --rebuild")
        sys.exit(2)

    base_prompt = load_prompt(prompt_path)

    conn = sqlite3.connect(f"file:{db_path.as_posix()}?mode=ro", uri=True)
    try:
        schema_context = build_schema_context(conn)
    finally:
        conn.close()

    prompt = base_prompt.strip() + "\n\nTABLES_AND_COLUMNS:\n" + schema_context + "\n\nQUESTION:\n" + question

    model = select_model()
    sql = run_ollama(model, prompt)
    safe_sql = enforce_sql_safety(sql)

    conn = sqlite3.connect(f"file:{db_path.as_posix()}?mode=ro", uri=True)
    try:
        cur = conn.execute(safe_sql)
        rows = cur.fetchall()
        headers = [desc[0] for desc in cur.description]
    except sqlite3.Error as e:
        conn.close()
        sys.stderr.write(f"SQLite error: {e}\n")
        sys.exit(4)
    finally:
        conn.close()

    print("SQL:")
    print(safe_sql)
    print(f"ROWS: {len(rows)}")
    if rows:
        print(tabulate(rows, headers=headers, tablefmt="github"))

    sys.exit(0)


if __name__ == "__main__":
    main()
