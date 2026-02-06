#!/usr/bin/env python3
"""
NAMI Clearlane Dashboard API
FastAPI backend for running analysis scripts and serving results.
"""

import json
import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = BASE_DIR / "scripts"
DATA_DIR = BASE_DIR / "_data"

app = FastAPI(
    title="NAMI Clearlane API",
    description="Arkansas Public Finance Validated Artifacts Dashboard",
    version="1.0.0"
)

# Allow CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def run_script(script_name: str, args: list = None) -> dict:
    """Run a Python script and capture output."""
    script_path = SCRIPTS_DIR / script_name
    if not script_path.exists():
        raise HTTPException(status_code=404, detail=f"Script not found: {script_name}")
    
    cmd = [sys.executable, str(script_path)]
    if args:
        cmd.extend(args)
    
    # Set environment for UTF-8 output
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    
    try:
        result = subprocess.run(
            cmd,
            cwd=str(BASE_DIR),
            capture_output=True,
            text=True,
            timeout=120,
            encoding='utf-8',
            errors='replace',
            env=env
        )
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "return_code": result.returncode,
            "timestamp": datetime.now().isoformat()
        }
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=504, detail="Script timed out after 120 seconds")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# =============================================================================
# API Endpoints
# =============================================================================

@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok", "timestamp": datetime.now().isoformat()}


@app.get("/api/summary")
async def get_summary():
    """Get artifact summary statistics."""
    graph_path = DATA_DIR / "artifacts_graph.json"
    if not graph_path.exists():
        raise HTTPException(status_code=404, detail="Graph data not found. Run linkage analyzer first.")
    
    with open(graph_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    nodes = data["nodes"]
    mf = [n for n in nodes if n["category"] == "money_flow"]
    auth = [n for n in nodes if n["category"] == "authority_reference"]
    evid = [n for n in nodes if n["category"] == "evidence_item"]
    fv = [n for n in nodes if n["category"] == "field_validation"]
    
    total_amount = sum(
        n.get("data", {}).get("amount", 0) 
        for n in mf 
        if n.get("data", {}).get("amount")
    )
    
    return {
        "total_artifacts": len(nodes),
        "money_flows": len(mf),
        "authority_references": len(auth),
        "evidence_items": len(evid),
        "field_validations": len(fv),
        "total_linkages": len(data["edges"]),
        "tracked_amount": total_amount,
        "orphan_count": data["metadata"]["orphan_count"],
        "generated_at": data["metadata"]["generated_at"]
    }


@app.get("/api/graph")
async def get_graph():
    """Get the full artifact graph data."""
    graph_path = DATA_DIR / "artifacts_graph.json"
    if not graph_path.exists():
        raise HTTPException(status_code=404, detail="Graph data not found. Run linkage analyzer first.")
    
    with open(graph_path, "r", encoding="utf-8") as f:
        return json.load(f)


@app.get("/api/artifacts/{category}")
async def get_artifacts_by_category(category: str):
    """Get all artifacts in a category."""
    valid_categories = ["money_flow", "authority_reference", "evidence_item", "field_validation"]
    if category not in valid_categories:
        raise HTTPException(status_code=400, detail=f"Invalid category. Must be one of: {valid_categories}")
    
    graph_path = DATA_DIR / "artifacts_graph.json"
    if not graph_path.exists():
        raise HTTPException(status_code=404, detail="Graph data not found.")
    
    with open(graph_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    return [n for n in data["nodes"] if n["category"] == category]


@app.post("/api/run/linkage-analyzer")
async def run_linkage_analyzer():
    """Run the linkage analyzer and update graph data."""
    result = run_script("linkage_analyzer.py", ["--export-all"])
    
    # Reload the updated data
    summary = None
    if result["success"]:
        try:
            summary = await get_summary()
        except:
            pass
    
    return {
        **result,
        "summary": summary
    }


@app.post("/api/run/gap-analyzer")
async def run_gap_analyzer():
    """Run the gap analyzer to detect missing artifacts."""
    result = run_script("gap_analyzer.py")
    return result


@app.post("/api/run/quick-summary")
async def run_quick_summary():
    """Run the quick summary report."""
    result = run_script("quick_summary.py")
    return result


@app.get("/api/flows/top")
async def get_top_flows(limit: int = 10):
    """Get top money flows by amount."""
    graph_path = DATA_DIR / "artifacts_graph.json"
    if not graph_path.exists():
        raise HTTPException(status_code=404, detail="Graph data not found.")
    
    with open(graph_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    flows = [n for n in data["nodes"] if n["category"] == "money_flow"]
    sorted_flows = sorted(
        flows, 
        key=lambda x: x.get("data", {}).get("amount", 0), 
        reverse=True
    )
    
    return sorted_flows[:limit]


# =============================================================================
# Static Files (serve dashboard)
# =============================================================================

# Serve the _data folder for static files
app.mount("/data", StaticFiles(directory=str(DATA_DIR)), name="data")

# Serve dashboard at root
@app.get("/")
async def serve_dashboard():
    """Serve the main dashboard."""
    dashboard_path = DATA_DIR / "index.html"
    if dashboard_path.exists():
        return FileResponse(dashboard_path)
    raise HTTPException(status_code=404, detail="Dashboard not found")


if __name__ == "__main__":
    import uvicorn
    print("=" * 60)
    print("  NAMI Clearlane Dashboard Server")
    print("  http://localhost:8000")
    print("=" * 60)
    uvicorn.run(app, host="0.0.0.0", port=8000)
