# Canonical Gap Definitions — Operation NAMI Clearlane

**Status:** CANON  
**Applies To:** VECTOR 1 / Clearlane Dossier  
**Purpose:** Define the three foundational gap types that the gap analyzer detects  
**Method:** Append-only; new gap types may be added but existing definitions are immutable

---

## I. What Is a Gap?

A **gap** is a missing linkage between artifacts that *should* exist based on the references, citations, or structural requirements present in existing validated artifacts.

Gaps are **signals, not failures**. They reveal where the Dossier is incomplete and guide artifact collection priority.

**Canonical Rule:** Gaps are equal in discovery priority. All gaps must be surfaced; prioritization is a separate operational decision.

---

## II. The Three Foundational Gap Types

### GAP-001: INCOMPLETE_CHAIN

**Definition:** An artifact references another artifact (by ID, citation, or structural pointer) that does not exist in the Dossier.

**Detection Pattern:**
- `money_flow.statutory_basis` references an authority or evidence ID → that ID does not exist
- `authority_reference.governs[]` lists a flow ID → that flow does not exist
- `evidence_item.section` references a flow ID → that flow does not exist
- `field_validation.evidence_basis[]` lists an evidence or authority ID → that ID does not exist

**Example:**
```json
{
  "flow_id": "MF-AR-EXAMPLE-2026",
  "statutory_basis": "Ark. Code § 99-99-999 (AUTH-AR-99-99-999)"
}
```
If `AUTH-AR-99-99-999` does not exist as an artifact → **INCOMPLETE_CHAIN**

**Stub Generation:** Creates a placeholder artifact for the missing target.

---

### GAP-002: MISSING_VALIDATION

**Definition:** A `money_flow` or `authority_reference` artifact exists but has no corresponding `field_validation` artifact that references it in `evidence_basis[]`.

**Detection Pattern:**
- For each `money_flow`: search all `field_validation.evidence_basis[]` arrays → if none reference the flow → gap
- For each `authority_reference`: search all `field_validation.evidence_basis[]` arrays → if none reference it → gap

**Rationale:** Field validation confirms that an authority or money flow has been checked against real-world implementation. Missing validation means the artifact is unconfirmed.

**Example:**
```
MF-AR-MEDICAID-PEER-ROUTING-2026 exists
No field_validation artifact references it in evidence_basis[]
→ MISSING_VALIDATION gap
```

**Stub Generation:** Creates a placeholder `field_validation` artifact pointing to the unvalidated source.

---

### GAP-003: ORPHAN_REFERENCE

**Definition:** An artifact references a section, flow, or authority that implies another artifact should exist, but the reference does not match any existing artifact ID.

**Detection Pattern:**
- `evidence_item.section` contains a flow-like pattern (e.g., `AR_FY2026_*`, `MF-*`) → no matching `money_flow` exists
- `authority_reference.governs[]` contains entries that look like flow IDs → no matching flow exists
- Any free-text field contains an artifact ID pattern → no matching artifact exists

**Difference from INCOMPLETE_CHAIN:** Orphan references are *implied* links found via pattern matching, not explicit ID references. They catch cases where the referencing artifact uses descriptive text rather than exact IDs.

**Example:**
```json
{
  "evidence_id": "EVID-AR-ACT776-2025-S25-SpecialtyCourtProgram-300000-FY2026",
  "section": "AR_FY2026_AOC_DRUG_COURT_ENHANCEMENT_SPECIALTY_COURT_PROGRAM_FUND_ACT776_SEC27 (Act 776 §25)"
}
```
If `AR_FY2026_AOC_DRUG_COURT_ENHANCEMENT_SPECIALTY_COURT_PROGRAM_FUND_ACT776_SEC27` does not exist → **ORPHAN_REFERENCE**

**Stub Generation:** Creates a placeholder artifact for the orphaned target.

---

## III. Gap Record Schema

All detected gaps are output as JSON records for tracking and future visualization.

```json
{
  "gap_id": "GAP-<TYPE>-<SOURCE_ID>-<TARGET_ID>",
  "gap_type": "INCOMPLETE_CHAIN | MISSING_VALIDATION | ORPHAN_REFERENCE",
  "source_artifact": "<artifact_id that contains the reference>",
  "source_category": "<money_flow | authority_reference | evidence_item | field_validation>",
  "source_field": "<field name containing the reference>",
  "target_reference": "<the referenced ID or pattern>",
  "target_category": "<expected category of missing artifact>",
  "detected_at": "<ISO timestamp>",
  "stub_generated": true | false,
  "stub_path": "<path to generated stub if applicable>"
}
```

---

## IV. Stub Artifact Schema

Generated stubs follow their category's schema but with:
- `editor_status`: `"pending"`
- Minimal placeholder values
- A `_gap_metadata` field (non-schema, for tracking only)

**Example Stub (authority_reference):**
```json
{
  "authority_id": "AUTH-AR-99-99-999",
  "authority_type": "statute",
  "citation": "[GAP STUB - citation needed]",
  "administering_body": "[GAP STUB - administering body needed]",
  "governs": ["[GAP STUB - governs entries needed]"],
  "effects": {
    "access_limiting": false,
    "appeal_mechanism": false
  },
  "editor_status": "pending",
  "_gap_metadata": {
    "generated_by": "gap_analyzer",
    "gap_type": "INCOMPLETE_CHAIN",
    "source_artifact": "MF-AR-EXAMPLE-2026",
    "detected_at": "2026-02-04T12:00:00Z"
  }
}
```

---

## V. Operational Use

1. Run `gap_analyzer.py` to discover gaps
2. Review gap records in `_gaps/` directory
3. Fill gaps by:
   - Researching and creating real artifacts, OR
   - Using Composite Schema Cycling (experimental), OR
   - Marking stubs as `nullified` if gap is invalid
4. Re-run analyzer to confirm closure

---

## VI. Version Control

- **Document:** Canonical Gap Definitions
- **Version:** v1
- **Status:** CANON — Active
- **Amendments:** Append-only; new gap types require new GAP-00X designations
