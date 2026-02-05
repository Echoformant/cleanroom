# Composite Schema Cycling — Methodology

**Status:** EXPERIMENTAL  
**Applies To:** Operation NAMI Clearlane / VECTOR 1  
**Purpose:** Systematic gap discovery and artifact generation through schema rotation

---

## I. Concept

Composite Schema Cycling is a method for discovering and filling gaps in the artifact network by:

1. Starting with a known, validated artifact (the **anchor**)
2. Generating empty schema templates for the other three artifact types
3. Using LLM research to fill those templates based on what the anchor implies
4. Rotating the anchor through all four types to complete one cycle

The key insight: **a single validated artifact implies the existence of related artifacts in the other three categories**. This method makes those implied relationships explicit.

---

## II. The Four Categories

| Order | Category | ID Pattern | Primary Fields |
|-------|----------|------------|----------------|
| 1 | `authority_reference` | `AUTH-*`, `AR-AUTH-*` | citation, governs[], administering_body |
| 2 | `money_flow` | `MF-*`, `AR_FY*` | source, destination, amount, statutory_basis |
| 3 | `evidence_item` | `EVID-*`, `EV-*` | section, claim_summary, source |
| 4 | `field_validation` | `FV-*` | alignment_status, evidence_basis[] |

---

## III. Cycle Structure

### Turn 1: Authority Anchor
```
[ANCHOR: authority_reference]
     ↓
[FILL: money_flow]      ← What funding does this authority govern?
[FILL: evidence_item]   ← What documents support this authority?
[FILL: field_validation] ← Has this authority been validated?
```

### Turn 2: Money Flow Anchor
```
[ANCHOR: money_flow]     ← (promoted from Turn 1)
     ↓
[FILL: authority_reference] ← What authority enables this flow?
[FILL: evidence_item]       ← What documents describe this flow?
[FILL: field_validation]    ← Has this flow been validated?
```

### Turn 3: Evidence Anchor
```
[ANCHOR: evidence_item]  ← (promoted from Turn 2)
     ↓
[FILL: authority_reference] ← What authority does this evidence cite?
[FILL: money_flow]          ← What funding does this evidence describe?
[FILL: field_validation]    ← Has this evidence been validated?
```

### Turn 4: Field Validation Anchor
```
[ANCHOR: field_validation] ← (promoted from Turn 3)
     ↓
[FILL: authority_reference] ← What authority was validated?
[FILL: money_flow]          ← What funding was validated?
[FILL: evidence_item]       ← What evidence supports the validation?
```

---

## IV. Critical Rule: No Reuse Within Cycle

**Within a single cycle, an artifact cannot be used more than once.**

The cycle tracks all used artifacts. When generating new slots, the LLM must produce *new* artifacts, not variations of already-used ones.

This forces the network to expand rather than loop back on itself.

---

## V. Tool Usage

### Start a New Cycle

```powershell
python scripts/schema_cycler.py anchor AUTH-AR-ACA-19-5-1144-ACCOUNTABILITY-COURT-FUND
```

Output:
```
🔄 New Cycle Created: CYCLE-20260204-153000-a1b2c3

Anchor: AUTH-AR-ACA-19-5-1144-ACCOUNTABILITY-COURT-FUND (authority_reference)
Turn: 1 of 4

📄 Prompt file: _cycles/CYCLE-20260204-153000-a1b2c3/turn_1_prompt.json
```

### Send to LLM

1. Open `turn_1_prompt.json`
2. Copy the contents
3. Send to LLM with this instruction:

```
Fill the empty schema slots based on the anchor artifact. 
Research and provide real Arkansas public finance data.
Do not reuse any artifacts listed in used_artifacts.
Return the complete JSON with filled slots.
```

4. Save LLM response to `turn_1_response.json` in the cycle directory

### Ingest Response

```powershell
python scripts/schema_cycler.py ingest CYCLE-20260204-153000-a1b2c3 turn_1_response.json
```

### Continue to Next Turn

```powershell
python scripts/schema_cycler.py continue CYCLE-20260204-153000-a1b2c3
```

### Check Status

```powershell
python scripts/schema_cycler.py status CYCLE-20260204-153000-a1b2c3
```

### List All Cycles

```powershell
python scripts/schema_cycler.py list
```

---

## VI. Cycle Directory Structure

```
_cycles/
└── CYCLE-20260204-153000-a1b2c3/
    ├── state.json              # Cycle state and metadata
    ├── turn_1_prompt.json      # Prompt for Turn 1
    ├── turn_1_response.json    # LLM response (user adds this)
    ├── turn_2_prompt.json      # Generated after ingest
    ├── turn_2_response.json    # LLM response (user adds this)
    ├── turn_3_prompt.json
    ├── turn_3_response.json
    ├── turn_4_prompt.json
    └── turn_4_response.json
```

Generated artifacts are saved to `_stubs/cycle_CYCLE-xxx/` for review before promotion.

---

## VII. When to Use This Method

**Good starting anchors:**

- Authorities that govern multiple flows (`AUTH-AR-ACT776-*`)
- Money flows with complex routing (`AR_FY2026_*`)
- Evidence items from major legislation
- Field validations with audit findings

**Best for:**

- Expanding a known cluster of artifacts
- Discovering implied but undocumented relationships
- Systematic gap filling in a domain

**Not ideal for:**

- Initial artifact discovery (use direct research instead)
- Artifacts with no implied relationships

---

## VIII. Post-Cycle Workflow

After completing a cycle:

1. Review generated artifacts in `_stubs/cycle_CYCLE-xxx/`
2. Validate each artifact against source documents
3. Remove `_gap_metadata` if present
4. Update `editor_status` to `"accepted"` if validated
5. Move to proper category folder
6. Create minified `0.json` version in folder structure
7. Run `gap_analyzer.py` to confirm gap closure

---

## IX. Cycle Chaining

A completed cycle may reveal new anchors for additional cycles.

Example chain:
```
Cycle 1: AUTH-AR-ACT776-2025 → generates MF-AR-SPECIALTY-COURT-NEW
Cycle 2: MF-AR-SPECIALTY-COURT-NEW → generates EVID-AR-SPECIALTY-COURT-NEW
Cycle 3: EVID-AR-SPECIALTY-COURT-NEW → generates FV-AR-SPECIALTY-COURT-NEW
```

Chains continue until:
- No new gaps are discovered
- All generated artifacts are duplicates of existing ones
- Research cannot find source material

---

## X. Version Control

- **Document:** Composite Schema Cycling Methodology
- **Version:** v1
- **Status:** EXPERIMENTAL — Active for testing
- **Amendments:** Append-only
