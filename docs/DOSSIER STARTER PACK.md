Great — YAML it is. Below is a **starter dossier pack** converted into **schema-valid YAML artifacts** for each of your four artifact types.

* The YAML keys match your schemas exactly (no extra properties), so these should validate cleanly against:

  * `authority_reference.schema.json`

  * `evidence_item.schema.json`

  * `field_validation.schema.json`

  * `money_flow.schema.json`

All items are marked `editor_status: pending` so you can “accept/correct/nullify” after review.

---

# **A) Authority References**

Put these under: `funding_intel/dossier/authority_reference/`

### **1\) DHS/OSAMH authority over SUD program standards**

`authority_id: AR-ACA-20-64-602-b19`  
`authority_type: statute`  
`citation: Ark. Code § 20-64-602(b)(19)`  
`administering_body: Arkansas Department of Human Services (DHS) — Office of Substance Abuse and Mental Health (OSAMH)`  
`governs:`  
  `- Accreditation/certification/licensing standards for alcohol and drug abuse prevention, treatment, and rehabilitation programs`  
`effects:`  
  `access_limiting: true`  
  `appeal_mechanism: false`  
`editor_status: pending`

### **2\) “Peer Support Specialist” qualification linkage to approved peer recovery certification**

`authority_id: AR-ACA-20-77-135-peer-support`  
`authority_type: statute`  
`citation: Ark. Code § 20-77-135(2)`  
`administering_body: Arkansas Department of Human Services (DHS) — Division of Medical Services (Medicaid) and Arkansas Alcohol and Drug Abuse Coordinating Council (approval role)`  
`governs:`  
  `- Peer support specialist qualification for Medicaid recognition tied to approved peer recovery certification`  
`effects:`  
  `access_limiting: true`  
  `appeal_mechanism: false`  
`editor_status: pending`

### **3\) Arkansas Peer Specialist Program (APSP) “Arkansas Model” credential ladder**

`authority_id: AR-POL-APSP-arkansas-model`  
`authority_type: policy`  
`citation: Arkansas Peer Specialist Program (APSP) — Arkansas Model credential ladder (PR/APR/PRPS) including core training, supervised hours, exam, and recovery duration requirements`  
`administering_body: DHS OSAMH Office of Recovery (oversight) with NAADAC/credentialing partner (implementation)`  
`governs:`  
  `- Peer Recovery Specialist credentialing requirements and tier progression rules`  
`effects:`  
  `access_limiting: true`  
  `appeal_mechanism: false`  
`editor_status: pending`

### **4\) APAC (Arkansas Peer Advisory Committee) governance**

`authority_id: AR-POL-APAC-governance`  
`authority_type: policy`  
`citation: DHS Office of Recovery — Arkansas Peer Advisory Committee (APAC) description (advisory body for peer recovery workforce matters)`  
`administering_body: DHS OSAMH Office of Recovery`  
`governs:`  
  `- Advisory influence over DHS peer recovery workforce practices and program guidance`  
`effects:`  
  `access_limiting: true`  
  `appeal_mechanism: false`  
`editor_status: pending`

### **5\) RCO designation criteria (AARCO / Arkansas Peer Services Model requirements)**

`authority_id: AR-POL-RCO-designation-AARCO`  
`authority_type: policy`  
`citation: AARCO RCO designation process requiring certified peer staffing and adherence to Arkansas Peer Services Model`  
`administering_body: DHS OSAMH Office of Recovery (via AARCO designation process)`  
`governs:`  
  `- Recovery Community Organization (RCO) designation eligibility criteria`  
`effects:`  
  `access_limiting: true`  
  `appeal_mechanism: false`  
`editor_status: pending`

### **6\) Specialty court program evaluation and approval authority**

