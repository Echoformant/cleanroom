# _claims — Claim Assembly Files

**Status:** ACTIVE  
**Purpose:** Stores Claim Assembly bundles that bind multiple artifacts to support factual claims

---

## Overview

A **Claim Assembly** is a bundle that points to multiple artifacts across different categories to support a single factual claim. Claims don't contain new information — they **juxtapose** existing artifacts.

See [docs/claim_assemblies.md](../docs/claim_assemblies.md) for full methodology.

---

## File Naming

```
CLAIM-AR-<TOPIC>-<SEQUENCE>.json
```

Examples:
- `CLAIM-AR-DHS-HIDDEN-OBLIGATIONS-001.json`
- `CLAIM-AR-AOC-CLEAN-ROUTING-001.json`
- `CLAIM-AR-MEDICAID-FEDERAL-MATCH-001.json`

---

## Template

```json
{
  "claim_id": "CLAIM-AR-EXAMPLE-001",
  "claim_statement": "One neutral, factual sentence.",
  "claim_type": "structural",
  "authority_anchors": [],
  "money_anchors": [],
  "evidence_anchors": [],
  "validation_anchors": [],
  "confidence_level": "medium",
  "editor_status": "pending",
  "created_at": "2026-02-05"
}
```

---

## Validation Rule

A valid claim must have:
- At least 1 authority OR money anchor
- At least 1 evidence OR validation anchor

This ensures every claim has both "source of authority" and "proof of reality."

---

## Example

```json
{
  "claim_id": "CLAIM-AR-DHS-HIDDEN-OBLIGATIONS-001",
  "claim_statement": "Participation with DHS programs creates binding obligations that are not visible at the time of engagement.",
  "claim_type": "structural",
  "authority_anchors": [
    "AUTH-AR-ACA-25-10-129"
  ],
  "money_anchors": [],
  "evidence_anchors": [
    "EVID-AR-DHS-PROVIDER-MANUAL-2026"
  ],
  "validation_anchors": [],
  "confidence_level": "medium",
  "editor_status": "pending",
  "created_at": "2026-02-05"
}
```
