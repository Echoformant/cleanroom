# Arkansas Public-Finance Validated Artifacts — AI Guide

This repo catalogs validated artifacts from Arkansas state government appropriations, authorities, evidence, and money flows. Each artifact is a single JSON object with strict schema conventions.

**Part of:** Operation NAMI Clearlane / VECTOR 1  
**Purpose:** Build a law-anchored, schema-validated Dossier for defensible navigation of Arkansas public finance

## Architecture & Data Model

| Folder               | Purpose                                                      | Key ID Field       |
|----------------------|--------------------------------------------------------------|---------------------|
| `money_flow/`        | Tracks money moving between government entities              | `flow_id`           |
| `authority_reference/` | Statutes, rules, and acts that authorize fund use          | `authority_id`      |
| `evidence_item/`     | Budget/legal evidence supporting appropriation claims        | `evidence_id`       |
| `field_validation/`  | Compliance checks and audit alignment records                | `fv_id`             |
| `_manifests/`        | Build output manifests (SHA-keyed); links proposals→outputs  | `cleanroom_sha`     |
| `_gaps/`             | Gap records (JSON) — discovered missing linkages             | `gap_id`            |
| `_stubs/`            | Placeholder artifacts generated for gaps                     | varies              |
| `scripts/`           | Analysis tools (linkage, gap detection)                      | —                   |
| `docs/`              | Canonical definitions and methodology                        | —                   |

### File Organization Pattern
- **Root `.json`**: Pretty-printed, human-readable, canonical copy (2-space indent, trailing newline)
- **`<id>.yaml/0.json`** or **`<id>.json/0.json`**: Minified ingestion snapshot inside a folder matching the ID
- Always update both when editing an artifact

### Field Conventions by Type

**Money Flow** (`MF-*`):
- Field order: `flow_id`, `source`, `intermediary`, `destination`, `amount`, `fund_type`, `fiscal_year`, `restrictions.medicaid`, `restrictions.dhs_controlled`, `statutory_basis`, `statutory_basis_refs`, `editor_status`
- `amount`: integer USD (no commas/decimals); use `0` for unspecified with explanation in `statutory_basis`
- `fund_type`: `"state"` for AR-appropriated (even with federal match); `"federal"` only for direct US inflows
- `intermediary`: `"None"` when no pass-through exists (never omit)
- `fiscal_year`: Use format `"FY2026"` for single years; `"FY2025-2026"` for biennia (always include "FY" prefix)
- `statutory_basis`: Human-readable text citation (e.g., "Ark. Code § 20-77-107")
- `statutory_basis_refs`: Array of authority/evidence IDs that this flow cites (e.g., `["AUTH-AR-ACA-20-77-107", "EVID-AR-ACT776-S25"]`) — enables bidirectional graph traversal
- Canonical: [MF-AR-MEDICAID-PEER-ROUTING-2026.json](money_flow/MF-AR-MEDICAID-PEER-ROUTING-2026.json)

**Authority Reference** (`AR-AUTH-*`, `AUTH-*`):
- Fields: `authority_id`, `authority_type`, `citation`, `administering_body`, `governs[]`, `effects`, `editor_status`
- `authority_type`: `statute` | `regulation` | `act` | `administrative` | `court_order` | `mou` | `settlement`
  - Use `administrative` for desk-level authorities (director positions, committees, delegation chains)
- Match citation style to source (preserve Unicode dashes/section symbols §)
- Example: [AR-AUTH-20-77-107.json](authority_reference/AR-AUTH-20-77-107.json)

**Evidence Item** (`EVID-*`, `EV-*`):
- Fields: `evidence_id`, `section`, `claim_summary`, `evidence_type` (`budget`|`audit`|`policy`), `source{}`, `confidence_level`, `editor_status`
- `source.url` should link to official Arkansas Legislature or agency document
- Example: [EVID-AR-ACT776-2025-S25-SpecialtyCourtProgram-300000-FY2026.json](evidence_item/EVID-AR-ACT776-2025-S25-SpecialtyCourtProgram-300000-FY2026.json)

**Field Validation** (`FV-*`):
- Fields: `fv_id`, `jurisdiction`, `validating_entity`, `alignment_status` (`captured`|`open`|`mixed`), `evidence_basis[]`, `disclosure_level`, `editor_status`
- Example: [FV-AR-LegAudit-AOC-FY2022-AppropriationPurposeFinding.json](field_validation/FV-AR-LegAudit-AOC-FY2022-AppropriationPurposeFinding.json)

## Editing Workflow

1. **Authoring order**: Edit the numbered file inside the `.yaml/` or `.json/` folder first, then paste the pretty-printed version to the root
2. **Editor status**: Use `"pending"` for unverified; promote to `"accepted"` after citation/source validation
3. **Citations**: Use `【docId†Lstart-Lend】` suffix for source line references; keep Unicode symbols from source
4. **Validation**: No build system—use VS Code JSON diagnostics or `pwsh -Command "Get-Content path | jq . > $null"`

## ID Naming Patterns

