# 990 Processing Queue

**Part of:** Operation NAMI Clearlane / VECTOR 1  
**Last Updated:** 2026-02-10

---

## Purpose

Staging area for IRS Form 990 XML files awaiting extraction by the daemon.

## Workflow

1. Place XML files in this folder
2. Run `python scripts/daemon_990_extractor.py --queue-dir _990_queue`
3. Daemon processes files and outputs to `_990_extracted/`
4. Processed XMLs move to `_990_done/` (unless `--no-move` flag used)

## Expected File Format

- IRS 990 XML files from TEOS dataset
- Naming pattern: `{ObjectId}_public.xml`
- UTF-8 encoding

## Current Status

Queue is typically empty when daemon has completed processing.

## See Also

- [_990_extracted/README.md](../_990_extracted/README.md) - Extraction output
- [scripts/README.md](../scripts/README.md) - Daemon documentation
