# Temporary Context Packet — Working Archive

**Status:** ARCHIVE (Do Not Delete)  
**Purpose:** Original concept documents used to bootstrap Operation NAMI Clearlane  
**Rule:** Files remain here as historical reference; canonical versions live in `docs/`

---

## Overview

This folder contains the foundational concepts, methods, and LLM instructions developed during the early phases of Operation NAMI Clearlane. These documents were used to:

1. Define the operational framework (VECTOR 1, Clearlane, Dossier)
2. Establish the four artifact schemas
3. Create the model behavioral contract
4. Document core methods (360° visibility, three lanes, desk-touch maps)

---

## Canonization Status

See [docs/canonization_status.md](../docs/canonization_status.md) for a detailed review of what has been canonized vs. remains draft.

**Key concepts now in docs/:**
- Canonical Gap Definitions (`docs/canonical_gap_definitions.md`)
- Composite Schema Cycling (`docs/composite_schema_cycling.md`)

**Key concepts still here (priority for canonization):**
- Claim Assemblies (`methods_concepts/CLAIM ASSEMBLIES!!!!.md`)
- Clearlane Agency Doctrine (`methods_concepts/Clearlane Agency Doctrine v1.md`)
- Clearlane Core Methods (`methods_concepts/Clearlane_Core_Methods_Draft_v1.md`)

---

## Folder Structure

```
temp_context_packet/
├── README.md                    # This file
├── instructions_llm/            # (empty - superseded by LLM_op_instructions)
├── LLM_op_instructions/         # Model contracts and instruction YAML
│   ├── # Instruction Set...md   # Full instruction set with schemas
│   ├── vector1_clearlane_instruction.yaml
│   └── llm_op_instructions/     # (subfolder)
└── methods_concepts/            # Core methodology documents
    ├── Arkansas Named Desk Roster v1.md
    ├── CLAIM ASSEMBLIES!!!!.md           # KEY - Binding method
    ├── Clearlane Administrative Overlay Matrix v1.md
    ├── Clearlane Agency Doctrine v1.md   # KEY - Agency framework
    ├── Clearlane Desk-Touch Map v1 (Arkansas).md
    ├── Clearlane Latent Authority Trigger Register v1.md
    ├── Clearlane_Core_Methods_Draft_v1.md # KEY - 360° visibility
    ├── Clearlane_Executive_Assembly_Doctrine.md
    ├── clearlane_guide_mapping_hidden_authority_layers.md
    ├── Clearlane_Operations_Binder_PLACEHOLDER.md
    └── NAMI_Clearlane_Guide_Draft_v1.md
```

---

## Usage Rule

**Do not delete or move files from this folder.**

When canonizing a concept:
1. Create the canonical version in `docs/`
2. Reference this folder as the source
3. Update `docs/canonization_status.md`
