# Formulas & Schemas

**Part of:** Operation NAMI Clearlane / VECTOR 1  
**Last Updated:** 2026-02-10

---

## Purpose

This folder contains reusable formulas, prompt schemas, and extraction definitions used by analysis tools. These are the "instructions" that guide LLM-based data extraction and entity registration.

## Structure

```
_formulas/
├── 990/              # IRS Form 990 extraction formulas
│   ├── tier1_core/        # Production-ready formulas
│   ├── tier2_useful/      # Validated but specialized
│   ├── tier3_experimental/ # Testing/development
│   ├── _deprecated/       # Retired formulas
│   ├── _raw/              # Unprocessed imports
│   └── _triage/           # Awaiting classification
│
└── key_registry/     # Entity key mapping schemas
    └── key_registry.schema.json
```

## 990 Formulas

Prompt templates for extracting structured data from IRS 990 XML files using Ollama LLM.

Current production formula: `tier1_core/990_forensics_extractor_v1.md`

See [990/README.md](990/README.md) for details.

## Key Registry

Schema for linking entities across 990 filings and artifact graph.

See [key_registry/README.md](key_registry/README.md) for details.

## Usage

Formulas are loaded by scripts like:
- `scripts/daemon_990_extractor.py` - Uses 990 formulas
- `scripts/key_registry_manager.py` - Uses key_registry schema

## Tiering System

| Tier | Status | Use |
|------|--------|-----|
| tier1_core | Production | Active scripts reference these |
| tier2_useful | Validated | Specialized use cases |
| tier3_experimental | Testing | Development only |
| _deprecated | Retired | Historical reference |
| _raw | Unprocessed | Needs review |
| _triage | Pending | Awaiting classification |
