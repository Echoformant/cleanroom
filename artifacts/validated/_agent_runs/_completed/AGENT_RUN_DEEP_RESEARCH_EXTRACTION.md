# AGENT_RUN: Deep Research Artifact Extraction

## Mode: Extract Maximum Artifacts from Research Content

**Purpose:** When you have deep research results (web search, PDF analysis, database lookups), use this template to extract the maximum number of schema-compliant artifacts.

**Use Case:** ARORP, nonprofit 990 research, federal grant analysis, legislative session review

---

## YOUR TASK

You have been given research content about an organization, program, or topic. Your job is to extract EVERY POSSIBLE artifact that can be derived from this content.

**Do NOT simply summarize.** Create discrete, linkable artifacts in schema format.

---

## EXTRACTION MINDSET

For each piece of information, ask:

1. **Is this a legal authority?** → `authority_reference`
   - Statute citations
   - Regulations
   - Federal requirements
   - Bylaws, charters
   - Executive orders

2. **Is this money moving?** → `money_flow`
   - Grants received
   - Grants distributed
   - Contracts
   - Appropriations
   - Fees collected
   - Payments made

3. **Is this documentation?** → `evidence_item`
   - Budget documents
   - Annual reports
   - Audit findings
   - Policy statements
   - Meeting minutes
   - Federal award notices

4. **Is this a compliance/validation record?** → `field_validation`
   - Audit findings
   - Compliance reviews
   - Certification status
   - Accreditation records

---

## ARTIFACT SCHEMAS

### authority_reference

```json
{
  "authority_id": "AUTH-{JURISDICTION}-{TYPE}-{IDENTIFIER}",
  "authority_type": "statute" | "regulation" | "act" | "policy" | "bylaw" | "federal_requirement",
  "citation": "Full legal citation or document reference",
  "administering_body": "Agency or organization name",
  "governs": ["programs", "flow_ids", "other authorities"],
  "effects": {
    "access_limiting": true/false,
    "appeal_mechanism": true/false
  },
  "editor_status": "pending"
}
```

**ID Pattern Examples:**

- `AUTH-AR-ACA-20-77-107` — Arkansas Code Annotated
- `AUTH-US-42-CFR-438` — Federal regulation
- `AUTH-AR-ARORP-BYLAWS-2024` — Organization bylaws
- `AUTH-US-SAMHSA-MHBG-REQUIREMENTS` — Federal grant requirements

### money_flow

```json
{
  "flow_id": "MF-{JURISDICTION}-{PROGRAM/SOURCE}-{DESCRIPTION}-{FY}",
  "source": "Entity providing funds",
  "intermediary": "None" or "Pass-through organization",
  "destination": "Entity receiving funds",
  "amount": integer in USD (0 if unknown),
  "fund_type": "state" | "federal" | "private" | "settlement" | "fee",
  "fiscal_year": "2026" or "2025-2026",
  "restrictions": {
    "medicaid": true/false,
    "dhs_controlled": true/false
  },
  "statutory_basis": "Legal authority for this flow",
  "editor_status": "pending"
}
```

**ID Pattern Examples:**

- `MF-AR-ARORP-SAMHSA-MHBG-SUBGRANT-FY2026` — Federal grant to org
- `MF-AR-ARORP-MEMBERSHIP-DUES-FY2026` — Fee revenue
- `MF-AR-ARORP-TO-LOCALPROVIDER-TRAINING-FY2026` — Pass-through

### evidence_item

```json
{
  "evidence_id": "EVID-{JURISDICTION}-{SOURCE}-{DESCRIPTION}",
  "section": "artifact_id this evidence supports",
  "claim_summary": "What this evidence proves with specifics",
  "evidence_type": "budget" | "audit" | "policy" | "federal_award" | "form-990" | "annual_report",
  "source": {
    "title": "Document title",
    "issuing_body": "Who issued it",
    "url": "URL if available"
  },
  "confidence_level": "high" | "medium" | "low",
  "editor_status": "pending"
}
```