`authority_id: AR-ACA-16-10-139-specialty-court`  
`authority_type: statute`  
`citation: Ark. Code § 16-10-139`  
`administering_body: Arkansas Supreme Court / Administrative Office of the Courts (AOC)`  
`governs:`  
  `- Specialty court program evaluation and approval standards via judicial oversight structures`  
`effects:`  
  `access_limiting: false`  
  `appeal_mechanism: false`  
`editor_status: pending`

### **7\) Mental health specialty court program administration authority**

`authority_id: AR-ACA-16-100-204-mental-health-court`  
`authority_type: statute`  
`citation: Ark. Code § 16-100-204`  
`administering_body: Arkansas judiciary (local mental health specialty courts) under AOC/Supreme Court oversight`  
`governs:`  
  `- Administration of mental health specialty court programs and program-design authority`  
`effects:`  
  `access_limiting: false`  
  `appeal_mechanism: false`  
`editor_status: pending`

### **8\) Federal RHTP statutory basis (as cited in your draft)**

`authority_id: FED-PL-119-21-71401-RHTP`  
`authority_type: statute`  
`citation: Pub. L. 119-21 § 71401 (2025) — Rural Health Transformation Program (RHTP)`  
`administering_body: Centers for Medicare & Medicaid Services (CMS) with state implementation via Arkansas Department of Health (ADH)`  
`governs:`  
  `- Rural Health Transformation Program funding authorization and state implementation constraints`  
`effects:`  
  `access_limiting: true`  
  `appeal_mechanism: false`  
`editor_status: pending`

### **9\) Arkansas RHTP implementation policy (state-level administration)**

`authority_id: AR-POL-RHTP-implementation-2026`  
`authority_type: policy`  
`citation: Arkansas RHTP implementation framework (FY2026) — HEART/PACT/RISE AR/THRIVE administered by Arkansas Department of Health (ADH)`  
`administering_body: Arkansas Department of Health (ADH)`  
`governs:`  
  `- RHTP subaward categories, application process, and oversight routing (state implementation)`  
`effects:`  
  `access_limiting: true`  
  `appeal_mechanism: false`  
`editor_status: pending`

---

# **B) Evidence Items**

Put these under: `funding_intel/dossier/evidence_item/`

### **1\) Evidence for Ark. Code § 20-64-602**

`evidence_id: EV-AR-ACA-20-64-602`  
`section: Authority Map — DHS/OSAMH Powers`  
`claim_summary: Ark. Code § 20-64-602(b)(19) authorizes DHS to develop and promulgate standards and rules for accrediting, certifying, and licensing alcohol and drug abuse prevention, treatment, and rehabilitation programs.`  
`evidence_type: statute`  
`source:`  
  `title: Arkansas Code § 20-64-602 (Powers and duties)`  
  `issuing_body: Arkansas General Assembly (as republished by Justia)`  
  `url: https://law.justia.com/codes/arkansas/title-20/subtitle-4/chapter-64/subchapter-6/section-20-64-602/`  
`confidence_level: medium`  
`editor_status: pending`

### **2\) Evidence for Ark. Code § 20-77-135**

`evidence_id: EV-AR-ACA-20-77-135`  
`section: Authority Map — Medicaid Peer Support Qualification`  
`claim_summary: Ark. Code § 20-77-135 ties peer support specialist qualification to certification in peer recovery from an accredited organization approved by the Arkansas Alcohol and Drug Abuse Coordinating Council.`  
`evidence_type: statute`  
`source:`  
  `title: Arkansas Code § 20-77-135 (Peer support specialist)`  
  `issuing_body: Arkansas General Assembly (as republished by Justia)`  
  `url: https://law.justia.com/codes/arkansas/title-20/subtitle-5/chapter-77/subchapter-1/section-20-77-135/`  
`confidence_level: medium`  
`editor_status: pending`

### **3\) Evidence describing APAC’s role (policy/governance description)**

