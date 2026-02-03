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
