# Schema Cycling Sessions

**Part of:** Operation NAMI Clearlane / VECTOR 1  
**Last Updated:** 2026-02-10

---

## Purpose

This folder stores active and completed schema cycling sessions. Schema cycling is a systematic method for discovering gaps by rotating through all four artifact types.

## Concept

Starting from one "anchor" artifact, the cycler generates empty templates for the other three types. An LLM fills these templates, then the process rotates the anchor through each type to build out the full network.

## Workflow

```
1. Start: anchor AUTH-AR-ACA-19-5-1144
   ├── Generate: empty money_flow template
   ├── Generate: empty evidence_item template  
   └── Generate: empty field_validation template

2. LLM fills templates

3. Ingest responses

4. Rotate anchor to next filled artifact

5. Repeat until network saturated
```

## Usage

```powershell
# Start a new cycle
python scripts/schema_cycler.py anchor AUTH-AR-ACA-19-5-1144-ACCOUNTABILITY-COURT-FUND

# List all cycles
python scripts/schema_cycler.py list

# Ingest LLM response
python scripts/schema_cycler.py ingest CYCLE-xxx turn_1_response.json

# Continue to next turn
python scripts/schema_cycler.py continue CYCLE-xxx
```

## File Structure

Each cycle creates a folder:
```
CYCLE-{timestamp}/
├── manifest.json      # Cycle metadata
├── turn_0_prompt.md   # Initial prompt
├── turn_0_response.json  # LLM response
├── turn_1_prompt.md   # Next turn prompt
└── ...
```

## See Also

- [docs/composite_schema_cycling.md](../docs/composite_schema_cycling.md) - Full methodology
- [scripts/schema_cycler.py](../scripts/README.md) - Cycler script
