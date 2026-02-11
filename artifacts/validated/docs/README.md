# Documentation

**Part of:** Operation NAMI Clearlane / VECTOR 1  
**Last Updated:** 2026-02-10

---

## Purpose

This folder contains canonical methodology documents, specifications, and design documentation for the Clearlane dossier system.

## Document Index

| Document | Purpose |
|----------|---------|
| `990_pipeline_architecture.md` | 990 extraction pipeline design |
| `canonical_gap_definitions.md` | Gap type definitions and detection rules |
| `canonization_status.md` | Artifact promotion workflow |
| `claim_assemblies.md` | Claim structure and evidence linking |
| `composite_schema_cycling.md` | Schema rotation methodology |
| `free_stack_architecture_index.md` | System architecture overview |
| `key_registry_spec.md` | Entity key registry specification |
| `recommendations.md` | Strategic recommendations |
| `ux_concepts_tricia.md` | User experience concepts |

## Key Documents

### canonical_gap_definitions.md
Defines the three canonical gap types:
- `INCOMPLETE_CHAIN` - Broken references
- `MISSING_VALIDATION` - No field_validation coverage
- `ORPHAN_REFERENCE` - Pattern-implied gaps

### composite_schema_cycling.md
Explains the four-artifact rotation method for systematic gap discovery.

### key_registry_spec.md
Specifies how entities (from 990s) are linked to artifact graph via EIN and name matching.

### 990_pipeline_architecture.md
Documents the extraction pipeline:
```
XML → Ollama LLM → Markdown → Key Registry → Artifact Linking
```

## Contributing

When adding new methodology:
1. Create `.md` file with descriptive name
2. Include date and status header
3. Link from this README
4. Reference from relevant script READMEs
