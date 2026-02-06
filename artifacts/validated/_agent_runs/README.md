# _agent_runs — GPT Agent Mode Instruction Files

**Status:** ACTIVE  
**Created:** 2026-02-05  
**Purpose:** Contains structured instruction files for running batch artifact generation in GPT Agent mode

---

## Overview

This folder stores the instruction files (prompts) designed to be pasted into GPT Agent mode for executing multi-turn Composite Schema Cycling runs. Each file is a self-contained prompt with:

- Canonical schema definitions
- Anchor artifact specification
- Turn structure and output format
- Expected artifact counts

---

## Files

| File | Description |
|------|-------------|
| `AGENT_RUN_EXHAUSTIVE_25-10-129.md` | 4-turn exhaustive cycle anchored on `AUTH-AR-ACA-25-10-129` (DHS Federal Fund Conformity) |

---

## Naming Convention

```
AGENT_RUN_<MODE>_<ANCHOR_ID>.md
```

- **MODE:** `EXHAUSTIVE` (4-turn), `QUICK` (1-turn), `TARGETED` (specific gap)
- **ANCHOR_ID:** Short form of the anchor artifact ID

---

## Usage

1. Open the `.md` file
2. Copy the entire contents
3. Paste into GPT Agent mode (or any LLM with web access)
4. Wait for completion
5. Save output as JSON
6. Ingest with: `python scripts/batch_ingest.py <output_file>`

---

## Output Format

Agent runs should return a JSON object structured as:

```json
{
  "batch_id": "BATCH-<ANCHOR_ID>-<MODE>",
  "anchor_id": "<full_anchor_id>",
  "mode": "<exhaustive-4-turn | quick-1-turn | targeted>",
  "generated_at": "YYYY-MM-DD",
  "total_turns": 4,
  "artifacts": {
    "money_flow": [...],
    "authority_reference": [...],
    "evidence_item": [...],
    "field_validation": [...]
  },
  "turn_log": [...],
  "research_notes": "..."
}
```

---

## Related

- [docs/composite_schema_cycling.md](../docs/composite_schema_cycling.md) — Method documentation
- [scripts/batch_ingest.py](../scripts/batch_ingest.py) — Batch ingestion script
- [scripts/schema_cycler.py](../scripts/schema_cycler.py) — Programmatic cycle management