`evidence_id: EV-DHS-APAC-DESCRIPTION`  
`section: Authority Map — APAC Governance`  
`claim_summary: DHS Office of Recovery describes APAC as advising DHS/OSAMH on peer recovery matters and strengthening the peer recovery workforce.`  
`evidence_type: administrative_rule`  
`source:`  
  `title: Arkansas Peer Recovery (APAC description)`  
  `issuing_body: Arkansas Department of Human Services (DHS)`  
  `url: https://humanservices.arkansas.gov/divisions-shared-services/shared-services/office-of-substance-abuse-and-mental-health/arkansas-peer-recovery/`  
`confidence_level: medium`  
`editor_status: pending`

### **4\) Evidence for APSP credential ladder description**

`evidence_id: EV-NAADAC-APSP-INTRO`  
`section: Authority Map — APSP Credentialing`  
`claim_summary: APSP is described as a three-tier credentialing process (PR/APR/PRPS) with training, education, experience, and supervision requirements.`  
`evidence_type: administrative_rule`  
`source:`  
  `title: Introducing the Arkansas Peer Specialist Program`  
  `issuing_body: NAADAC`  
  `url: https://www.naadac.org/assets/2416/aa&r_spring2021_introducing_the_arkansas_peer_specialist_program.pdf`  
`confidence_level: medium`  
`editor_status: pending`

### **5\) Evidence for RCO designation criteria via AARCO**

`evidence_id: EV-AARCO-RCO-DESIGNATION`  
`section: Authority Map — RCO Designation`  
`claim_summary: The RCO designation process describes benchmarks including certified peer staffing, paid supervision, and adherence to the Arkansas Peer Services Model.`  
`evidence_type: administrative_rule`  
`source:`  
  `title: Designation Process`  
  `issuing_body: Arkansas Alliance of Recovery-Centered Organizations (AARCO)`  
  `url: https://www.arrecovery.org/about-5`  
`confidence_level: medium`  
`editor_status: pending`

### **6\) Evidence for specialty court evaluation/approval statute**

`evidence_id: EV-AR-ACA-16-10-139`  
`section: Authority Map — Specialty Courts Oversight`  
`claim_summary: Ark. Code § 16-10-139 establishes specialty court program evaluation and approval structures under the Arkansas Supreme Court.`  
`evidence_type: statute`  
`source:`  
  `title: Arkansas Code § 16-10-139 (Specialty court program evaluation and approval)`  
  `issuing_body: Arkansas General Assembly (as republished by Justia)`  
  `url: https://law.justia.com/codes/arkansas/title-16/subtitle-2/chapter-10/subchapter-1/section-16-10-139/`  
`confidence_level: medium`  
`editor_status: pending`

### **7\) Evidence for mental health specialty court administration statute**

`evidence_id: EV-AR-ACA-16-100-204`  
`section: Authority Map — Mental Health Specialty Courts`  
`claim_summary: Ark. Code § 16-100-204 governs administration of mental health specialty court programs and permits development of manuals with assistance of relevant entities.`  
`evidence_type: statute`  
`source:`  
  `title: Arkansas Code § 16-100-204 (Administration of mental health specialty court program)`  
  `issuing_body: Arkansas General Assembly (as republished by Justia)`  
  `url: https://law.justia.com/codes/arkansas/title-16/subtitle-6/chapter-100/subchapter-2/section-16-100-204/`  
`confidence_level: medium`  
`editor_status: pending`

### **8\) Evidence item from your internal NAMI artifact about SAMHSA→DHS routing**

`evidence_id: EV-NAMI-ART1-SAMHSA-DHS`  
`section: Money Flow — DHS Capture Risk`  
`claim_summary: Internal note states SAMHSA dollars in Arkansas flow through DHS, creating policy gatekeeping and low downstream visibility; recommended to treat as contextual signal rather than an actionable pipeline.`  
`evidence_type: field_validation`  
`source:`  
  `title: Artifact 1 NAMI`  
  `issuing_body: NAMI (internal)`  
