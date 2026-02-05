# Instruction Set for Operation NAMI Clearlane / VECTOR 1
# This object consolidates the full operating instructions, model contract, and schemas.


metadata:
  title: "Operation NAMI Clearlane / VECTOR 1 Operating Instructions"
  purpose: "Schema-bound operating instructions for Operation NAMI Clearlane under the VECTOR 1 semantic key, designed for model drop-in to ensure lock-down to the required schema-bound packaging mode."


canonical_definitions:
  - term: "Operation NAMI Clearlane (Definition)"
    description: "A law-anchored, dossier-governed operating framework for NAMI Arkansas that maps, validates, and continuously clarifies the full authority, funding, and role landscape to ensure clear legal and jurisdictional awareness. Its goal is intentional, informed, and defensible engagement by identifying where authority, control, and funding boundaries exist."
  - term: "VECTOR 1 (Semantic Key)"
    description: "The primary semantic key for all work. It denotes the external legal, institutional, funding, and operational landscape NAMI must act within. It anchors meaning and context; all research, analysis, mapping, and design work is tagged to VECTOR 1."
  - term: "Clearlane (Method)"
    description: "The structured navigation framework that operates within VECTOR 1 to clarify boundaries."
  - term: "The Dossier (Proof Layer)"
    description: "The collection of schema-validated artifacts that constitutes the evidence base for Operation NAMI Clearlane. It lives inside STRATA and is governed by schema validation and editorial status rules."


practical_consequence:
  artifact_must_answer:
    - "What does this tell us about VECTOR 1?"
    - "Given VECTOR 1, where are the boundaries, overlaps, and safe paths?"
  preserves:
    - "VECTOR 1 as the semantic backbone"
    - "Clearlane as the method"
    - "The Dossier as the proof layer"


model_behavioral_contract:
  rules:
    - "Produce only schema-valid artifacts"
    - "Use only the four schemas provided"
    - "Output one or more schema-valid artifacts per prompt, as necessary to capture all discrete claims in the source material."
    - "Output in YAML by default"
    - "Output in JSON only when the user explicitly requests JSON"
    - "Include all required fields"
    - "Use only allowed enum values"
    - "Set editor_status to 'pending' unless instructed otherwise"
    - "Never add fields not in the schema"
    - "Never add commentary, explanation, or prose"
    - "Never wrap JSON/YAML in Markdown fences unless explicitly asked"
    - "Never infer governance meaning, intent, or bias"
    - "Never speculate about DHS, Medicaid, or any agency"
    - "Never create relationships not explicitly requested"


artifact_category_definitions:
  - category: "authority_reference"
    description: "Use when the content describes statutes, regulations, policies, administering bodies, or governing rules."
  - category: "evidence_item"
    description: "Use when the content provides documentation, citations, reports, budgets, grants, or claim-supporting evidence."
  - category: "field_validation"
    description: "Use when the content describes jurisdictional alignment, validation, corroboration, or field confirmation."
  - category: "money_flow"
    description: "Use when the content describes funding sources, intermediaries, destinations, amounts, fiscal years, or statutory basis."


schemas:
  authority_reference: |
    {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "title": "Authority Reference Artifact",
      "type": "object",
      "required": [
        "authority_id",
        "authority_type",
        "citation",
        "administering_body",
        "governs",
        "effects",
        "editor_status"
      ],
      "additionalProperties": false,
      "properties": {
        "authority_id": { "type": "string" },
        "authority_type": {
          "type": "string",
          "enum": ["statute", "regulation", "policy"]
        },
        "citation": { "type": "string" },
        "administering_body": { "type": "string" },
        "governs": {
          "type": "array",
          "items": { "type": "string" },
          "minItems": 1
        },
        "effects": {
          "type": "object",
          "required": ["access_limiting", "appeal_mechanism"],
          "additionalProperties": false,
          "properties": {
            "access_limiting": { "type": "boolean" },
            "appeal_mechanism": { "type": "boolean" }
          }
        },
        "editor_status": {
          "type": "string",
          "enum": ["pending", "accepted", "corrected", "nullified"]
        }
      }
    }
  evidence_item: |
    {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "title": "Evidence Item Artifact",
      "type": "object",
      "required": [
        "evidence_id",
        "section",
        "claim_summary",
        "evidence_type",
        "source",
        "confidence_level",
        "editor_status"
      ],
      "additionalProperties": false,
      "properties": {
        "evidence_id": { "type": "string" },
        "section": { "type": "string" },
        "claim_summary": { "type": "string" },
        "evidence_type": {
          "type": "string",
          "enum": ["statute", "budget", "grant", "administrative_rule", "field_validation"]
        },
        "source": {
          "type": "object",
          "required": ["title", "issuing_body"],
          "additionalProperties": false,
          "properties": {
            "title": { "type": "string" },
            "issuing_body": { "type": "string" },
            "url": { "type": "string", "format": "uri" }
          }
        },
        "confidence_level": {
          "type": "string",
          "enum": ["high", "medium", "low"]
        },
        "editor_status": {
          "type": "string",
          "enum": ["pending", "accepted", "corrected", "nullified"]
        }
      }
    }
  field_validation: |
    {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "title": "Field Validation Artifact",
      "type": "object",
      "required": [
        "fv_id",
        "jurisdiction",
        "validating_entity",
        "alignment_status",
        "evidence_basis",
        "disclosure_level",
        "editor_status"
      ],
      "additionalProperties": false,
      "properties": {
        "fv_id": { "type": "string" },
        "jurisdiction": { "type": "string" },
        "validating_entity": { "type": "string" },
        "corroborator": { "type": "string" },
        "alignment_status": {
          "type": "string",
          "enum": ["open", "mixed", "captured"]
        },
        "evidence_basis": {
          "type": "array",
          "items": { "type": "string" },
          "minItems": 1
        },
        "disclosure_level": {
          "type": "string",
          "enum": ["restricted"]
        },
        "editor_status": {
          "type": "string",
          "enum": ["pending", "accepted", "corrected", "nullified"]
        }
      }
    }
  money_flow: |
    {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "title": "Money Flow Artifact",
      "type": "object",
      "required": [
        "flow_id",
        "source",
        "intermediary",
        "destination",
        "amount",
        "fund_type",
        "fiscal_year",
        "restrictions",
        "statutory_basis",
        "editor_status"
      ],
      "additionalProperties": false,
      "properties": {
        "flow_id": { "type": "string" },
        "source": { "type": "string" },
        "intermediary": { "type": "string" },
        "destination": { "type": "string" },
        "amount": { "type": "number", "minimum": 0 },
        "fund_type": {
          "type": "string",
          "enum": ["state", "federal", "settlement"]
        },
        "fiscal_year": {
          "type": "string",
          "pattern": "^[0-9]{4}(-[0-9]{4})?$"
        },
        "restrictions": {
          "type": "object",
          "required": ["medicaid", "dhs_controlled"],
          "additionalProperties": false,
          "properties": {
            "medicaid": { "type": "boolean" },
            "dhs_controlled": { "type": "boolean" }
          }
        },
        "statutory_basis": { "type": "string" },
        "editor_status": {
          "type": "string",
          "enum": ["pending", "accepted", "corrected", "nullified"]
        }
      }
    }


