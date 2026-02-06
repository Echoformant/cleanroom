# Server — FastAPI Backend for Clearlane Dashboard

**Status:** ACTIVE  
**Created:** 2026-02-05  
**Purpose:** Provides REST API endpoints to run Python analysis scripts from the web dashboard

---

## Overview

This module provides an HTTP API layer that enables the interactive dashboard to execute Python scripts and retrieve results. It bridges the browser-based visualization tools with the command-line analysis scripts.

---

## Files

| File | Description |
|------|-------------|
| `api.py` | FastAPI application with all endpoints |

---

## Endpoints

### Health & Data

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Serves the main dashboard (`_data/index.html`) |
| `/api/health` | GET | Returns server status |
| `/api/summary` | GET | Returns quick stats (artifact counts, dollar totals) |
| `/api/graph` | GET | Returns the full linkage graph JSON |
| `/api/artifacts/{category}` | GET | Returns artifacts for a specific category |

### Script Runners

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/run/linkage-analyzer` | POST | Runs `linkage_analyzer.py --export-all` |
| `/api/run/gap-analyzer` | POST | Runs `gap_analyzer.py` |
| `/api/run/quick-summary` | POST | Runs `quick_summary.py` |

---

## Running the Server

```powershell
# From the validated/ directory
python -m uvicorn server.api:app --host 0.0.0.0 --port 8000 --reload
```

The `--reload` flag enables auto-restart when code changes.

---

## Configuration

- **Port:** 8000 (default)
- **CORS:** Enabled for all origins (development mode)
- **Encoding:** UTF-8 forced for Windows subprocess compatibility

---

## Dependencies

```
fastapi
uvicorn
```

Install via:
```powershell
pip install fastapi uvicorn
```

---

## Architecture

```
Browser (index.html)
    ↓ POST /api/run/*
FastAPI (api.py)
    ↓ subprocess.run()
Python Scripts (scripts/*.py)
    ↓ stdout/stderr
FastAPI
    ↓ JSON response
Browser
```

---

## Related

- [_data/index.html](_data/index.html) — Interactive dashboard UI
- [scripts/README.md](scripts/README.md) — Analysis script documentation