**ID Pattern Examples:**

- `EVID-AR-ARORP-990-GRANTSRECEIVED-2023` — 990 extract
- `EVID-AR-ARORP-ANNUALREPORT-2024` — Annual report
- `EVID-AR-ARORP-DHS-CONTRACT-2025` — Contract evidence

### field_validation

```json
{
  "fv_id": "FV-{JURISDICTION}-{ENTITY}-{FINDING}-{YEAR}",
  "jurisdiction": "Arkansas" or "Federal",
  "validating_entity": "Who did the validation",
  "alignment_status": "captured" | "open" | "mixed",
  "evidence_basis": ["evidence_ids", "authority_ids"],
  "disclosure_level": "public" | "restricted",
  "editor_status": "pending"
}
```

---

## ORGANIZATION-SPECIFIC EXTRACTION GUIDE

When researching an organization (like ARORP), extract:

### From 990 Forms

- Total revenue → note in evidence
- Government grants received → `money_flow` (source: federal/state agency, dest: org)
- Program service revenue → `money_flow` (source: payers, dest: org)
- Grants paid out → `money_flow` (source: org, dest: recipients)
- Officer compensation → note in evidence
- Program accomplishments → `evidence_item`

### From Websites/About Pages

- Mission statement → `evidence_item`
- Board of directors → `authority_reference` (governance structure)
- Programs offered → `evidence_item` per program
- Partner organizations → potential linked artifacts

### From State Databases

- State contracts → `money_flow`
- Grants received → `money_flow`
- Compliance records → `field_validation`

### From Federal Sources

- Federal grant awards → `money_flow` + `evidence_item`
- Grant requirements → `authority_reference`
- Compliance reviews → `field_validation`

---

## CROSS-REFERENCING

Link artifacts to each other:

- `money_flow.statutory_basis` → references `authority_reference`
- `evidence_item.section` → points to artifact it supports
- `field_validation.evidence_basis` → lists supporting evidence/authority
- `authority_reference.governs` → lists flows/programs it controls

---

## OUTPUT FORMAT

Return a single JSON object with ALL extracted artifacts:

```json
{
  "batch_id": "BATCH-{SUBJECT}-EXTRACTION-{DATE}",
  "mode": "deep-research-extraction",
  "subject": "ARORP" or "Organization Name",
  "generated_at": "2026-02-XX",
  "source_summary": "Brief description of research sources used",
  "total_artifacts": 0,
  "artifacts": {
    "money_flow": [],
    "authority_reference": [],
    "evidence_item": [],
    "field_validation": []
  },
  "extraction_notes": "What was found, what gaps remain"
}
```

---

## EXTRACTION CHECKLIST

Before submitting:

- [ ] Every grant mentioned → money_flow
- [ ] Every statute/regulation cited → authority_reference  
- [ ] Every document referenced → evidence_item
- [ ] Every audit/compliance finding → field_validation
- [ ] All amounts are integers (no decimals, no commas)
- [ ] All intermediary fields present (use "None" if direct)
- [ ] All restrictions objects present on money_flows
- [ ] All editor_status = "pending"
- [ ] Cross-references populated where possible

---

## ARORP-SPECIFIC SEEDS

If researching Arkansas Recovery Organizations and Providers (ARORP), look for:

**Authorities:**

- State behavioral health statutes (ACA 20-47, 20-64)
- DHS OBHS certification requirements
- SAMHSA MHBG/SABG requirements
- Peer support specialist certification rules

**Money Flows:**

- SAMHSA block grant pass-throughs
- DHS OBHS contracts
- State appropriations for peer services
- Training program fees
- Membership dues

**Evidence:**

- 990 tax returns (if nonprofit)
- Annual reports
- DHS contract documents
- SAMHSA grant award notices
- Board meeting minutes

**Validations:**

- Legislative audit findings
- DHS compliance reviews
- Federal OIG audits
- Certification status records

---

## BEGIN

Extract every possible artifact from the provided research content. Create maximum coverage with proper schema compliance.