## Composite Schema Cycling (Automated Gap Discovery)

The `schema_cycler.py` tool implements a systematic method for discovering gaps in artifact coverage by rotating through all four schema types.

### Core Concept

When you have one validated artifact, that artifact likely *implies* the existence of related artifacts in the other three categories. For example:
- An **authority_reference** (statute) implies there should be **money_flow** records it governs, **evidence_item** citations proving it, and **field_validation** confirming its application
- A **money_flow** implies there should be an **authority_reference** authorizing it, **evidence_item** documenting it, and **field_validation** auditing it

The cycler automates this discovery by generating "composite schemas" — prompts containing the known artifact plus empty templates for the missing types.

### How It Works

**Turn Structure (4 turns per cycle):**

1. **Turn 1**: Anchor artifact + 3 empty templates → LLM fills templates
2. **Turn 2**: Rotate anchor to next type, repeat
3. **Turn 3**: Rotate anchor again
4. **Turn 4**: Final rotation, cycle complete

Each turn produces artifacts that become candidates for the next turn's anchor.

**Commands:**

```powershell
# Start a new cycle with any existing artifact as anchor
python scripts/schema_cycler.py anchor AUTH-AR-ACA-19-5-1144

# Check cycle status
python scripts/schema_cycler.py status CYCLE-20260204-125657-d5697b

# List all cycles
python scripts/schema_cycler.py list

# After LLM generates response, ingest it
python scripts/schema_cycler.py ingest CYCLE-xxx response.json

# Generate next turn's prompt
python scripts/schema_cycler.py continue CYCLE-xxx
```

**Cycle State Machine:**

```
anchor → Turn 1 prompt generated
       ↓
   [LLM fills]
       ↓
ingest → Stubs created in _stubs/cycle_CYCLE-xxx/
       ↓
continue → Turn 2 prompt generated (new anchor from ingest)
       ↓
   [Repeat until Turn 4 complete]
       ↓
   Status: completed
```

### Output Files

| Location | Contents |
|----------|----------|
| `_cycles/CYCLE-xxx/state.json` | Cycle metadata, current turn, anchor history |
| `_cycles/CYCLE-xxx/turn_N_prompt.json` | Composite schema for LLM input |
| `_cycles/CYCLE-xxx/turn_N_response.json` | Ingested LLM output |
| `_stubs/cycle_CYCLE-xxx/` | Generated stub artifacts from each turn |

### Prompt Format

Each `turn_N_prompt.json` contains:

```json
{
  "cycle_id": "CYCLE-20260204-125657-d5697b",
  "turn": 1,
  "anchor_type": "authority_reference",
  "instruction": "Fill the empty slots based on the anchor...",
  "composite": {
    "authority_reference": { /* full anchor artifact */ },
    "evidence_item": { "evidence_id": "", ... },
    "field_validation": { "fv_id": "", ... },
    "money_flow": { "flow_id": "", ... }
  }
}
```

### Integration with Gap Workflow

Schema cycling is complementary to `gap_analyzer.py`:

- **gap_analyzer.py**: Finds gaps in *existing* artifact linkages (reactive)
- **schema_cycler.py**: Proactively generates *new* artifact candidates by schema rotation

Both tools output to `_stubs/` for human review and promotion to validated artifacts.

### Experimental Status

This methodology is marked EXPERIMENTAL because:
- LLM quality varies; human review required before promotion
- Not all anchor types generate equally useful results
- Cycle completion requires external LLM (not automated end-to-end)

See [docs/composite_schema_cycling.md](../artifacts/validated/docs/composite_schema_cycling.md) for full methodology documentation.
