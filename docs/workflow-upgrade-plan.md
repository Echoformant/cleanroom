# Workflow Upgrade Plan: fix-invalidated-files.yml

This document outlines planned improvements to the `fix-invalidated-files.yml` workflow for future implementation.

## Background

The current workflow has limitations when processing:
- Multi-document YAML files (files with `---` separators)
- Mixed schema types in a single file (e.g., `money_flow` + `evidence_item`)
- Git push race conditions with the `clearlane-pipeline` bot

## Option A: Multi-Document YAML + Schema-Type Routing

### Changes Required

1. **Replace `yaml.safe_load()` with `yaml.safe_load_all()`**
   ```python
   # Current (fails on multi-doc YAML)
   data = yaml.safe_load(content)
   
   # Proposed (handles multi-doc YAML)
   for doc in yaml.safe_load_all(content):
       process_document(doc)
   ```

2. **Add schema type detection per document**
   ```python
   def detect_schema_type(doc):
       # Check for wrapper keys
       for schema_type in ["evidence_item", "money_flow", "field_validation", "authority_reference"]:
           if schema_type in doc:
               return schema_type, doc[schema_type]
       
       # Check for ID fields (unwrapped documents)
       id_to_type = {
           "evidence_id": "evidence_item",
           "flow_id": "money_flow",
           "fv_id": "field_validation",
           "authority_id": "authority_reference"
       }
       for id_field, schema_type in id_to_type.items():
           if id_field in doc:
               return schema_type, doc
       
       return None, None
   ```

3. **Route each document to correct subdirectory**
   ```python
   schema_type, item = detect_schema_type(doc)
   target_dir = PROPOSALS_DIR / schema_type
   ```

### Potential Issues

- **Filename collisions**: Multiple documents may generate same filename. Mitigation: Use content-based hashing or sequential numbering.
- **Partial failures**: If one document fails, others may still succeed. Need to decide: fail all or continue?
- **Duplicate detection**: Same content in multiple files. Mitigation: Content hash deduplication.

---

## Option E: Full Production-Ready Upgrade

### Features to Add

1. **Git pull-before-push with retry**
   ```yaml
   - name: Commit and push changes
     run: |
       git add proposals/ reports/ invalidated/
       if ! git diff --staged --quiet; then
         git commit -m "fix: process invalidated files"
         for i in {1..3}; do
           git pull --rebase origin main && git push && break
           sleep 5
         done
       fi
   ```

2. **Schema validation before moving**
   ```python
   import jsonschema
   
   def validate_against_schema(item, schema_type):
       schema_path = Path(f"schemas/{schema_type}.schema.json")
       with open(schema_path) as f:
           schema = json.load(f)
       jsonschema.validate(item, schema)
   ```

3. **Auto-fill missing required fields**
   ```python
   DEFAULTS = {
       "money_flow": {
           "fund_type": "state",
           "fiscal_year": "2025-2026",
       },
       "evidence_item": {
           "evidence_type": "field_validation",
           "confidence_level": "medium"
       }
   }
   
   for field, default in DEFAULTS.get(schema_type, {}).items():
       if field not in item:
           item[field] = default
   ```

4. **Detailed error reporting**
   ```python
   errors = []
   for file_path in files:
       try:
           process_file(file_path)
       except Exception as e:
           errors.append({"file": str(file_path), "error": str(e)})
   
   if errors:
       save_json(REPORTS_DIR / "processing-errors.json", errors)
   ```

5. **Idempotent processing**
   ```python
   def already_processed(item, schema_type):
       id_field = SCHEMA_CONFIG[schema_type]["id_field"]
       item_id = item.get(id_field)
       if not item_id:
           return False
       target_file = PROPOSALS_DIR / schema_type / f"{sanitize(item_id)}.json"
       return target_file.exists()
   ```

6. **Conditional `[skip ci]`**
   Consider using a different marker or workflow filter:
   ```yaml
   on:
     push:
       branches: [main]
       paths-ignore:
         - 'reports/**'
   ```

---

## Alternative: Replace `[skip ci]` with Path Filtering

Instead of using `[skip ci]` to prevent infinite loops:

```yaml
# In other workflows that should not trigger on pipeline commits
on:
  push:
    branches: [main]
    paths-ignore:
      - 'reports/**'
      - 'proposals/**'
```

This way, commits that only touch `reports/` or `proposals/` won't trigger other workflows, but the commit message remains clean.

---

## Implementation Priority

1. **Option A** (Multi-doc YAML + routing) - Medium effort, high value
2. **Git retry logic** - Low effort, prevents push failures
3. **Schema validation + auto-fill** - Medium effort, improves data quality
4. **Full Option E** - Higher effort, production-hardened

---

## Related Files

- `.github/workflows/fix-invalidated-files.yml` - Main workflow file
- `schemas/*.schema.json` - JSON schemas for validation
- `invalidated/` - Source directory
- `proposals/` - Target directory
