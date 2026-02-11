# Evidence Item Artifacts

**Part of:** Operation NAMI Clearlane / VECTOR 1  
**Last Updated:** 2026-02-10  
**Artifact Count:** 260

---

## Purpose

This folder contains **evidence item** artifacts that document specific claims, budget line items, audit findings, and policy statements supporting the dossier. Evidence items provide the factual basis for money flows and authority references.

## Schema

| Field | Type | Description |
|-------|------|-------------|
| `evidence_id` | string | Unique identifier (e.g., `EVID-AR-ACT776-2025-S25-SpecialtyCourtProgram`) |
| `section` | string | Money flow ID this evidence supports |
| `claim_summary` | string | What the evidence asserts |
| `evidence_type` | string | `budget`, `audit`, or `policy` |
| `source.document` | string | Document title |
| `source.url` | string | Official URL (Arkansas Legislature preferred) |
| `source.retrieval_date` | string | When document was accessed |
| `confidence_level` | string | `high`, `medium`, or `low` |
| `editor_status` | string | `"pending"` or `"accepted"` |

## Evidence Types

| Type | Description |
|------|-------------|
| `budget` | Appropriation acts, budget proposals, fiscal documents |
| `audit` | Legislative audit findings, compliance reports |
| `policy` | Rules, manuals, policy statements, guidance documents |

## ID Naming Patterns

| Pattern | Example | Meaning |
|---------|---------|---------|
| `EVID-AR-ACT*-SEC*` | `EVID-AR-ACT776-2025-S25-SpecialtyCourtProgram-300000-FY2026` | Act section with amount |
| `EVID-AR-*-HANDBOOK-*` | `EVID-AR-MHC-HANDBOOK-PEERSUPPORT` | Handbook excerpts |
| `EVID-US-*` | `EVID-US-USCODE-DFC-PART-A` | Federal evidence |
| `EV-*` | Legacy format (deprecated) |

## Key Artifact Categories

### Act 776 (2025) Budget Items
- `EVID-AR-ACT776-2025-S25-SpecialtyCourtProgram-300000-FY2026`
- `EVID-AR-ACT776-2025-S30-AccountabilityCourtFund-400000-FY2026`
- Multi-section appropriations for AOC, DHS, courts

### Handbook & Program Evidence
- `EVID-AR-MHC-HANDBOOK-PEERSUPPORT` - Mental health court peer support
- `EVID-AR-ARHP-PEER-GRANT` - SAMHSA peer grant documentation
- `EVID-AR-ADDENDUM-VETERANS-DIVERSION` - Veterans court program

### Federal Grant Evidence
- `EVID-AR-BJA-GRANT-FOR-TREATMENT-COURTS` - BJA treatment court funding
- `EVID-US-SAMHSA-*` - SAMHSA grant documentation

### Audit Findings
- `EVID-AR-LEGAUDIT-*` - Legislative audit excerpts
- `EVID-AR-AOC-AUDIT-*` - AOC-specific findings

## File Index (Sample)

```
EVID-AR-ACT776-2025-S25-SpecialtyCourtProgram-300000-FY2026.json
EVID-AR-ADDENDUM-VETERANS-DIVERSION.json
EVID-AR-ARHP-PEER-GRANT.json
EVID-AR-BJA-GRANT-FOR-TREATMENT-COURTS.json
EVID-AR-ISP-2021-107-CONTRACTS.json
EVID-AR-MHC-HANDBOOK-PEERSUPPORT.json
EVID-AR-MOU-WIOA.json
EVID-US-USCODE-DFC-PART-A.json
...
```

## Citation Format

Evidence items may include source line references in the format:
```
【docId†Lstart-Lend】
```

Example: `【993523828842590†L631-L741】` refers to lines 631-741 of document ID 993523828842590.

## Usage

```powershell
# Count by evidence type
Get-ChildItem -Filter *.json | ForEach-Object {
    (Get-Content $_ | ConvertFrom-Json).evidence_type
} | Group-Object | Select-Object Name, Count

# Find all ACT776 evidence
Get-ChildItem -Filter *ACT776*.json

# Validate sources have URLs
Get-ChildItem -Filter *.json | ForEach-Object {
    $e = Get-Content $_ | ConvertFrom-Json
    if (-not $e.source.url) { Write-Host "Missing URL: $($_.Name)" }
}
```

## Linkage

Evidence items link to:
- **money_flow**: Via `section` field
- **authority_reference**: As supporting documentation
- **field_validation**: Via `evidence_basis[]` array

Run `python scripts/linkage_analyzer.py --category evidence_item` to see all links.