`confidence_level: medium`  
`editor_status: pending`

---

# **C) Field Validations**

Put these under: `funding_intel/dossier/field_validation/`

### **1\) DHS peer-recovery lane is “captured” (automatic jurisdiction trigger)**

`fv_id: FV-AR-DHS-PEER-CAPTURED-001`  
`jurisdiction: Arkansas`  
`validating_entity: STRATA / GLE Dossier Governance`  
`corroborator: Pending editor validation`  
`alignment_status: captured`  
`evidence_basis:`  
  `- authority_reference:AR-ACA-20-64-602-b19`  
  `- authority_reference:AR-ACA-20-77-135-peer-support`  
  `- authority_reference:AR-POL-APSP-arkansas-model`  
  `- authority_reference:AR-POL-RCO-designation-AARCO`  
  `- rule:DHS-approved peer recovery certification is an eligibility gate for Medicaid-recognized peer support specialist status in Arkansas.`  
`disclosure_level: restricted`  
`editor_status: pending`

### **2\) AOC specialty court lane is “open” for court-defined non-clinical support roles**

`fv_id: FV-AR-AOC-SPECIALTY-COURT-OPEN-001`  
`jurisdiction: Arkansas`  
`validating_entity: STRATA / GLE Dossier Governance`  
`corroborator: Administrative Office of the Courts (AOC) — pending corroboration`  
`alignment_status: open`  
`evidence_basis:`  
  `- authority_reference:AR-ACA-16-10-139-specialty-court`  
  `- authority_reference:AR-ACA-16-100-204-mental-health-court`  
  `- rule:Define support roles as court-adjacent navigation/education functions; avoid DHS-defined titles that imply Medicaid peer service billing.`  
`disclosure_level: restricted`  
`editor_status: pending`

### **3\) ADH-administered RHTP lane is “mixed” until each RFA confirms DHS-independence**

`fv_id: FV-AR-ADH-RHTP-MIXED-001`  
`jurisdiction: Arkansas`  
`validating_entity: STRATA / GLE Dossier Governance`  
`corroborator: Arkansas Department of Health (ADH) — pending corroboration`  
`alignment_status: mixed`  
`evidence_basis:`  
  `- authority_reference:FED-PL-119-21-71401-RHTP`  
  `- authority_reference:AR-POL-RHTP-implementation-2026`  
  `- rule:ADH-administered funding may be DHS-independent, but each category must be screened for dhs_controlled triggers in the RFA language.`  
`disclosure_level: restricted`  
`editor_status: pending`

---

# **D) Money Flows**

Put these under: `funding_intel/dossier/money_flow/`

### **1\) RHTP Year 1 (Arkansas share) — routing via ADH**

`flow_id: MF-AR-RHTP-Y1-2026`  
`source: CMS (Rural Health Transformation Program)`  
`intermediary: Arkansas Department of Health (ADH)`  
`destination: RHTP Year 1 subawards (HEART/PACT/RISE AR/THRIVE)`  
`amount: 208779396`  
`fund_type: federal`  
`fiscal_year: "2026"`  
`restrictions:`  
  `medicaid: false`  
  `dhs_controlled: false`  
`statutory_basis: Pub. L. 119-21 § 71401 (2025) — RHTP (as cited in Arkansas materials)`  
`editor_status: pending`

### **2\) PACT category (FY2026)**

`flow_id: MF-AR-RHTP-PACT-2026`  
`source: CMS (Rural Health Transformation Program)`  
`intermediary: Arkansas Department of Health (ADH)`  
`destination: PACT initiative subawards`  
`amount: 83400000`  
`fund_type: federal`  
`fiscal_year: "2026"`  
`restrictions:`  
  `medicaid: false`  
  `dhs_controlled: false`  
`statutory_basis: Arkansas RHTP implementation framework (PACT category, FY2026) — validate against final ADH RFA`  
`editor_status: pending`

