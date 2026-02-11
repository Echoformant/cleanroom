# 990 Processed Files

**Part of:** Operation NAMI Clearlane / VECTOR 1  
**Last Updated:** 2026-02-10

---

## Purpose

Archive of IRS Form 990 XML files that have been successfully extracted.

## Workflow

Files are moved here from `_990_queue/` after the extraction daemon processes them (unless `--no-move` flag is used).

## Current Status

When processing from external queue (e.g., `moonlight/data/teos/xmls`) with `--no-move`, this folder remains mostly empty since source files stay in place.

## See Also

- [_990_queue/README.md](../_990_queue/README.md) - Input queue
- [_990_extracted/README.md](../_990_extracted/README.md) - Extraction output
