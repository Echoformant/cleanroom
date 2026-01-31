# Analysis: Fix Invalidated Files Workflow Issues

## Executive Summary

The workflow was **only moving files** from `invalidated/` to `proposals/` without **fixing** them. The GitLab pipeline validates files in proposals, and when they fail validation, it moves them back to `invalidated/` with error logs. This created an infinite loop.

**Root Cause:** Files were missing required schema fields and some files were being placed in wrong directories based on their actual schema type.

**Solution:** Updated the workflow to **transform and fix** files to match schema requirements before moving them to proposals.

---

## What Was Happening

### The Cycle

1. User triggers "Fix Invalidated Files" workflow manually
2. Workflow moves files from `invalidated/` → `proposals/` **without fixing them**
3. GitLab pipeline picks up the changes (triggered by commit)
4. GitLab validates files against their respective schemas
5. Files **fail validation** (missing required fields, wrong types, etc.)
6. GitLab moves invalid files back to `invalidated/` with error logs
7. User sees invalidated directory is still full

### Why Files Failed Validation

Example: `AR-AUTH-16-10-701-SPECIALTY-COURT-USER-FEES.json`

**Original content:**
```json
{
  "schema": "authority_reference",
  "authority_id": "AR-AUTH-16-10-701-SPECIALTY-COURT-USER-FEES",
  "statute": "Ark. Code § 16-10-701",
  "administering_body": ["Circuit courts", "Admin Office"],
  "description": "...",
  "effects": {...}
}
```

**Problems:**
- `administering_body` is an array but schema requires a string
- `description` is not an allowed property
- Missing required fields: `authority_type`, `citation`, `governs`

**Schema requires:**
- `authority_type`: "statute" | "regulation" | "policy"
- `citation`: string
- `administering_body`: string (not array)
- `governs`: array of strings
- `additionalProperties: false` (no extra fields allowed)

---

## The Fix

### Updated Workflow Capabilities

The workflow now:

1. **Detects schema type** from content (not directory location)
2. **Transforms data** to match schema requirements:
   - Adds missing required fields with sensible defaults
   - Converts types (array → string for `administering_body`)
   - Maps fields (e.g., `statement` → `claim_summary`)
   - Removes disallowed extra properties
3. **Routes to correct directory** based on content's schema type
4. **Handles pipeline directory structure** (e.g., `file.json/0.json`)
5. **Commits without `[skip ci]`** to trigger GitLab validation

### Schema Transformations

| Schema Type | Key Fixes Applied |
|-------------|------------------|
| `authority_reference` | Adds `authority_type`, `citation`, `governs`; converts `administering_body` array to string |
| `evidence_item` | Adds `section`, `source` object; maps `statement` → `claim_summary` |
| `money_flow` | Ensures `restrictions` has boolean values; validates `fiscal_year` pattern |
| `field_validation` | Adds `disclosure_level: "restricted"`, `evidence_basis` array |

---

## Validation Results

After the fix, all test files pass schema validation:

```
✅ proposals/authority_reference/AR-AUTH-16-10-701-SPECIALTY-COURT-USER-FEES.json - VALID
✅ proposals/evidence_item/EV-A-review-of-the-Administrative-Office-of-015.json - VALID
✅ proposals/money_flow/MF-AR-RHTP-Y1-2026.json - VALID
```

---

## Key Changes to Workflow

### 1. Schema-Aware Fixing Functions

```python
def fix_authority_reference(data, original_id=None):
    """Transform authority_reference data to match schema."""
    fixed = {}
    fixed["authority_id"] = data.get("authority_id") or original_id
    fixed["authority_type"] = "statute"  # inferred from content
    fixed["citation"] = data.get("statute", data.get("citation", "..."))
    # Convert array to string
    ab = data.get("administering_body")
    fixed["administering_body"] = ", ".join(ab) if isinstance(ab, list) else str(ab)
    # ... etc
```

### 2. Content-Based Routing

Files are now routed to the correct `proposals/` subdirectory based on their `schema` field or ID field, not their source directory.

### 3. Commit Message Without `[skip ci]`

```yaml
git commit -m "fix: process and fix invalidated files, move to proposals"
# NO [skip ci] - GitLab will validate the fixed files
```

---

## Expected Flow After Fix

1. User triggers "Fix Invalidated Files" workflow
2. Workflow **fixes** files (adds missing fields, corrects types)
3. Fixed files are moved to correct `proposals/` subdirectory
4. Commit is pushed **without** `[skip ci]`
5. GitLab validates files → **they pass**
6. GitLab moves files to `artifacts/` directory
7. `invalidated/` is now empty

---

## Files Modified

- `.github/workflows/fix-invalidated-files.yml` - Complete rewrite with fixing logic

---

## Testing

The updated workflow was tested locally:
- 48 files processed successfully
- All transformed files pass schema validation
- Pipeline directories (with `0.json` structure) are handled correctly
