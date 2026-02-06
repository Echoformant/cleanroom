# Claim Assemblies — Binding Method for Multi-Artifact Claims

**Status:** CANON  
**Source:** temp_context_packet/methods_concepts/CLAIM ASSEMBLIES!!!!.md  
**Purpose:** Define the method for binding multiple artifacts to support a single factual claim

---

## I. What Is a Claim Assembly?

A **Claim Assembly** is not a new schema. It's a **temporary bundle** that answers one question:

> *"What do we know, and what proves it?"*

You don't change the artifacts.  
You **point to them together**.

---

## II. The Core Rule

**If a statement cannot be supported by at least two different schema types, it's not operational yet.**

A valid Claim Assembly requires artifacts from at least two categories:
- authority_reference (what allows it)
- money_flow (what funds it)
- evidence_item (what states it)
- field_validation (what confirms it)

---

## III. Building a Claim Assembly

### Step 1: Define ONE Claim (Neutral, Factual)

Write a single factual sentence. No intent, no blame, no interpretation.

**Examples:**
- "Participation with DHS programs creates binding obligations that are not visible at the time of engagement."
- "AOC specialty court funds flow through state appropriations without DHS intermediation."
- "Federal matching requirements attach conditions to state behavioral health spending."

### Step 2: Pull Artifacts by Role

For each claim, identify artifacts by **function**:

| Role | Schema Type | Count |
|------|-------------|-------|
| **Authority Anchor** (what allows it) | authority_reference | 1-2 |
| **Money Anchor** (what funds it) | money_flow | 0-2 |
| **Evidence Anchor** (what states it) | evidence_item | 1-2 |
| **Reality Anchor** (what confirms it) | field_validation | 0-2 |

You're not summarizing them. You're **juxtaposing** them.

### Step 3: Create the Claim Table

```
CLAIM: [one sentence]

Authority (allows it):
  - AUTH-AR-[X]
  - AUTH-AR-[Y]

Money (funds it):
  - MF-AR-[A]

Evidence (states it):
  - EVID-AR-[B]
  - EVID-AR-[C]

Field Validation (confirms it):
  - FV-AR-[D]
```

No commentary. Anyone reading this can:
- See the logic
- Check the sources
- Understand the conclusion *without you saying it*

---

## IV. Claim Assembly Schema

```json
{
  "claim_id": "CLAIM-AR-DHS-HIDDEN-OBLIGATIONS-001",
  "claim_statement": "Participation with DHS programs creates binding obligations that are not visible at the time of engagement.",
  "claim_type": "structural",
  "authority_anchors": [
    "AUTH-AR-ACA-25-10-129",
    "AUTH-AR-DHS-PROVIDER-MANUAL"
  ],
  "money_anchors": [
    "MF-AR-MEDICAID-PEER-ROUTING-2026"
  ],
  "evidence_anchors": [
    "EVID-AR-DHS-PROVIDER-OBLIGATIONS-2026"
  ],
  "validation_anchors": [
    "FV-AR-DHS-AUDIT-2025"
  ],
  "confidence_level": "high",
  "editor_status": "pending",
  "created_at": "2026-02-05"
}
```

### Field Definitions

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `claim_id` | string | ✓ | Pattern: `CLAIM-AR-*` |
| `claim_statement` | string | ✓ | One neutral, factual sentence |
| `claim_type` | enum | ✓ | `"structural"` \| `"funding"` \| `"compliance"` \| `"risk"` |
| `authority_anchors` | array[string] | ✓ | Authority IDs (min 0) |
| `money_anchors` | array[string] | | Money flow IDs (optional) |
| `evidence_anchors` | array[string] | ✓ | Evidence IDs (min 1) |
| `validation_anchors` | array[string] | | Field validation IDs (optional) |
| `confidence_level` | enum | ✓ | `"high"` \| `"medium"` \| `"low"` |
| `editor_status` | enum | ✓ | `"pending"` \| `"accepted"` |
| `created_at` | string | ✓ | ISO date |

### Validation Rule

```
(authority_anchors.length + money_anchors.length) >= 1
AND
(evidence_anchors.length + validation_anchors.length) >= 1
```

A claim must have at least one "source of authority" AND at least one "proof of reality."

---

## V. Claim Types

| Type | Description | Typical Anchors |
|------|-------------|-----------------|
| `structural` | How systems are designed to operate | authority + evidence |
| `funding` | How money moves or is controlled | money + authority |
| `compliance` | Whether requirements are being met | validation + evidence |
| `risk` | Where capture or constraint exists | all four types |

---

## VI. Why This Works

Claim Assemblies let you:

- **Point**, not explain
- **Prove**, not persuade
- **Pause**, not defend

When asked "Show me where that's coming from," you point to a **bundle**, not a paragraph.

---

## VII. Relationship to Clearlane

Clearlane is not a report. It's a **decision firewall**.

Claim Assemblies let you:
- Flag risk
- Justify exits
- Defend refusals
- Explain caution

Without writing essays.

---

## VIII. Usage

### Manual Assembly

Create a JSON file in `_claims/`:

```powershell
# Create claim file
New-Item _claims/CLAIM-AR-DHS-HIDDEN-OBLIGATIONS-001.json
```

### Future: Script-Assisted

```powershell
# (Not yet implemented)
python scripts/claim_table.py --claim "DHS programs create hidden obligations" \
  --authority AUTH-AR-ACA-25-10-129 \
  --evidence EVID-AR-DHS-PROVIDER-OBLIGATIONS-2026
```

---

## IX. File Organization

```
_claims/
├── README.md
├── CLAIM-AR-DHS-HIDDEN-OBLIGATIONS-001.json
├── CLAIM-AR-AOC-CLEAN-ROUTING-001.json
└── ...
```

Claims are stored in `_claims/` folder, separate from the four core artifact categories.
