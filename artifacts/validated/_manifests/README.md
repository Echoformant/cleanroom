# Build Manifests

**Part of:** Operation NAMI Clearlane / VECTOR 1  
**Last Updated:** 2026-02-10  
**Manifest Count:** 316

---

## Purpose

This folder contains build output manifests that link proposal SHA hashes to generated artifacts. Each manifest captures the state of a batch ingestion or schema cycling run.

## File Naming

Files are named by SHA hash:
```
{cleanroom_sha}.json
```

Example: `004922c15087fc840c87ba53ef440f423b94fcce.json`

## Schema

| Field | Type | Description |
|-------|------|-------------|
| `cleanroom_sha` | string | SHA-256 hash of input proposal |
| `created_at` | string | ISO timestamp |
| `source_file` | string | Original input file |
| `artifacts_created` | array | List of artifact IDs generated |
| `artifacts_updated` | array | List of artifact IDs modified |
| `validation_status` | string | `passed`, `failed`, or `pending` |

## Usage

```powershell
# Find manifest by SHA prefix
Get-ChildItem -Filter 004922*.json

# List recent manifests
Get-ChildItem -Filter *.json | Sort-Object LastWriteTime -Descending | Select-Object -First 10

# Count artifacts in a manifest
$m = Get-Content 004922c15087fc840c87ba53ef440f423b94fcce.json | ConvertFrom-Json
$m.artifacts_created.Count
```

## Workflow

1. Proposal submitted (batch file, LLM response, etc.)
2. SHA computed from proposal content
3. Artifacts ingested to appropriate folders
4. Manifest written linking SHA → artifacts

## See Also

- [scripts/batch_ingest.py](../scripts/README.md) - Ingestion script
- [_gaps/README.md](../_gaps/README.md) - Gap records
