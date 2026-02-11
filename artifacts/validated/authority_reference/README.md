# Authority Reference Artifacts

**Part of:** Operation NAMI Clearlane / VECTOR 1  
**Last Updated:** 2026-02-10  
**Artifact Count:** 152

---

## Purpose

This folder contains **authority reference** artifacts that document the legal basis for Arkansas public finance activities. These include statutes, regulations, administrative orders, court orders, MOUs, and settlements.

## Schema

| Field | Type | Description |
|-------|------|-------------|
| `authority_id` | string | Unique identifier (e.g., `AUTH-AR-ACA-20-77-107`) |
| `authority_type` | string | See types below |
| `citation` | string | Official citation with Unicode symbols preserved |
| `administering_body` | string | Entity responsible for enforcement |
| `governs[]` | array | IDs of money flows this authority controls |
| `effects` | object | Describes legal effects/impacts |
| `editor_status` | string | `"pending"` or `"accepted"` |

## Authority Types

| Type | Use Case |
|------|----------|
| `statute` | Arkansas Code Annotated sections |
| `regulation` | Agency rules and regulations |
| `act` | Session laws (e.g., Act 776 of 2025) |
| `administrative` | Desk-level authorities, positions, committees |
| `court_order` | Judicial decisions and orders |
| `mou` | Memoranda of understanding |
| `settlement` | Settlement agreements |

## ID Naming Patterns

| Pattern | Example | Meaning |
|---------|---------|---------|
| `AUTH-AR-ACA-*` | `AUTH-AR-ACA-20-77-107` | Arkansas Code citation |
| `AUTH-AR-ACT*` | `AUTH-AR-ACT776-2025-AOC-APPROPRIATION` | Session law |
| `AUTH-AR-CONST-*` | `AUTH-AR-CONST-ART16-SEC1` | Constitutional provision |
| `AUTH-AR-SC-*` | `AUTH-AR-SC-ADMIN-ORDER-14` | Supreme Court order |
| `AUTH-US-*` | `AUTH-US-42-USC-1396` | Federal authority |
| `AR-AUTH-*` | Legacy format (deprecated) |

## Key Artifact Categories

### Constitutional Authorities
- `AUTH-AR-CONST-ART16-SEC1` through `SEC12` - Finance & taxation

### Drug & Specialty Courts
- `AUTH-AR-ACA-16-10-139` - Drug court establishment
- `AUTH-AR-ACA-16-98-303` - Mental health court
- `AUTH-AR-ACA-16-100-203` - Veterans treatment court
- `AUTH-AR-ACA-19-5-1144-ACCOUNTABILITY-COURT-FUND` - Fund creation

### Medicaid & DHS
- `AUTH-AR-ACA-20-77-107` - Medicaid provider requirements
- `AUTH-AR-ACA-20-64-602` - Peer certification authority

### Administrative
- `AUTH-AR-DHS-OSAMH-DIRECTOR` - Director position authority
- `AUTH-AR-LEGISLATIVE-COUNCIL-REVIEW` - Administrative rule review

## File Index (Sample)

```
AUTH-AR-ACA-16-10-139.json
AUTH-AR-ACA-16-98-303.json
AUTH-AR-ACA-16-100-203.json
AUTH-AR-ACA-19-5-1144.json
AUTH-AR-ACA-19-5-1144-ACCOUNTABILITY-COURT-FUND.json
AUTH-AR-ACA-20-64-602.json
AUTH-AR-ACA-20-77-107.json
AUTH-AR-CONST-ART16-SEC1.json
AUTH-AR-SC-ADMIN-ORDER-14.json
...
```

## Usage

```powershell
# Find all constitutional authorities
Get-ChildItem -Filter *CONST*.json

# Find Medicaid-related authorities
Get-ChildItem | Where-Object { (Get-Content $_ | ConvertFrom-Json).governs -match "MEDICAID" }

# List all statute types
Get-ChildItem -Filter *.json | ForEach-Object { 
    $a = Get-Content $_ | ConvertFrom-Json
    [PSCustomObject]@{ID=$a.authority_id; Type=$a.authority_type}
} | Group-Object Type
```

## Linkage

Authority references link to:
- **money_flow**: Via `governs[]` array
- **evidence_item**: As source documentation
- **field_validation**: As evidence basis

Run `python scripts/linkage_analyzer.py --category authority_reference` to see all links.
