# Origins → Moves → Direction (Artifacts + 990/TEOS)

Date: 2026-02-02 (inventory from this session)

## Where things started
- **`gle/funding_intel/`** — First schema-governed dossier for authority_reference, evidence_item, field_validation, money_flow (with schemas and narrative profiles). README documents governance and validation patterns; clearlane_pipeline_README sketches the CI/CD contract (raw → proposals → artifacts/validated).
- **`gle/clearlane/`** — A minimal lane declaring that only Governance CI–validated artifacts are authoritative; empty `artifacts/validated/` placeholder for that lane.
- **TEOS origin: `gle/.pulse/teos/`** — Moonlight parser born here: index fetcher + XML parser targeting select EINs (AR focus). README documents TEOS URLs, scope (2021–2023), outputs (`ein_filings.json`, `facts_teos.csv`).

## How it evolved
- **Cleanroom as the new center:** `cleanroom/artifacts/validated/` became the working, CI-like dataset:
  - Rich catalogs under `authority_reference/`, `evidence_item/`, `field_validation/`, `money_flow/`.
  - Ops scaffolding: `_agent_runs/`, `_gaps/`, `_manifests/`, `_archives/`, `_batched_turns/`, `_990_queue/_extracted/_done`, `_formulas/990/`, `scripts/` (daemon_990_extractor, ingest/gap analyzers), `server/`, temp context packets, LLM control contracts.
  - Canonical docs under `artifacts/validated/docs/` (990 pipeline architecture, gap definitions, canonization status, composite schema cycling, key registry).
  - `temp_context_packet/` retains the early concept/LLM instruction binders; README marks archival status.
  - `_formulas/990/README` lays out the extraction formula library tiers.
  - `scripts/README_990_DAEMON` shows the Ollama-based 990 extraction workflow tied to the `_990_*` queues.
- **Moonlight split for 990 work:** `moonlight/` repo created to work TEOS/990 without disturbing cleanroom. Later, GLE TEOS assets (indexes, XMLs, outputs, zips, scripts) were mirrored into `moonlight/data/teos/*_gle` for provenance.

## Current state on disk
- **Validated artifacts (authoritative set):** `cleanroom/artifacts/validated/` with full ops/logs/tooling and 990 extraction helpers.
- **TEOS/990 pipelines:** 
  - Legacy GLE pipeline: `gle/.pulse/teos/` (AR-focused, 2021–2023 indexes).
  - Moonlight pipeline: `moonlight/data/teos/` (2013–2016 indexes/xmls/facts + mirrored GLE TEOS assets under `_gle`).
- **Historical concept docs:** `cleanroom/artifacts/validated/temp_context_packet/` (LLM instructions, methods) and canonicalized versions in `cleanroom/artifacts/validated/docs/`.

## Direction
- **Unify into a new repo** that cleanly combines:
  - TEOS/990 ingestion (indexes/zips/xmls, fetch/parse scripts, 990 formula library, queues/daemon).
  - Clearlane/Operation NAMI artifact governance (authority/evidence/field_validation/money_flow, gap analyzers, CI contract).
  - Shared docs and control contracts (LLM instructions, canonization status).
  - Provenance-preserving subfolders (`*_gle`, `_archives`, `_agent_runs`) copied as-is.
- **Proposed top-level skeleton for the new repo:**
  - `data/teos/` → indexes, zips, xmls, out (plus `_gle` provenance).
  - `artifacts/validated/` → move the entire cleanroom validated tree intact.
  - `scripts/` → TEOS fetch/parse, 990 daemon, gap/linkage analyzers.
  - `docs/` → merged canonical docs (pipeline architecture, gap definitions, ops binders).
  - `schemas/` (if separated from artifacts) and `tools/` (helper/ingest).
  - `ops/` (optional) → queues (`_990_*`), agent runs, manifests, evaluations.

## Intent mapping (what each locus was for)
- `gle/funding_intel/` → First governed dossier + schemas for funding intelligence.
- `gle/clearlane/` → Lane declaration for governance-only artifacts (CI authority).
- `gle/.pulse/teos/` → Original Moonlight TEOS fetch/parse (AR EINs, 2021–2023).
- `moonlight/` → Isolated TEOS/990 workbench; later mirrored GLE TEOS assets for provenance.
- `cleanroom/artifacts/validated/` → Canonical artifact set + ops, gap engine, LLM control, 990 extraction scripts and queues; effectively the living “truth” workspace.

## Next moves (if we proceed)
- Instantiate the new repo with the skeleton above.
- Copy `cleanroom/artifacts/validated/` intact; wire scripts/daemon to the new `data/teos/` paths.
- Decide TEOS scope expansion (add 2017 index, broaden years/states) and normalize 990 outputs into the artifact workflow.
- Keep legacy repos untouched as archives until the new repo is stable.
