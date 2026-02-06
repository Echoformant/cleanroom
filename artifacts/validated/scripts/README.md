# Clearlane Artifact Analysis Scripts

This directory contains Python scripts for analyzing the validated artifacts repository.

## Requirements

- Python 3.10+
- No external dependencies (uses only standard library)

---

## Scripts

### 1. linkage_analyzer.py

**Purpose:** Discovers and displays relationships between artifacts across all four categories.

**What it finds:**
- `section→flow`: Evidence items referencing money flows
- `evidence_basis→`: Field validations referencing evidence/authorities
- `governs→`: Authorities governing money flows
- `statutory_basis→`: Money flows citing authorities/evidence

#### Usage

```powershell
# Default: Show summary + volume ranking (most connected artifacts first)
python scripts/linkage_analyzer.py

# Show all links for a specific artifact
python scripts/linkage_analyzer.py --artifact MF-AR-MEDICAID-PEER-ROUTING-2026
python scripts/linkage_analyzer.py -a AUTH-AR-ACA-19-5-1144-ACCOUNTABILITY-COURT-FUND

# Show external links for all artifacts in a category
python scripts/linkage_analyzer.py --category money_flow
python scripts/linkage_analyzer.py -c field_validation

# Summary statistics only
python scripts/linkage_analyzer.py --summary
python scripts/linkage_analyzer.py -s
```

#### Output Examples

**Volume Ranking:**
```
📊 Linkage Volume Ranking (Top 30)
================================================================================

  1. [ 67 links] AUTH-AR-ACT776-2025-AOC-APPROPRIATIONS-SPECIAL-LANGUAGE
      Category: authority_reference
      ←money_flow AR_FY2026_AOC_BYRNE_JAG_BEHAVIORAL_HEALTH_COLLAB...
```

**Single Artifact:**
```
📄 MF-AR-MEDICAID-PEER-ROUTING-2026
   Category: money_flow
   Path: .../money_flow/MF-AR-MEDICAID-PEER-ROUTING-2026.yaml

   🔗 Linkages (1 total):

   [statutory_basis→]
      → AR-ACA-20-77-135-peer-support (authority_reference)
```

---

### 2. gap_analyzer.py

**Purpose:** Discovers gaps in the artifact network where references exist but target artifacts are missing.

**Gap Types (Canonical):**

| Type | ID | Description |
|------|-----|-------------|
| Incomplete Chain | `INCOMPLETE_CHAIN` | An artifact references another artifact ID that doesn't exist |
| Missing Validation | `MISSING_VALIDATION` | A money_flow or authority has no field_validation coverage |
| Orphan Reference | `ORPHAN_REFERENCE` | A pattern-matched reference implies a missing artifact |

See [docs/canonical_gap_definitions.md](../docs/canonical_gap_definitions.md) for full definitions.

#### Usage

```powershell
# Full analysis: find all gaps, generate stubs, save to _gaps/ and _stubs/
python scripts/gap_analyzer.py

# Analysis only, no stub generation
python scripts/gap_analyzer.py --no-stubs

# Filter by gap type
python scripts/gap_analyzer.py --type INCOMPLETE_CHAIN
python scripts/gap_analyzer.py --type MISSING_VALIDATION
python scripts/gap_analyzer.py --type ORPHAN_REFERENCE

# Summary statistics only
python scripts/gap_analyzer.py --summary

# Output full report as JSON (for visualization pipelines)
python scripts/gap_analyzer.py --json
python scripts/gap_analyzer.py --json > gap_report.json
```

#### Output Structure

**Console Output:**
```
📊 Gap Analysis Summary
================================================================================

Total artifacts analyzed: 150
Total gaps discovered: 89

Gaps by type:
  INCOMPLETE_CHAIN: 12
  MISSING_VALIDATION: 65
  ORPHAN_REFERENCE: 12

Gaps by source category:
  authority_reference: 23
  evidence_item: 31
  money_flow: 35

Missing artifacts by expected category:
  authority_reference: 8
  evidence_item: 4
  field_validation: 65
  money_flow: 12
```

**Generated Files:**

