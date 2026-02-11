# Money Flow Artifacts

**Part of:** Operation NAMI Clearlane / VECTOR 1  
**Last Updated:** 2026-02-10  
**Artifact Count:** 216

---

## Purpose

This folder contains **money flow** artifacts that track the movement of funds between government entities in Arkansas public finance. Each artifact represents a discrete funding stream with source, intermediary (if any), destination, and statutory basis.

## Schema

| Field | Type | Description |
|-------|------|-------------|
| `flow_id` | string | Unique identifier (e.g., `MF-AR-MEDICAID-PEER-ROUTING-2026`) |
| `source` | string | Originating entity or fund |
| `intermediary` | string | Pass-through entity; `"None"` if direct |
| `destination` | string | Receiving entity or program |
| `amount` | integer | USD amount (no decimals); `0` if unspecified |
| `fund_type` | string | `"state"` or `"federal"` |
| `fiscal_year` | string | `"FY2026"` format; biennia as `"FY2025-2026"` |
| `restrictions.medicaid` | boolean | True if Medicaid-reimbursable |
| `restrictions.dhs_controlled` | boolean | True if disbursed by DHS |
| `statutory_basis` | string | Human-readable citation |
| `statutory_basis_refs` | array | IDs of authority/evidence artifacts |
| `editor_status` | string | `"pending"` or `"accepted"` |

## ID Naming Patterns

| Pattern | Meaning |
|---------|---------|
| `MF-AR-*` | Arkansas state-level money flow |
| `MF-US-*` | Federal inflow to Arkansas |
| `AR_FY20XX_*` | Appropriation act tracing |
| `--001`, `--002` | Multiple flows sharing base name |

## Key Artifact Categories

### Medicaid Flows
- `MF-AR-MEDICAID-PEER-ROUTING-2026` - Peer support routing
- `MF-AR-MEDICAID-EXPANSION-*` - Expansion funding streams

### Specialty Court Funding
- `MF-AR-SPPROGRAM-FY2026` - Specialty Court Program Fund ($300K)
- `MF-AR-ACCOUNTABILITY-FUND-FY2026` - Accountability Court Fund ($400K)
- `MF-AR-ADULT-DRUG-COURT-FUNDING` - Drug court appropriations

### Federal Grants
- `MF-US-SAMHSA-*` - SAMHSA grant inflows
- `MF-US-DOJ-*` - Department of Justice grants
- `MF-US-ONDCP-*` - ONDCP Drug-Free Communities

### Budget Process Flows
- `MF-AR-CFO-BUDGET-PLANNING-FY2026` - Planning phase
- `MF-AR-LEGISLATIVE-BUDGET-HEARINGS-FY2026` - Hearings

## File Index (Sample)

```
MF-AR-ACCOUNTABILITY-FUND-FY2026.json
MF-AR-ADULT-DRUG-COURT-FUNDING.json
MF-AR-CFO-BUDGET-PLANNING-FY2026.json
MF-AR-LEGISLATIVE-COUNCIL-ADMIN-RULE-REVIEW-ONGOING.json
MF-AR-MEDICAID-PEER-ROUTING-2026.json
MF-AR-MENTAL-HEALTH-COURT-FEES.json
MF-AR-SAMHSA-ARHP-PEER-GRANT.json
MF-AR-SAMHSA-ATC-VETERANS.json
MF-AR-SPPROGRAM-FY2026.json
MF-AR-WIOA-ONE-STOP-INFRASTRUCTURE-FUNDING-FY2024.json
...
```

## Usage

```powershell
# Count all money flows
(Get-ChildItem -Filter *.json -File).Count

# Find Medicaid flows
Get-ChildItem -Filter *MEDICAID*.json

# Validate JSON syntax
Get-ChildItem -Filter *.json | ForEach-Object { Get-Content $_ | jq . > $null }
```

## Linkage

Money flows link to:
- **authority_reference**: Via `statutory_basis_refs[]`
- **evidence_item**: Via `statutory_basis_refs[]`
- **field_validation**: Flows are validated by FV artifacts

Run `python scripts/linkage_analyzer.py --artifact MF-AR-MEDICAID-PEER-ROUTING-2026` to see connections.
