# Gap Records

**Part of:** Operation NAMI Clearlane / VECTOR 1  
**Last Updated:** 2026-02-10  
**Gap Count:** 376

---

## Purpose

This folder contains gap records documenting missing linkages in the artifact network. Each gap represents an artifact that should exist but hasn't been created yet.

## Gap Types

| Type | ID | Description |
|------|-----|-------------|
| Incomplete Chain | `INCOMPLETE_CHAIN` | Artifact references another that doesn't exist |
| Missing Validation | `MISSING_VALIDATION` | Money flow/authority has no field_validation |
| Orphan Reference | `ORPHAN_REFERENCE` | Pattern implies missing artifact |

## Schema

| Field | Type | Description |
|-------|------|-------------|
| `gap_id` | string | Unique identifier (e.g., `GAP-MF-AR-MISSING-MEDICAID-001`) |
| `gap_type` | string | One of the canonical types above |
| `source_artifact` | string | ID of artifact with the broken reference |
| `expected_target` | string | ID of artifact that should exist |
| `discovered_at` | string | ISO timestamp |
| `resolution_status` | string | `open`, `stub_created`, `resolved` |

## Workflow

1. Run `python scripts/gap_analyzer.py`
2. Gaps saved to `_gaps/`, stubs to `_stubs/`
3. Review stub artifacts and research missing info
4. Replace placeholders with real data
5. Move completed artifacts to proper category folder
6. Re-run analyzer to confirm closure

## Usage

```powershell
# List all open gaps
Get-ChildItem -Filter *.json | ForEach-Object {
    $g = Get-Content $_ | ConvertFrom-Json
    if ($g.resolution_status -eq "open") { $_.Name }
}

# Count by gap type
Get-ChildItem -Filter *.json | ForEach-Object {
    (Get-Content $_ | ConvertFrom-Json).gap_type
} | Group-Object | Select-Object Name, Count

# Find gaps for specific artifact
Get-ChildItem -Filter *.json | Where-Object {
    (Get-Content $_ | ConvertFrom-Json).source_artifact -match "MEDICAID"
}
```

## See Also

- [docs/canonical_gap_definitions.md](../docs/canonical_gap_definitions.md) - Full definitions
- [_stubs/README.md](../_stubs/README.md) - Generated stubs
- [scripts/gap_analyzer.py](../scripts/README.md) - Gap detection script