### **3\) RISE AR category (FY2026)**

`flow_id: MF-AR-RHTP-RISEAR-2026`  
`source: CMS (Rural Health Transformation Program)`  
`intermediary: Arkansas Department of Health (ADH)`  
`destination: RISE AR initiative subawards`  
`amount: 33600000`  
`fund_type: federal`  
`fiscal_year: "2026"`  
`restrictions:`  
  `medicaid: false`  
  `dhs_controlled: false`  
`statutory_basis: Arkansas RHTP implementation framework (RISE AR category, FY2026) — validate against final ADH RFA`  
`editor_status: pending`

### **4\) HEART category (FY2026)**

`flow_id: MF-AR-RHTP-HEART-2026`  
`source: CMS (Rural Health Transformation Program)`  
`intermediary: Arkansas Department of Health (ADH)`  
`destination: HEART initiative subawards`  
`amount: 31200000`  
`fund_type: federal`  
`fiscal_year: "2026"`  
`restrictions:`  
  `medicaid: false`  
  `dhs_controlled: false`  
`statutory_basis: Arkansas RHTP implementation framework (HEART category, FY2026) — validate against final ADH RFA`  
`editor_status: pending`

### **5\) THRIVE category (FY2026)**

`flow_id: MF-AR-RHTP-THRIVE-2026`  
`source: CMS (Rural Health Transformation Program)`  
`intermediary: Arkansas Department of Health (ADH)`  
`destination: THRIVE initiative subawards`  
`amount: 60400000`  
`fund_type: federal`  
`fiscal_year: "2026"`  
`restrictions:`  
  `medicaid: false`  
  `dhs_controlled: false`  
`statutory_basis: Arkansas RHTP implementation framework (THRIVE category, FY2026) — validate against final ADH RFA`  
`editor_status: pending`

### **6\) DHS-controlled SAMHSA routing (routing-intel placeholder)**

`flow_id: MF-AR-SAMHSA-DHS-ROUTING-2026`  
`source: SAMHSA (formula/block grant dollars)`  
`intermediary: Arkansas Department of Human Services (DHS)`  
`destination: State behavioral health allocations (peer/recovery-related programming)`  
`amount: 0`  
`fund_type: federal`  
`fiscal_year: "2026"`  
`restrictions:`  
  `medicaid: false`  
  `dhs_controlled: true`  
`statutory_basis: Routing-intel placeholder; amount unknown. See EV-NAMI-ART1-SAMHSA-DHS for narrative basis.`  
`editor_status: pending`

### **7\) Medicaid peer-support reimbursement (routing-intel placeholder)**

`flow_id: MF-AR-MEDICAID-PEER-ROUTING-2026`  
`source: Medicaid (federal/state financing)`  
`intermediary: Arkansas DHS Division of Medical Services (Medicaid)`  
`destination: Peer support specialist reimbursement (requires approved peer recovery certification per Ark. Code § 20-77-135)`  
`amount: 0`  
`fund_type: federal`  
`fiscal_year: "2026"`  
`restrictions:`  
  `medicaid: true`  
  `dhs_controlled: true`  
`statutory_basis: Ark. Code § 20-77-135. Amount unknown; placeholder 0 used for routing classification only.`  
`editor_status: pending`

---

## **What you can do immediately with this pack**

1. Drop these into the correct `funding_intel/dossier/...` folders.

2. Your validator/indexer can now stop reporting “EMPTY” because you have **schema-compliant artifacts** (even if `pending`).

3. Editor review can promote each to `accepted` as sources are verified.

If you want, I can generate the **next batch** by expanding your map into:

* a dedicated authority\_reference for AODACC (if/when you provide its establishing authority)

* APAC “choke point” evidence items (minutes/charter/decision records) once you ingest them

* “actors & power structure” as *evidence items* (organizational charts, committee rosters) so they remain schema-valid without inventing new schema fields