| Pattern                  | Meaning                                                      |
|--------------------------|--------------------------------------------------------------|
| `MF-AR-*`               | Arkansas money flow (state-level)                            |
| `AR_FY20XX_*`           | Appropriation act tracing (Governor→CFO flow)                |
| `AUTH-US-*`             | Federal authority (SAMHSA, DOJ, etc.)                        |
| `EVID-AR-ACT*-SEC*`     | Budget evidence from specific Act section                    |
| `--001`, `--002` suffix | Multiple flows sharing base name—never renumber              |

## Domain Rules

- **Medicaid flows**: Set `restrictions.medicaid: true` only when destination is Medicaid-reimbursable; cite DHS OBHS Provider Manual
- **DHS-controlled**: `restrictions.dhs_controlled: true` for funds disbursed by DHS or sub-divisions
- **RHTP proposals** (HEART, PACT, RISE AR, THRIVE): Keep descriptions synchronized across all four files; reference Arkansas Senate summaries
- **Fiscal years**: Always use `"FY2026"` format (include "FY" prefix); biennia as `"FY2025-2026"`; multi-year ranges as `"FY2022-2038"`
- **Desk-level authority**: When mapping organizational hierarchies, create `authority_type: "administrative"` artifacts for positions, committees, and delegation chains (e.g., `AUTH-AR-DHS-OSAMH-DIRECTOR`, `AUTH-AR-DHS-PEER-ADVISORY-COMMITTEE`)

## Artifact Linkage

Artifacts reference each other through several fields. The [linkage_analyzer.py](scripts/linkage_analyzer.py) script discovers these relationships:

| Link Type | Source Field | Target Category |
|-----------|--------------|-----------------|
| `section→flow` | evidence_item.section | money_flow |
| `evidence_basis→` | field_validation.evidence_basis[] | evidence_item, authority_reference |
| `governs→` | authority_reference.governs[] | money_flow |
| `statutory_basis→` | money_flow.statutory_basis | authority_reference, evidence_item || `statutory_basis_refs→` | money_flow.statutory_basis_refs[] | authority_reference, evidence_item |
**Usage:**
```powershell
# Show all linkages ranked by volume (most connected first)
python scripts/linkage_analyzer.py

# Show links for a specific artifact
python scripts/linkage_analyzer.py --artifact MF-AR-MEDICAID-PEER-ROUTING-2026

# Show all external links for a category
python scripts/linkage_analyzer.py --category money_flow

# Summary statistics only
python scripts/linkage_analyzer.py --summary
```

## Gap Detection

Gaps are missing linkages where artifacts *should* reference each other but don't. See [docs/canonical_gap_definitions.md](docs/canonical_gap_definitions.md) for full definitions.

### Canonical Gap Types

| Type | ID | Description |
|------|-----|-------------|
| Incomplete Chain | `INCOMPLETE_CHAIN` | Artifact references another artifact ID that doesn't exist |
| Missing Validation | `MISSING_VALIDATION` | Money flow or authority has no field_validation coverage |
| Orphan Reference | `ORPHAN_REFERENCE` | Pattern-matched reference implies a missing artifact |

**Usage:**
```powershell
# Full analysis with stub generation
python scripts/gap_analyzer.py

# Analysis only, no stubs
python scripts/gap_analyzer.py --no-stubs

# Filter by gap type
python scripts/gap_analyzer.py --type MISSING_VALIDATION

# JSON output for visualization pipelines
python scripts/gap_analyzer.py --json > gap_report.json
```

### Gap Workflow
1. Run `gap_analyzer.py` → gaps saved to `_gaps/`, stubs to `_stubs/`
2. Review stub artifacts and research missing information
3. Replace `[GAP STUB - ...]` placeholders with real data
4. Remove `_gap_metadata` field, move to proper category folder
5. Re-run analyzer to confirm closure

## Composite Schema Cycling (Experimental)

A method for systematic gap discovery through schema rotation. See [docs/composite_schema_cycling.md](docs/composite_schema_cycling.md).

**Concept:** Start with one artifact, generate empty templates for the other three types, fill via LLM, rotate anchor through all four types.

```powershell
# Start a cycle with an anchor artifact
python scripts/schema_cycler.py anchor AUTH-AR-ACA-19-5-1144-ACCOUNTABILITY-COURT-FUND

# List all cycles
python scripts/schema_cycler.py list

# Continue after ingesting LLM response
python scripts/schema_cycler.py ingest CYCLE-xxx turn_1_response.json
python scripts/schema_cycler.py continue CYCLE-xxx
```

## Common Tasks

- **Add new artifact**: Choose unique ID with correct prefix, create minified `0.json` in folder, add pretty-printed root twin
- **Update citation**: Modify `statutory_basis` or `citation` only; keep evidence token stable unless PDF changed
- **Check for duplicates**: Search ID substring before creating—batch files may contain staged items
- **Batch promotion**: Copy object from `*_batch*.yaml/N.json`, update `editor_status` to `"accepted"`, move to standalone file
- **Analyze linkages**: Run `python scripts/linkage_analyzer.py` to see artifact connectivity
- **Find gaps**: Run `python scripts/gap_analyzer.py` to discover missing artifacts
- **Run schema cycle**: Use `python scripts/schema_cycler.py anchor <id>` to start systematic gap filling

