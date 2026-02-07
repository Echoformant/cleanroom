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

### Focused Batch Runs (Priority Order)

| File | Priority | Est. Time | Description |
|------|----------|-----------|-------------|
| `AGENT_RUN_BATCH_DHS_PEER_CHAIN.md` | **HIGHEST** | 45-60m | DHS→Medicaid→Peer authority chain |
| `AGENT_RUN_BATCH_KIRK_LANE_PROFILE.md` | HIGH | 45-60m | Complete Kirk Lane position mapping |
| `AGENT_RUN_BATCH_FEDERAL_AUTHORITIES.md` | HIGH | 30-45m | Federal statute/regulation backfill |
| `AGENT_RUN_BATCH_990_ARORP_PREP.md` | HIGH | 30-45m | EIN manifest for ARORP recipients |
| `AGENT_RUN_BATCH_SPECIALTY_COURTS.md` | MED-HIGH | 30-45m | AOC pathway (non-DHS alternative) |
| `AGENT_RUN_BATCH_RHTP_PROPOSALS.md` | MEDIUM | 30-45m | Four Senate healthcare proposals |

### Exhaustive Cycling Runs

| File | Description |
|------|-------------|
| `AGENT_RUN_V2_SEEDS_11-20.md` | Seeds 11-20 exhaustive cycling |
| `AGENT_RUN_V2_SEEDS_21-30.md` | Seeds 21-30 exhaustive cycling |
| `AGENT_RUN_EXHAUSTIVE_25-10-129.md` | DHS Federal Fund Conformity anchor |
| `AGENT_RUN_EXHAUSTIVE_CYCLING_V2.md` | V2 cycling methodology |
| `AGENT_RUN_EXHAUSTIVE_FULL_GRAPH.md` | Full graph exploration |
| `AGENT_RUN_EXHAUSTIVE_MEDICAID_WAIVERS.md` | Medicaid waiver focus |

### Gap Fill Runs

| File | Description |
|------|-------------|
| `AGENT_RUN_GAP_FILL_VALIDATIONS.md` | Create missing field_validations |
| `AGENT_RUN_GAP_FILL_ORPHANS.md` | Triage 59 orphan artifacts |

### Other

| File | Description |
|------|-------------|
| `AGENT_RUN_ARORP_DOSSIER.md` | ARORP/Kirk Lane cluster (largely complete) |
| `AGENT_RUN_DHS_DESK_MAPPING.md` | DHS internal hierarchy |
| `AGENT_RUN_AGENCY_SWEEP.md` | Agency profile mapping |
| `AGENT_RUN_DEEP_RESEARCH_EXTRACTION.md` | Deep research → batch format |

---

## Logs

Run logs are stored in `_logs/` folder. See `_logs/README.md` for format.

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
