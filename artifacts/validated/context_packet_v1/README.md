# Context Packet v1 — Batch Ingestion Files

**Part of:** Operation NAMI Clearlane / VECTOR 1  
**Last Updated:** 2026-02-10  
**Status:** PROCESSED

---

## Purpose

This folder contains batch JSON files from external schema generation sessions. These files were ingested into the production artifact folders on 2026-02-10.

## Files

| File | Status | Artifacts |
|------|--------|-----------|
| `arkansas_public_finance_batch.json` | ✅ Ingested | 15 |
| `arkansas_public_finance_batch (1).json` | ✅ Ingested | 49 |
| `arkansas_public_finance_batch (2).json` | ✅ Ingested | 15 updates |
| `new_artifacts.json` | ✅ Ingested | 16 (15 AUTH, 1 EVID) |
| `field_validations.json` | ✅ Ingested | 115 |
| `field_validation_batch1.json` | ✅ Ingested | 50 |
| `batch_output.json` | ✅ Ingested | 18 (after JSON fix) |
| `batch_orphan_triage.json` | ✅ Ingested | 4 updates, 2 new |

**Total Ingested:** ~280 artifacts/updates

## Ingestion Methods

### Standard Format
Uses `scripts/batch_ingest.py`:
```powershell
python scripts/batch_ingest.py context_packet_v1/arkansas_public_finance_batch.json
```

Expected structure:
```json
{
  "artifacts": {
    "money_flow": [...],
    "authority_reference": [...]
  }
}
```

### Non-Standard Format
Uses custom Python for files with alternate structures.

## Key Artifacts Added

### Constitutional Authorities
- `AUTH-AR-CONST-ART16-SEC1` through `SEC12`

### Budget Process Flows
- `MF-AR-CFO-BUDGET-PLANNING-FY2026`
- `MF-AR-LEGISLATIVE-BUDGET-HEARINGS-FY2026`

### Specialty Court Funding
- `MF-AR-SPPROGRAM-FY2026`
- `MF-AR-ACCOUNTABILITY-FUND-FY2026`

### Field Validations
- 165 new validations covering tobacco settlement, Medicaid expansion, statutory provisions

## Note

This folder is retained for audit trail. Do not delete.
