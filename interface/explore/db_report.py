import argparse
import sqlite3
import subprocess
from pathlib import Path


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


def safe_distinct_count(conn: sqlite3.Connection, table: str, col: str, limit: int = 5000) -> int:
    # Keep it cheap: sample up to N rows.
    cur = conn.cursor()
    return int(
        cur.execute(
            f"SELECT COUNT(DISTINCT {col}) FROM (SELECT {col} FROM {table} LIMIT ?)",
            (int(limit),),
        ).fetchone()[0]
    )


def safe_null_count(conn: sqlite3.Connection, table: str, col: str, limit: int = 5000) -> int:
    cur = conn.cursor()
    return int(
        cur.execute(
            f"SELECT SUM(CASE WHEN {col} IS NULL THEN 1 ELSE 0 END) FROM (SELECT {col} FROM {table} LIMIT ?)",
            (int(limit),),
        ).fetchone()[0]
        or 0
    )


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Generate a local HTML report of clearlane.db")
    parser.add_argument(
        "--out",
        default=None,
        help="Output HTML path (default: interface/reports/db_report.html)",
    )
    parser.add_argument(
        "--include-plotlyjs",
        choices=["cdn", "inline"],
        default="inline",
        help="Plotly JS inclusion mode; inline works offline but is large",
    )
    args = parser.parse_args(argv)

    # Import plotly only when needed so core tools don't require it.
    try:
        import plotly.graph_objects as go
        import plotly.io as pio
    except ModuleNotFoundError:
        print("Missing dependency: plotly")
        print("Install: pip install -r interface/requirements.explore.txt")
        return 2

    sample_limit = 5000

    repo_root = get_repo_root()
    db_path = repo_root / "interface" / "db" / "clearlane.db"
    out_path = (
        Path(args.out)
        if args.out is not None
        else (repo_root / "interface" / "reports" / "db_report.html")
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if not db_path.exists():
        print("DB missing. Run: python interface/db/build_db.py --rebuild")
        return 2

    conn = sqlite3.connect(f"file:{db_path.as_posix()}?mode=ro", uri=True)
    try:
        tables = list_tables(conn)
        if not tables:
            print("No tables found.")
            return 0

        # Summary chart: rows per table
        table_counts = [(t, table_row_count(conn, t)) for t in tables]
        table_counts.sort(key=lambda x: x[1], reverse=True)
        tables_sorted = [t for t, _ in table_counts]
        counts_sorted = [c for _, c in table_counts]

        fig_counts = go.Figure(
            data=[
                go.Bar(
                    x=tables_sorted,
                    y=counts_sorted,
                    text=counts_sorted,
                    textposition="outside",
                    hovertemplate="table=%{x}<br>rows=%{y}<extra></extra>",
                    marker_color="#2F6FED",
                )
            ],
            layout=go.Layout(
                title="Rows per table",
                xaxis_title="Table",
                yaxis_title="Row count",
                margin=dict(l=40, r=20, t=60, b=120),
            ),
        )
        fig_counts.update_layout(template="plotly_white")

        # Column quality heatmap-ish (null rate over sample) using a bar per column per table in sections.
        sections = []
        sections.append("<h1>Cleanroom DB Report</h1>")
        sections.append(f"<p>DB: {db_path}</p>")
        sections.append(
            f"<p>Note: per-column NULL and DISTINCT charts are computed over the first {sample_limit} rows "
            f"(or fewer, if the table has fewer rows).</p>"
        )
        sections.append(pio.to_html(fig_counts, include_plotlyjs=args.include_plotlyjs, full_html=False))

        # Add a quick summary table (so it's not just bars).
        summary_rows = []
        for t in tables_sorted:
            cols = [c for c in table_columns(conn, t) if c != "_raw_json"]
            summary_rows.append((t, table_row_count(conn, t), len(cols)))

        fig_table = go.Figure(
            data=[
                go.Table(
                    header=dict(
                        values=["table", "rows", "columns (excl _raw_json)"],
                        fill_color="#111827",
                        font=dict(color="white", size=12),
                        align="left",
                    ),
                    cells=dict(
                        values=[
                            [r[0] for r in summary_rows],
                            [r[1] for r in summary_rows],
                            [r[2] for r in summary_rows],
                        ],
                        fill_color="#F3F4F6",
                        align="left",
                        height=24,
                    ),
                )
            ]
        )
        fig_table.update_layout(margin=dict(l=0, r=0, t=0, b=0), template="plotly_white")
        sections.append("<h2>Tables overview</h2>")
        sections.append(pio.to_html(fig_table, include_plotlyjs=False, full_html=False))

        for t in tables_sorted:
            cols = [c for c in table_columns(conn, t) if c != "_raw_json"]
            if not cols:
                continue

            row_count = table_row_count(conn, t)
            sample_n = min(row_count, sample_limit)

            nulls = [safe_null_count(conn, t, c, limit=sample_limit) for c in cols]
            distinct = [safe_distinct_count(conn, t, c, limit=sample_limit) for c in cols]

            # Keep charts readable: show top columns only.
            max_cols = 25
            null_pairs = sorted(zip(cols, nulls), key=lambda x: x[1], reverse=True)[:max_cols]
            distinct_pairs = sorted(zip(cols, distinct), key=lambda x: x[1], reverse=True)[:max_cols]
            null_cols, null_vals = zip(*null_pairs) if null_pairs else ([], [])
            distinct_cols, distinct_vals = zip(*distinct_pairs) if distinct_pairs else ([], [])

            null_pct = [
                (v / sample_n * 100.0) if sample_n else 0.0
                for v in null_vals
            ]

            fig_nulls = go.Figure(
                data=[
                    go.Bar(
                        x=list(null_cols),
                        y=list(null_vals),
                        text=[f"{p:.1f}%" for p in null_pct],
                        textposition="outside",
                        hovertemplate=(
                            "table=" + t + "<br>"
                            "column=%{x}<br>"
                            "nulls=%{y}<br>"
                            f"sample_rows={sample_n}<br>"
                            "null_pct=%{text}<extra></extra>"
                        ),
                        marker_color="#EF4444",
                    )
                ],
                layout=go.Layout(
                    title=f"{t}: NULL count (sampled)",
                    xaxis_title="Column",
                    yaxis_title="NULLs in sample",
                    xaxis_tickangle=-35,
                    margin=dict(l=40, r=20, t=60, b=160),
                ),
            )
            fig_distinct = go.Figure(
                data=[
                    go.Bar(
                        x=list(distinct_cols),
                        y=list(distinct_vals),
                        text=list(distinct_vals),
                        textposition="outside",
                        hovertemplate=(
                            "table=" + t + "<br>"
                            "column=%{x}<br>"
                            "distinct=%{y}<br>"
                            f"sample_rows={sample_n}<extra></extra>"
                        ),
                        marker_color="#10B981",
                    )
                ],
                layout=go.Layout(
                    title=f"{t}: DISTINCT count (sampled)",
                    xaxis_title="Column",
                    yaxis_title="Distinct values in sample",
                    xaxis_tickangle=-35,
                    margin=dict(l=40, r=20, t=60, b=160),
                ),
            )

            sections.append(f"<h2>{t}</h2>")
            sections.append(pio.to_html(fig_nulls, include_plotlyjs=False, full_html=False))
            sections.append(pio.to_html(fig_distinct, include_plotlyjs=False, full_html=False))

        html = "\n".join(
            [
                "<!doctype html>",
                "<html>",
                "<head><meta charset='utf-8'><title>Cleanroom DB Report</title></head>",
                "<body>",
                *sections,
                "</body>",
                "</html>",
            ]
        )
        out_path.write_text(html, encoding="utf-8")
        print(f"Wrote: {out_path}")
        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
