# Cleanroom Local Ask Interface

## Prerequisites
- Python 3.10+ with stdlib `sqlite3`
- Local Ollama CLI with a downloaded model named `phi3` or `llama3` (or set `OLLAMA_MODEL`)

## A) Create venv (optional but recommended)
```
python -m venv .venv
source .venv/bin/activate   (mac/linux)
.venv\Scripts\activate    (windows powershell)
```

## B) Install deps
```
pip install -r interface/requirements.txt
```

## C) Build DB
```
python interface/db/build_db.py --rebuild
```

## D) Ask a question
```
python interface/ask/ask.py "list 5 money_flow rows"
```

## Optional: Diagnostics (artifacts vs ingested)
```
python interface/db/diagnostics.py
```

## Optional: Inspect DB (no Ollama)
Shows tables, columns, and sample rows.
```
python interface/db/inspect_db.py
```

## Optional: Plotly HTML report (no Ollama)
1) Install Plotly:
```
pip install -r interface/requirements.explore.txt
```
2) Generate report:
```
python interface/explore/db_report.py
```
This writes: interface/reports/db_report.html

## Optional: Export dashboard data (no Ollama)
Exports the four tables to JSON/CSV for use in a static dashboard.
```
python interface/explore/export_dashboard_data.py
```
This writes: interface/reports/dashboard_data/

## Optional: Vega-Lite dashboard (static HTML)
1) Export dashboard data (JSON):
```
python interface/explore/export_dashboard_data.py --format json
```
2) Serve reports and open the dashboard:
```
cd interface/reports
python -m http.server 8000
```
Then open: http://localhost:8000/dashboard/index.html
If the charts are blank and you see an error about Vega libraries not loading, your network may be blocking the CDN scripts.
You can vendor the JS files by running:
```
python interface/reports/dashboard/fetch_vendor.py
```

## Optional: Custom Ollama binary
Set `OLLAMA_BIN` if `ollama` is not on PATH.

## E) Expected example output (must be literal example)
```
SQL:
SELECT flow_id FROM money_flow LIMIT 5
ROWS: 5
<tabulated output>
```

## Manual verification steps
1) Verify DB file exists:
   - interface/db/clearlane.db exists on disk
2) Verify tables exist:
   - authority_reference, evidence_item, money_flow, field_validation
3) Verify read-only mode:
   - ask.py uses uri=True with mode=ro
4) Verify safety gate:
   - Running: python interface/ask/ask.py "drop table money_flow" must reject SQL and exit code 3
5) Verify ingestion source restriction:
   - build_db.py references only artifacts/validated/
   - build_db.py does not reference proposals/, invalidated/, processed/, reports/
