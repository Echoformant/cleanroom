import argparse
import json
import sqlite3
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Tuple

SCHEMAS = {
    "authority_reference": {
        "file": "authority_reference.schema.json",
        "primary_key": "authority_id",
    },
    "evidence_item": {
        "file": "evidence_item.schema.json",
        "primary_key": "evidence_id",
    },
    "money_flow": {
        "file": "money_flow.schema.json",
        "primary_key": "flow_id",
    },
    "field_validation": {
        "file": "field_validation.schema.json",
        "primary_key": "fv_id",
    },
}

TYPE_MAP = {
    "string": "TEXT",
    "number": "REAL",
    "integer": "INTEGER",
    "boolean": "INTEGER",
    "array": "TEXT",
    "object": "TEXT",
}


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


def ensure_required_paths(root: Path) -> Tuple[Path, Path]:
    schemas_dir = root / "schemas"
    artifacts_dir = root / "artifacts" / "validated"
    if not schemas_dir.exists():
        print(f"Missing schemas directory: {schemas_dir}")
        sys.exit(1)
    if not artifacts_dir.exists():
        print(f"Missing artifacts/validated directory: {artifacts_dir}")
        sys.exit(1)
    return schemas_dir, artifacts_dir


def load_schema_properties(schema_path: Path, schema_key: str) -> Dict[str, Dict]:
    with schema_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    props = None
    defs = data.get("$defs", {})
    if schema_key in defs and isinstance(defs[schema_key], dict):
        props = defs[schema_key].get("properties")
    if props is None and "properties" in data:
        props = data.get("properties")
    if props is None:
        print(f"No properties found in schema {schema_path}")
        sys.exit(1)
    return props


def map_type(json_type) -> str:
    if isinstance(json_type, list):
        # prefer first recognized type
        for t in json_type:
            if t in TYPE_MAP:
                return TYPE_MAP[t]
        return "TEXT"
    return TYPE_MAP.get(json_type, "TEXT")


def build_schema_sql(schema_properties: Dict[str, Dict[str, Dict]]) -> str:
    statements: List[str] = []
    for table in ["authority_reference", "evidence_item", "money_flow", "field_validation"]:
        props = schema_properties[table]
        pk_col = SCHEMAS[table]["primary_key"]
        if pk_col not in props:
            print(f"Missing primary key column {pk_col} in schema {SCHEMAS[table]['file']}")
            sys.exit(1)
        # Column order: schema order if available, else sorted
        if props:
            col_names = list(props.keys())
        else:
            col_names = []
        columns_sql = []
        for col in col_names:
            col_type = map_type(props[col].get("type")) if isinstance(props[col], dict) else "TEXT"
            columns_sql.append(f"  {col} {col_type}")
        columns_sql.append("  _raw_json TEXT")
        columns_sql.append(f"  PRIMARY KEY ({pk_col})")
        stmt = [f"DROP TABLE IF EXISTS {table};", f"CREATE TABLE {table} (\n" + ",\n".join(columns_sql) + "\n);"]
        # Index rules
        if "editor_status" in props:
            stmt.append(f"CREATE INDEX idx_{table}_editor_status ON {table}(editor_status);")
        if table == "money_flow" and "event_date" in props:
            stmt.append("CREATE INDEX idx_money_flow_event_date ON money_flow(event_date);")
        if table == "evidence_item" and "issue_date" in props:
            stmt.append("CREATE INDEX idx_evidence_item_issue_date ON evidence_item(issue_date);")
        statements.extend(stmt)
    return "\n".join(statements) + "\n"


def ingest_table(conn: sqlite3.Connection, table: str, props: Dict[str, Dict], artifacts_dir: Path) -> int:
    target_dir = artifacts_dir / table
    if not target_dir.exists():
        return 0
    # Ingest recursively under artifacts/validated/<table>/ but ignore hidden/tooling dirs.
    files = []
    for p in target_dir.rglob("*.json"):
        if not p.is_file():
            continue
        parts = set(p.parts)
        if ".git" in parts or ".github" in parts or "_manifests" in parts:
            continue
        # If a parent directory looks like an original YAML artifact folder, skip JSON fragments under it.
        if any(part.lower().endswith((".yaml", ".yml")) for part in p.parts):
            continue
        # Skip any hidden path components.
        if any(part.startswith(".") for part in p.parts):
            continue
        files.append(p)
    files = sorted(files)
    if not files:
        return 0
    col_names = list(props.keys()) if props else []
    col_names = col_names if col_names else []
    cols_with_raw = col_names + ["_raw_json"]
    placeholders = ",".join(["?"] * len(cols_with_raw))
    # Deterministic dedupe: for duplicate primary keys, keep the first inserted row (files are processed in sorted order).
    sql = f"INSERT OR IGNORE INTO {table} (" + ",".join(cols_with_raw) + f") VALUES ({placeholders})"
    count = 0
    collisions = 0
    cur = conn.cursor()
    cur.execute("BEGIN")
    for path in files:
        with path.open("r", encoding="utf-8") as f:
            obj = json.load(f)
        if isinstance(obj, list):
            print(f"Artifact {path} is an array; aborting ingestion.")
            sys.exit(1)
        if not isinstance(obj, dict):
            print(f"Artifact {path} is not a JSON object; aborting ingestion.")
            sys.exit(1)
        row = []
        for col in col_names:
            val = obj.get(col)
            if isinstance(val, (dict, list)):
                row.append(json.dumps(val, ensure_ascii=False))
            elif isinstance(val, bool):
                row.append(int(val))
            else:
                row.append(val)
        row.append(json.dumps(obj, ensure_ascii=False))
        cur.execute(sql, row)
        # If a row was ignored, it's a PK collision (or other constraint); count it.
        if cur.rowcount == 1:
            count += 1
        else:
            collisions += 1
    conn.commit()
    if collisions:
        print(f"{table} collisions_ignored: {collisions}")
    return count


def main(argv=None):
    parser = argparse.ArgumentParser(description="Build SQLite DB from validated artifacts")
    parser.add_argument("--rebuild", action="store_true", help="Rebuild database if it exists")
    args = parser.parse_args(argv)

    repo_root = get_repo_root()
    schemas_dir, artifacts_dir = ensure_required_paths(repo_root)
    db_path = repo_root / "interface" / "db" / "clearlane.db"
    schema_sql_path = repo_root / "interface" / "db" / "schema.sql"

    if db_path.exists() and not args.rebuild:
        print("DB exists. Run with --rebuild to recreate.")
        sys.exit(1)
    if args.rebuild and db_path.exists():
        db_path.unlink()
    if schema_sql_path.exists():
        schema_sql_path.unlink()

    schema_properties: Dict[str, Dict] = {}
    for table, info in SCHEMAS.items():
        schema_path = schemas_dir / info["file"]
        if not schema_path.exists():
            print(f"Missing schema file: {schema_path}")
            sys.exit(1)
        props = load_schema_properties(schema_path, table)
        schema_properties[table] = props

    schema_sql = build_schema_sql(schema_properties)
    schema_sql_path.parent.mkdir(parents=True, exist_ok=True)
    schema_sql_path.write_text(schema_sql, encoding="utf-8")

    conn = sqlite3.connect(db_path)
    try:
        conn.executescript(schema_sql)
        totals = {}
        for table, props in schema_properties.items():
            totals[table] = ingest_table(conn, table, props, artifacts_dir)
    finally:
        conn.close()

    for table in ["authority_reference", "evidence_item", "money_flow", "field_validation"]:
        print(f"{table}: {totals.get(table, 0)}")


if __name__ == "__main__":
    main()