```
_gaps/
  GAP-INCOMPLETE-MF-AR-EXAMPLE-AUTH-AR-99-99-999.json
  GAP-NOVALIDATION-MF-AR-MEDICAID-PEER-ROUTING-2026.json
  ...

_stubs/
  AUTH-AR-99-99-999.json
  FV-GAP-MF-AR-MEDICAID-PEER-ROUTING-2026.json
  ...
```

#### Gap Record Format

```json
{
  "gap_id": "GAP-INCOMPLETE-MF-AR-EXAMPLE-AUTH-AR-99-99-999",
  "gap_type": "INCOMPLETE_CHAIN",
  "source_artifact": "MF-AR-EXAMPLE-2026",
  "source_category": "money_flow",
  "source_field": "statutory_basis",
  "target_reference": "AUTH-AR-99-99-999",
  "target_category": "authority_reference",
  "detected_at": "2026-02-04T15:30:00+00:00",
  "stub_generated": true,
  "stub_path": "C:/.../validated/_stubs/AUTH-AR-99-99-999.json"
}
```

#### Stub Artifact Format

Generated stubs include a `_gap_metadata` field for tracking:

```json
{
  "authority_id": "AUTH-AR-99-99-999",
  "authority_type": "statute",
  "citation": "[GAP STUB - citation needed]",
  "administering_body": "[GAP STUB - administering body needed]",
  "governs": ["[GAP STUB - governs entries needed]"],
  "effects": {
    "access_limiting": false,
    "appeal_mechanism": false
  },
  "editor_status": "pending",
  "_gap_metadata": {
    "generated_by": "gap_analyzer",
    "gap_type": "INCOMPLETE_CHAIN",
    "source_artifact": "MF-AR-EXAMPLE-2026",
    "detected_at": "2026-02-04T15:30:00+00:00"
  }
}
```

---

## Workflow

### Typical Analysis Session

```powershell
# 1. Check current linkage health
python scripts/linkage_analyzer.py --summary

# 2. Find all gaps
python scripts/gap_analyzer.py

# 3. Review gaps by type
python scripts/gap_analyzer.py --type MISSING_VALIDATION

# 4. Export for visualization/reporting
python scripts/gap_analyzer.py --json > reports/gap_report_2026-02-04.json

# 5. Review generated stubs
Get-ChildItem _stubs/*.json | Select-Object -First 5

# 6. Fill gaps by researching and replacing stubs with real artifacts
# Move completed artifacts from _stubs/ to appropriate category folder
# Update editor_status from "pending" to "accepted"

# 7. Re-run analysis to confirm gap closure
python scripts/gap_analyzer.py --summary
```

### Filling Gaps

1. Review stub artifacts in `_stubs/`
2. Research the missing information
3. Replace `[GAP STUB - ...]` placeholders with real data
4. Remove the `_gap_metadata` field
5. Move the artifact to its proper category folder
6. Create the minified `0.json` version in a folder
7. Update `editor_status` to `"accepted"`
8. Delete the corresponding gap record from `_gaps/`

---

## Directory Structure

```
validated/
├── scripts/
│   ├── README.md           # This file
│   ├── linkage_analyzer.py # Relationship discovery
│   ├── gap_analyzer.py     # Gap detection + stub generation
│   └── schema_cycler.py    # Composite Schema Cycling tool
├── docs/
│   ├── canonical_gap_definitions.md  # Gap type definitions (CANON)
│   └── composite_schema_cycling.md   # Cycling methodology (EXPERIMENTAL)
├── _gaps/                  # Gap records (JSON)
├── _stubs/                 # Generated stub artifacts
├── _cycles/                # Schema cycling state and prompts
├── money_flow/
├── authority_reference/
├── evidence_item/
└── field_validation/
```

---

### 3. schema_cycler.py

**Purpose:** Implements Composite Schema Cycling — a method for systematic gap discovery through schema rotation.

**Concept:** Start with one artifact (anchor), generate empty templates for the other three types, fill them via LLM, then rotate the anchor through all four types.

See [docs/composite_schema_cycling.md](../docs/composite_schema_cycling.md) for full methodology.

