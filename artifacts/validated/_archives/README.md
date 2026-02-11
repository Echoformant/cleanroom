# Archives

**Part of:** Operation NAMI Clearlane / VECTOR 1  
**Last Updated:** 2026-02-10

---

## Purpose

This folder stores archived artifacts, deprecated schemas, and historical snapshots that are no longer in active use but retained for reference.

## Contents

- Old schema versions
- Superseded artifact versions
- Experimental artifacts that weren't promoted
- Backup copies before major refactors

## Naming Convention

Archived files include date suffix:
```
{original_name}_{YYYYMMDD}.json
```

## Retrieval

If you need to restore an archived artifact:
1. Find the file in this folder
2. Review for compatibility with current schema
3. Update any deprecated fields
4. Copy to appropriate production folder
5. Update `editor_status` if needed

## Note

This folder is excluded from linkage analysis to avoid false positives.
