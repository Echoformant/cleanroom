# Field Validation Artifacts

**Part of:** Operation NAMI Clearlane / VECTOR 1  
**Last Updated:** 2026-02-10  
**Artifact Count:** 197

---

## Purpose

This folder contains **field validation** artifacts that document compliance checks, audit alignment, and verification of claims across the dossier. Field validations connect evidence to specific money flows and authorities to confirm their validity.

## Schema

| Field | Type | Description |
|-------|------|-------------|
| `fv_id` | string | Unique identifier (e.g., `FV-AR-LegAudit-AOC-FY2022-AppropriationPurposeFinding`) |
| `jurisdiction` | string | Geographic/legal scope (`AR`, `US`, etc.) |
| `validating_entity` | string | Who performed the validation |
| `alignment_status` | string | `captured`, `open`, or `mixed` |
| `evidence_basis[]` | array | IDs of evidence/authority artifacts |
| `disclosure_level` | string | `public`, `restricted`, `confidential` |
| `editor_status` | string | `"pending"` or `"accepted"` |

## Alignment Status

| Status | Meaning |
|--------|---------|
| `captured` | Fully documented and verified |
| `open` | Requires additional research/evidence |
| `mixed` | Partially verified, some gaps remain |

## ID Naming Patterns

| Pattern | Example | Meaning |
|---------|---------|---------|
| `FV-AR-*` | `FV-AR-LegAudit-AOC-FY2022-AppropriationPurposeFinding` | Arkansas validation |
| `FV-US-*` | Federal validation |
| `FV-GAP-*` | Gap placeholder (needs completion) |
| `FIELD-AR-*` | Field-level verification (policy/procedure) |

## Key Artifact Categories

### Legislative Audit Findings
- `FV-AR-LegAudit-*` - Legislative audit compliance checks
- `FV-AR-AOC-AUDIT-*` - AOC-specific audit alignment

### Tobacco Settlement
- `FV-AR-TOBACCO-*` - Master Settlement Agreement compliance
- Validation of TSR fund usage

### Medicaid Expansion  
- `FV-AR-MEDICAID-*` - Expansion funding verification
- Provider enrollment validations

### Statutory Provisions
- `FV-AR-STATUTORY-*` - Code section validations
- Constitutional requirement checks

### Policy/Procedure Fields
- `FIELD-AR-PEER-CERTIFICATION` - Peer worker certification requirements
- `FIELD-AR-NON-DHS-PATHWAY` - Non-DHS funding confirmation
- `FIELD-AR-PEER-SUPPORT-ALLOWED` - Peer support service validation

## File Index (Sample)

```
FIELD-AR-NON-DHS-PATHWAY.json
FIELD-AR-PEER-CERTIFICATION.json
FIELD-AR-PEER-SUPPORT-ALLOWED.json
FV-AR-LegAudit-AOC-FY2022-AppropriationPurposeFinding.json
FV-AR-MEDICAID-EXPANSION-2014.json
FV-AR-TOBACCO-MSA-FUND-USAGE.json
...
```

## Batch Ingestion History

| Date | Batch | Count |
|------|-------|-------|
| 2026-02-10 | field_validations.json | 115 |
| 2026-02-10 | field_validation_batch1.json | 50 |
| 2026-02-10 | batch_output.json | 3 |

## Usage

```powershell
# Count by alignment status
Get-ChildItem -Filter *.json | ForEach-Object {
    (Get-Content $_ | ConvertFrom-Json).alignment_status
} | Group-Object | Select-Object Name, Count

# Find open validations
Get-ChildItem -Filter *.json | Where-Object {
    (Get-Content $_ | ConvertFrom-Json).alignment_status -eq "open"
}

# List all gap placeholders
Get-ChildItem -Filter FV-GAP-*.json
```

## Linkage

Field validations link to:
- **evidence_item**: Via `evidence_basis[]` array
- **authority_reference**: Via `evidence_basis[]` array
- **money_flow**: Indirectly through evidence chain

Run `python scripts/linkage_analyzer.py --category field_validation` to see all links.

## Gap Closure Workflow

1. Identify `FV-GAP-*` or `alignment_status: "open"` artifacts
2. Research missing documentation
3. Update `evidence_basis[]` with new evidence IDs
4. Change `alignment_status` to `"captured"`
5. Remove `_gap_metadata` field if present