#### Usage

```powershell
# Start a new cycle with an anchor artifact
python scripts/schema_cycler.py anchor AUTH-AR-ACA-19-5-1144-ACCOUNTABILITY-COURT-FUND

# List all cycles
python scripts/schema_cycler.py list

# Check cycle status
python scripts/schema_cycler.py status CYCLE-20260204-125657-d5697b

# Ingest LLM response after filling slots
python scripts/schema_cycler.py ingest CYCLE-20260204-125657-d5697b turn_1_response.json

# Continue to next turn (after ingesting response)
python scripts/schema_cycler.py continue CYCLE-20260204-125657-d5697b
```

#### Workflow

1. **Start cycle:** `schema_cycler.py anchor <artifact_id>`
2. **Get prompt:** Open `_cycles/CYCLE-xxx/turn_1_prompt.json`
3. **Send to LLM:** Ask LLM to fill the empty slots
4. **Save response:** Save LLM output to `turn_1_response.json` in cycle folder
5. **Ingest:** `schema_cycler.py ingest CYCLE-xxx turn_1_response.json`
6. **Continue:** `schema_cycler.py continue CYCLE-xxx`
7. **Repeat:** Steps 2-6 for turns 2, 3, 4
8. **Review:** Check generated artifacts in `_stubs/cycle_CYCLE-xxx/`

#### Cycle Output

```
_cycles/
└── CYCLE-20260204-125657-d5697b/
    ├── state.json              # Cycle tracking
    ├── turn_1_prompt.json      # Anchor + empty slots
    ├── turn_1_response.json    # (user saves LLM response here)
    ├── turn_2_prompt.json      # (generated after ingest)
    └── ...

_stubs/cycle_CYCLE-20260204-125657-d5697b/
    ├── MF-AR-NEW-FLOW-2026.json
    ├── EVID-AR-NEW-EVIDENCE.json
    └── FV-AR-NEW-VALIDATION.json
```

---

### 4. find_orphans.py

**Purpose:** Lists all orphan artifacts — those with no incoming or outgoing linkages.

#### Usage

```powershell
# List all orphans by category
python scripts/find_orphans.py
```

#### Output

```
ORPHAN ARTIFACTS
================================================================================

Total: 55 orphans

money_flow (29 orphans):
  - MF-AR-OPIOID-SETTLEMENT-FY2026
  - MF-AR-FEDERAL-BLOCK-GRANT-2026
  ...

evidence_item (17 orphans):
  - EVID-AR-ACT776-S15-APPROPRIATION-2026
  ...
```

---

### 5. quick_summary.py

**Purpose:** Prints a quick overview of repository statistics.

#### Usage

```powershell
python scripts/quick_summary.py
```

#### Output

```
CLEARLANE VALIDATED ARTIFACTS SUMMARY
================================================================================
Total Artifacts: 181
Total Money Tracked: $10,659,714,946

By Category:
  money_flow: 85 artifacts
  authority_reference: 41 artifacts
  evidence_item: 44 artifacts
  field_validation: 11 artifacts

Linkage Health:
  Total Linkages: 2,058
  Orphan Artifacts: 55
```

---

### 6. batch_ingest.py

**Purpose:** Ingests batch artifact outputs from GPT Agent runs.

#### Usage

```powershell
# Ingest a batch JSON file
python scripts/batch_ingest.py path/to/agent_output.json

# Preview only (no file writes)
python scripts/batch_ingest.py path/to/agent_output.json --dry-run
```

#### Expected Input Format

```json
{
  "batch_id": "BATCH-AUTH-AR-25-10-129-EXHAUSTIVE",
  "artifacts": {
    "money_flow": [...],
    "authority_reference": [...],
    "evidence_item": [...],
    "field_validation": [...]
  }
}
```

---

## Future Enhancements

- [ ] Mermaid/GraphViz visualization output
- [ ] HTML report generation
- [ ] Gap priority scoring (optional)
- [ ] Claim Assembly validation
- [ ] Schema validation on ingest
- [ ] Dossier state snapshots
