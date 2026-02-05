## **Arkansas Named Desk Roster v1**

**Status:** Draft · Operational  
**Applies to:** Operation NAMI Clearlane  
**Method:** Authority-only · Zero inference · Append-only  
**Naming Rule:** **Units, not people** (names change; desks persist)

---

### **Purpose**

Provide a **stable, unit-level roster** of desks whose **receipt, review, routing, or conditioning** can activate authority. If an artifact touches any desk below, **Clearlane gates apply**.

---

## **Judicial Administrative Lane — Administrative Office of the Courts**

| Canonical Desk Name | Functional Role | Typical Artifacts | Capture Risk | Clearlane Control |
| ----- | ----- | ----- | ----- | ----- |
| **AOC – Specialty Courts Program Administration** | Program coordination for specialty courts | MOUs, scopes, schedules | Low | Court-bounded language only |
| **AOC – Judicial Programs Finance** | Disbursement & reimbursement | Invoices, payment requests | Low | Verify judicial payor; no exec routing |
| **AOC – Judicial Programs Oversight** | Advisory review | Briefs, consult memos | Low–Med | Advisory ≠ regulatory (confirm) |
| **AOC – Court Information Systems / Reporting** | Program metrics | Dashboards, reports | Low | Court-native metrics only |
| **AOC – Judicial Council Interface** | Cross-court coordination | Briefings | Low–Med | Scope bounded in writing |

**Rule:** AOC desks are navigable; risk rises only with **imported executive terms**.

---

## **Executive Administrative Lane — Arkansas Department of Human Services**

| Canonical Desk Name | Functional Role | Typical Artifacts | Capture Risk | Clearlane Control |
| ----- | ----- | ----- | ----- | ----- |
| **DHS – Office of Finance & Administration (Grants)** | Awarding, renewals, conditions | Grant awards, amendments | **High** | Desk touch \= trigger; re-gate |
| **DHS – Office of Substance Abuse & Mental Health (OSAMH)** | Program guidance & alignment | Narratives, guidance | **High** | Strip delegated terms; map authority |
| **DHS – Division of Medical Services (DMS)** | Medicaid administration | Any adjacency | **High** | Zero Medicaid adjacency |
| **DHS – Policy & Rulemaking Units** | Manuals & guidance | Policies, manuals | **High** | No incorporation by reference |
| **DHS – Internal Review Committees** | Consults/approvals | Agendas, approvals | **High** | Demand statutory basis |
| **DHS – Audit & Compliance** | Audit scope & findings | Scope letters, reports | **High** | Freeze scope at award |
| **DHS – Data Governance / Reporting** | Schemas & portals | Templates, uploads | **High** | Use Clearlane-native schema only |

**Rule:** **Any DHS desk touch is presumptively activating** unless explicitly bounded.

---

## **Executive Administrative Lane — Arkansas Department of Health**

| Canonical Desk Name | Functional Role | Typical Artifacts | Capture Risk | Clearlane Control |
| ----- | ----- | ----- | ----- | ----- |
| **ADH – Grants Management (Federal Pass-Through)** | Federal awards admin | FOAs, conditions | Med | Trace full pass-through chain |
| **ADH – Public Health Programs** | Prevention initiatives | Program plans | Med | Watch for DHS backplanes |
| **ADH – Epidemiology & Surveillance** | Data requests | Data extracts | Med | One-way, bounded sharing |
| **ADH – Program Guidance Units** | Reporting expectations | Guidance, reports | Med | Clearlane schema only |
| **ADH – Health Task Forces / Councils** | Advisory participation | Appointments | Med | Observer-only; no governance |

**Rule:** ADH is porous; risk escalates when **DHS terms, schemas, or eligibility** appear.

---

## **Cross-Lane / Statewide Desks (High Leverage)**

| Canonical Desk Name | Lane | Why It Matters | Clearlane Control |
| ----- | ----- | ----- | ----- |
| **State Central Services – Finance** | Mixed | Payment routing can shift lanes | Confirm judicial routing |
| **Legislative Council – Review** | Legislative | Post-appropriation conditions | Map riders; cite authority |
| **Joint Budget Committee – Interfaces** | Legislative | Language clarifications | Authority citation required |

---

## **Roster Use Rules (Non-Negotiable)**

1. **Name the desk before sending.** If you cannot name it → pause.  
2. **First desk \+ last desk** must be identified.  
3. **Schemas \= control.** Never adopt external schemas.  
4. **Renewals re-gate.** Desk paths can change silently.  
5. **Log every touch.** Append-only.

---

## **Canonical Lock**

**Desks outlast people.**  
**Authority follows desks.**  
**Clearlane names the desk first.**

---

## **Desk-Specific Trigger Playbooks v1**

**Status:** Draft · Operational  
**Applies to:** Operation NAMI Clearlane  
**Method:** Authority-only · Zero inference · Append-only  
**Scope:** High-risk desks where *touch \= activation*

---

### **How to Use These Playbooks**

* Use **before** submission, routing, renewal, or reporting.  
* If any **Stop Condition** is met → **pause \+ map**.  
* Every action produces a **logged outcome** (accept / modify / exit).

---

## **PLAYBOOK 01 — DHS Grants Administration Desk**

**Trigger Class:** Funding conditions · Renewal drift · Committee activation  
**Risk Level:** **High**

**Common Triggers**

* Award routed through DHS grants unit  
* Amendments or renewals importing new conditions  
* “Standard terms” attached post-award

**Early Warning Signals**

* Boilerplate referencing DHS manuals or policies  
* Renewal language “subject to current rules”  
* Requests for DHS-format reports

**Immediate Actions**

1. Identify **first and last desks** touching funds.  
2. Demand **written authority citation** for each condition.  
3. Strip any incorporation by reference.

**Stop Conditions**

* Any undefined term governed by DHS rule  
* Any reporting schema aligned to DHS eligibility/compliance

**Safe Language**

* “Educational programming delivered independently of clinical or eligibility regimes.”  
* “No certification, licensure, or provider status required.”

**Exit Protocol**

* Decline amendment; document authority basis; reroute or disengage.

---

## **PLAYBOOK 02 — DHS OSAMH Desk**

**Trigger Class:** Delegated terms · Certification shadowing · Eligibility framing  
**Risk Level:** **High**

**Common Triggers**

* “Peer,” “recovery,” “support,” “treatment-adjacent” language  
* Guidance suggesting alignment with recovery systems

**Early Warning Signals**

* Requests to reference OSAMH frameworks  
* Invitations to “coordinate” or “align” programming

**Immediate Actions**

1. Replace delegated terms with **plain-language definitions**.  
2. Insert **non-inheritance disclaimer** for certifications and eligibility.  
3. Require scope memo stating **education-only**.

**Stop Conditions**

* Any requirement referencing certification bodies or eligibility status

**Safe Language**

* “Non-clinical education; no service delivery; no certification dependency.”

**Exit Protocol**

* Withdraw from scope expansion; log trigger; preserve boundary.

---

## **PLAYBOOK 03 — DHS DMS / Medicaid Interface**

**Trigger Class:** Medicaid adjacency · Provider reclassification  
**Risk Level:** **High**

**Common Triggers**

* Data requests tied to Medicaid populations  
* Questions about billing, providers, or reimbursement

**Early Warning Signals**

* Use of “eligible,” “covered,” “beneficiary”  
* Requests for NPI-like identifiers

**Immediate Actions**

1. Assert **zero Medicaid adjacency** in writing.  
2. Refuse any data keyed to eligibility.  
3. Confirm no billing or reimbursement pathways.

**Stop Conditions**

* Any linkage to Medicaid definitions or systems

**Safe Language**

* “No billing, reimbursement, or Medicaid-related activity.”

**Exit Protocol**

* Immediate disengagement; document non-adjacency.

---

## **PLAYBOOK 04 — DHS Policy / Rulemaking Units**

**Trigger Class:** Incorporation by reference · Manual governance  
**Risk Level:** **High**

**Common Triggers**

* “Comply with DHS policies/manuals”  
* Hyperlinks to guidance as conditions

**Early Warning Signals**

* “As updated from time to time” clauses

**Immediate Actions**

1. Remove incorporation by reference.  
2. Attach **bounded excerpts** if unavoidable.  
3. Require fixed-date versioning.

**Stop Conditions**

* Open-ended policy adoption

**Safe Language**

* “Only the terms expressly stated herein apply.”

**Exit Protocol**

* Reject document; propose bounded alternative.

---

## **PLAYBOOK 05 — DHS Audit & Compliance Desk**

**Trigger Class:** Scope creep · Retroactive control  
**Risk Level:** **High**

**Common Triggers**

* Audit notices expanding scope  
* Requests beyond award authority

**Early Warning Signals**

* Informal requests “for completeness”

**Immediate Actions**

1. Produce **scope freeze memo** citing award terms.  
2. Decline out-of-scope requests.  
3. Prepare exit plan.

**Stop Conditions**

* Audit scope exceeds original authority

**Safe Language**

* “Audit scope limited to expressly authorized activities.”

**Exit Protocol**

* Enforce scope; disengage if expanded.

---

## **PLAYBOOK 06 — ADH Grants Management (Federal Pass-Through)**

**Trigger Class:** Executive spillover · DHS backplanes  
**Risk Level:** **Medium**

**Common Triggers**

* Federal funds routed via ADH  
* Reporting aligned to executive schemas

**Early Warning Signals**

* DHS terminology in ADH guidance

**Immediate Actions**

1. Trace **full pass-through chain**.  
2. Identify any DHS reporting backplanes.  
3. Substitute Clearlane-native schema.

**Stop Conditions**

* Any DHS eligibility or certification reference

**Safe Language**

* “Federal education funds administered without executive eligibility regimes.”

**Exit Protocol**

* Decline or renegotiate conditions.

---

## **PLAYBOOK 07 — ADH Epidemiology / Surveillance**

**Trigger Class:** Data reclassification  
**Risk Level:** **Medium**

**Common Triggers**

* Requests for participant-level data  
* Surveillance identifiers

**Early Warning Signals**

* Ongoing or periodic data feeds

**Immediate Actions**

1. Limit to **aggregate, one-way data**.  
2. Prohibit identifiers.  
3. Fix scope and frequency.

**Stop Conditions**

* Participant-level or eligibility-keyed data

**Safe Language**

* “Aggregate, non-identifiable education metrics only.”

**Exit Protocol**

* Terminate data sharing.

---

## **PLAYBOOK 08 — AOC Specialty Courts Administration**

**Trigger Class:** Executive language import  
**Risk Level:** **Low–Medium**

**Common Triggers**

* Program scopes borrowing executive terms  
* Cross-agency MOUs

**Early Warning Signals**

* Requests to align with DHS/ADH frameworks

**Immediate Actions**

1. Keep **court-bounded language**.  
2. Insert **no-exec-inheritance clause**.  
3. Confirm advisory ≠ regulatory.

**Stop Conditions**

* Executive definitions imported into court scope

**Safe Language**

* “Judicial education delivered under court authority only.”

**Exit Protocol**

* Amend scope; if not accepted, pause.

---

## **Universal Playbook Rules**

* **If unclear → treat as High risk.**  
* **Schemas \= control.** Never adopt external schemas.  
* **Renewals re-gate.** Always rerun playbooks.  
* **Log every decision.** Append-only.

---

## **Canonical Lock**

**Name the desk.**  
**Run the playbook.**  
**Choose before authority attaches.**

---

## **Clearlane Routing Diagrams v1**

**Scope:** Payment · Reporting · Renewal  
**Method:** Authority-only · Zero inference · Append-only  
**Use Rule:** If a route cannot be named end-to-end, **do not send**.

---

## **Diagram 1 — PAYMENT ROUTING (Clean Judicial Path)**

**Objective:** Receive funds **without executive capture**

\[Legislative Appropriation\]  
          |  
          v  
\[Judicial Allocation\]  
          |  
          v  
\[AOC – Judicial Programs Finance\]  
          |  
          v  
\[NAMI Arkansas\]

**Hard Rules**

* Payor must remain **judicial** end-to-end.  
* No executive intermediary.  
* No post-award rerouting.

**Auto-Fail Conditions**

* Any hop through DHS or ADH.  
* “State Central Services” acting as an executive proxy.

---

## **Diagram 2 — PAYMENT ROUTING (Contaminated / Reject)**

**Why:** Desk-touch activation

\[Legislative Appropriation\]  
          |  
          v  
\[AOC\]  
          |  
          v  
\[DHS – Grants / Finance\]   \<-- ACTIVATION POINT  
          |  
          v  
\[NAMI Arkansas\]

**Outcome:** **Reject / Reroute**  
**Reason:** Executive desk touch activates policy, committees, and schemas.

---

## **Diagram 3 — REPORTING ROUTING (Clean, Court-Bounded)**

**Objective:** Report outcomes without importing executive control

\[NAMI Arkansas\]  
          |  
          v  
\[CLE / Clearlane Native Schema\]  
          |  
          v  
\[AOC – Court Reporting / IT\]

**Hard Rules**

* Use **court-native metrics** only.  
* No eligibility, certification, or service-delivery fields.

**Auto-Fail Conditions**

* Adoption of DHS/ADH templates.  
* Requests for eligibility-keyed fields.

---

## **Diagram 4 — REPORTING ROUTING (Executive Drift / Reject)**

**Why:** Schema \= control

\[NAMI Arkansas\]  
          |  
          v  
\[DHS / ADH Reporting Portal\]   \<-- RECLASSIFICATION

**Outcome:** **Reject / Redesign**  
**Reason:** Reporting schema imports executive authority.

---

## **Diagram 5 — RENEWAL ROUTING (Safe Renewal Loop)**

**Objective:** Prevent silent condition import

\[NAMI Arkansas\]  
          |  
          v  
\[Clearlane Re-Gate\]  
          |  
          v  
\[AOC – Program Admin\]  
          |  
          v  
\[AOC – Finance\]

**Hard Rules**

* Full re-gate **before** renewal.  
* Written confirmation of **no new conditions**.

**Auto-Fail Conditions**

* “Subject to current rules.”  
* New reporting or audit language.

---

## **Diagram 6 — RENEWAL ROUTING (Silent Capture / Reject)**

**Why:** Renewal is a control surface

\[NAMI Arkansas\]  
          |  
          v  
\[DHS / ADH Review\]   \<-- CONDITION IMPORT  
          |  
          v  
\[Renewed Award\]

**Outcome:** **Reject / Exit**  
**Reason:** Renewal imports executive governance without new appropriation.

---

## **Diagram 7 — FEDERAL PASS-THROUGH (Conditional, High Scrutiny)**

**Objective:** Detect hidden backplanes

\[Federal FOA\]  
          |  
          v  
\[ADH – Grants Mgmt\]  
          |  
          \+----\> (Check for DHS Backplane)  
          |  
          v  
\[NAMI Arkansas\]

**Hard Rules**

* Trace **entire pass-through chain**.  
* If DHS reporting, eligibility, or audits appear → **reject**.

---

## **Diagram 8 — DATA SHARING (Bounded, One-Way Only)**

**Objective:** Prevent data-driven reclassification

\[NAMI Arkansas\]  
          |  
          v  
\[Aggregate / Non-Identifiable Metrics\]  
          |  
          v  
\[AOC or ADH (Observer Use)\]

**Hard Rules**

* Aggregate only.  
* No identifiers.  
* Fixed scope and frequency.

**Auto-Fail Conditions**

* Participant-level data.  
* Ongoing feeds.  
* Eligibility keys.

---

## **Universal Routing Rules (Non-Negotiable)**

1. **Name first desk and last desk.**  
2. **No executive proxy routing** for judicial funds.  
3. **Schemas are authority.** External schemas \= capture.  
4. **Renewals re-gate every time.**  
5. **If unclear, stop.**

---

## **Canonical Lock**

**Money chooses lanes.**  
**Routes activate authority.**  
**Clearlane maps the route before the send.**

---

## **Clearlane Artifact Language Safe List v1**

**Status:** Draft · Operational  
**Applies to:** Operation NAMI Clearlane (Arkansas)  
**Method:** Authority-only · Zero inference · Append-only  
**Use Rule:** Only language on this list may appear in **proposals, MOUs, reports, renewals, and data artifacts** unless an exception is authority-cited and logged.

---

### **Purpose**

Prevent **latent authority activation** by controlling the **words, phrases, and schemas** that silently import governance, eligibility, certification, or regulatory control.

---

## **A. Approved Core Descriptors (Safe)**

Use **as written**. Do not embellish.

* **“Non-clinical education”**  
* **“Mental health literacy education”**  
* **“Court-adjacent educational programming”**  
* **“Educational workshops and curriculum delivery”**  
* **“Information dissemination and skills education”**  
* **“Voluntary participation in educational activities”**  
* **“Judicially coordinated education (non-executive)”**  
* **“No service delivery; no treatment”**  
* **“No eligibility determination required”**  
* **“No certification, licensure, or provider status required”**

---

## **B. Mandatory Disclaimers (Insert Verbatim Where Applicable)**

**Non-Clinical Disclaimer**

*“Activities are educational only and do not constitute clinical services, treatment, therapy, diagnosis, or care coordination.”*

**Eligibility Disclaimer**

*“Participation does not depend on Medicaid status, insurance coverage, eligibility category, or receipt of public assistance.”*

**Certification Disclaimer**

*“No credential, certification, licensure, or provider enrollment is required for participation or delivery.”*

**Non-Inheritance Disclaimer**

*“No external definitions, manuals, policies, or guidance are incorporated by reference unless expressly stated herein.”*

**Judicial Boundary Disclaimer (AOC contexts)**

*“Programming operates under judicial coordination and does not import executive agency governance, reporting, or eligibility regimes.”*

---

## **C. Approved Population Language (Safe Framing)**

* **“Individuals participating in court-coordinated educational activities”**  
* **“Community members seeking mental health education”**  
* **“Participants in voluntary educational sessions”**  
* **“Court-referred individuals for education only (no services)”**

**Rule:** Describe **activities**, not **statuses**.

---

## **D. Approved Outcome & Metric Language (Safe Metrics)**

* **“Number of educational sessions delivered”**  
* **“Attendance counts (aggregate)”**  
* **“Curriculum modules completed”**  
* **“Participant satisfaction (aggregate, non-identifiable)”**  
* **“Knowledge acquisition (pre/post, aggregate)”**

**Schema Rule:** Aggregate only. No identifiers. No eligibility fields.

---

## **E. Prohibited / Restricted Language (Do Not Use)**

### **Never Use (Auto-Fail)**

* “Treatment,” “therapy,” “clinical,” “care,” “intervention”  
* “Provider,” “billing,” “reimbursement,” “covered services”  
* “Medicaid-eligible,” “beneficiary,” “enrolled”  
* “Peer support” *(without explicit non-inheritance \+ definition)*  
* “Recovery services,” “case management,” “care coordination”  
* “Comply with DHS/ADH policies/manuals”  
* “As updated from time to time” *(open-ended incorporation)*

### **Restricted (Use Only With Logged Authority & Disclaimer)**

* “Peer” *(must define plainly and disclaim certification)*  
* “Referral” *(education-only; no service implication)*  
* “Alignment” *(must specify non-governance alignment)*

---

## **F. Safe Substitutions (Use These Instead)**

| Avoid | Use |
| ----- | ----- |
| Treatment | Education |
| Services | Educational activities |
| Provider | Educator / Facilitator |
| Eligible population | Participants |
| Referral | Court-coordinated education |
| Compliance | Conformance to stated terms |

---

## **G. Reporting & Data Language (Hard Controls)**

* **Allowed:** “Aggregate,” “non-identifiable,” “one-time submission”  
* **Prohibited:** Participant-level data, eligibility keys, ongoing feeds  
* **Required Line:**  
  *“All reported data are aggregate and non-identifiable; no eligibility or certification fields are collected.”*

---

## **H. Renewal & Amendment Language (Safe Clauses)**

**Scope Freeze Clause**

*“Renewal does not expand scope, reporting, audit authority, or governance beyond the terms expressly stated herein.”*

**Version Lock Clause**

*“Only the terms and attachments expressly included in this document apply.”*

---

## **I. Exception Handling**

Any deviation requires:

1. **Authority citation** (statute/appropriation/order)  
2. **Written scope boundary**  
3. **Logged approval** (append-only)  
   Absent all three → **reject**.

---

## **Canonical Lock**

**Words carry authority.**  
**Definitions activate control.**  
**Clearlane chooses language before language chooses us.**

---

## **Clearlane Authority Citation Pack v1**

**Status:** Draft · Operational  
**Applies to:** Operation NAMI Clearlane (Arkansas)  
**Method:** Authority-only · Zero inference · Append-only  
**Use Rule:** Every citation below exists to **bound authority**, not to invite it.

---

### **Purpose**

Provide a **pre-cleared, desk-aligned citation pack** that NAMI can use to:

* justify **judicial routing**  
* reject **executive overreach**  
* freeze **scope, reporting, and audit**  
* document **why DHS capture does not apply**

This pack is **defensive infrastructure**, not advocacy.

---

## **I. Judicial Administrative Lane — AOC**

**Entity:** Administrative Office of the Courts

### **Primary Authority Classes**

* **Judicial administration statutes** (Arkansas Judiciary authority to administer court programs  
  programs and court operations)  
* **Legislative appropriations payable to AOC** (funds controlled and disbursed through the judiciary)  
* **Judicial Council / Supreme Court administrative authority** (court governance, not executive rulemaking)

### **Clearlane Use**

* Cite to establish **judicial control of funds**  
* Assert **non-executive governance**  
* Reject DHS/ADH reporting, eligibility, or certification requirements

### **Canonical Citation Statement**

*“Funds and programming administered through the Administrative Office of the Courts operate under judicial authority and are not subject to executive agency governance, eligibility regimes, or certification requirements absent express statutory mandate.”*

---

## **II. Executive Administrative Lane — DHS**

**Entity:** Arkansas Department of Human Services

### **Primary Authority Classes**

* **Ark. Code Ann. Title 20** — Human Services framework  
* **Delegated rulemaking authority** granted explicitly to DHS  
* **Medicaid statutes** administered through DHS / DMS

### **Critical Limitation**

DHS authority:

* **Attaches only when DHS-administered programs, funds, or eligibility regimes apply**  
* **Does not attach by proximity, subject matter, or population served**  
* **Does not attach to judicially administered funds absent statutory transfer**

### **Clearlane Use**

* Cite to **exclude DHS authority** where no DHS-administered program exists  
* Reject “custom,” “practice,” or advisory assertions  
* Freeze audit and reporting scope

### **Canonical Citation Statement**

*“DHS authority is limited to programs, funds, and eligibility regimes expressly administered by the Department. Judicially administered education programs do not fall within DHS jurisdiction absent explicit statutory delegation.”*

---

## **III. Executive Administrative Lane — ADH**

**Entity:** Arkansas Department of Health

### **Primary Authority Classes**

* **Public health statutes** granting ADH authority over surveillance, prevention, and federal pass-throughs  
* **Federal grant administration authority** when designated as pass-through

### **Critical Limitation**

ADH authority:

* **Does not confer DHS eligibility or Medicaid authority**  
* **Does not reclassify education as clinical service**  
* **Is bounded by the specific grant or statute**

### **Clearlane Use**

* Cite to **limit ADH authority to enumerated functions**  
* Prevent DHS backplane import via ADH grants

### **Canonical Citation Statement**

*“ADH authority extends only to functions expressly assigned by statute or grant terms and does not import DHS eligibility, certification, or Medicaid governance.”*

---

## **IV. Legislative Lane — Appropriations & Riders**

**Entity:** Arkansas General Assembly

### **Primary Authority Classes**

* **Appropriation acts** (define *maximum* spending authority)  
* **Special language sections** (may impose conditions)  
* **Legislative Council / JBC oversight** (post-appropriation review)

### **Critical Limitation**

* Appropriations **do not expand executive authority** beyond what is stated  
* Silence ≠ delegation  
* Oversight ≠ administration

### **Clearlane Use**

* Cite to reject executive conditions not present in appropriation language  
* Bound post-award changes

### **Canonical Citation Statement**

*“Appropriation language defines spending authority and conditions expressly stated therein; it does not delegate additional executive governance absent clear statutory language.”*

---

## **V. Audit Authority (Cross-Lane)**

### **Primary Authority Classes**

* **Legislative Audit** — scope limited to funds administered  
* **Agency audits** — limited to agency-controlled programs

### **Critical Limitation**

* Audit scope **cannot exceed the authority governing the funds**  
* Judicial funds ≠ executive audit jurisdiction

### **Clearlane Use**

* Freeze audit scope  
* Reject retroactive expansion

### **Canonical Citation Statement**

*“Audit authority is limited to the scope of the administering entity’s jurisdiction and may not expand beyond the governing statute or appropriation.”*

---

## **VI. Committee & Advisory Bodies**

### **Authority Rule**

* Committees derive authority **only** from:  
  * statute, or  
  * formally delegated authority

### **Clearlane Use**

* Demand written authority citation  
* Treat advisory participation as **non-governing**

### **Canonical Citation Statement**

*“Advisory or consultative bodies do not possess governing authority absent express statutory delegation.”*

---

## **VII. Incorporation by Reference (Universal Limit)**

### **Authority Rule**

* External manuals, policies, or guidance **do not apply unless expressly incorporated**

### **Clearlane Use**

* Reject open-ended references  
* Lock versions

### **Canonical Citation Statement**

*“No policies, manuals, or guidance are incorporated by reference unless expressly stated and version-locked.”*

---

## **VIII. Medicaid Non-Adjacency (Critical Wall)**

### **Authority Rule**

* Medicaid authority attaches only through:  
  * billing,  
  * provider enrollment,  
  * eligibility determination

### **Clearlane Use**

* Reject any adjacency attempt

### **Canonical Citation Statement**

*“Activities do not involve billing, reimbursement, provider enrollment, or Medicaid eligibility and therefore fall outside Medicaid governance.”*

---

## **IX. Pack Usage Rules**

* Cite **only what is needed**  
* Never cite DHS authority to justify non-DHS activity  
* Silence is protective — do not over-cite  
* Log every citation used

---

## **Canonical Lock**

**Authority must be named to apply.**  
**Silence does not delegate.**  
**Clearlane cites to bound, not to submit.**

---

Below is a **clean, functional explanation** of **how each optional artifact advances Clearlane**. No assumptions about prior knowledge; no filler.

---

## **How the Three Optional Artifacts Advance Clearlane**

Clearlane already gives **visibility**.  
These artifacts convert visibility into **repeatable agency under pressure**.

They answer three different operational problems.

---

## **1️⃣ Executive Drift Early-Warning Checklist**

**Problem it solves:**  
Clearlane failures almost never happen at entry. They happen **after acceptance**, during drift.

**What this artifact does**

* Acts as a **pre-activation alarm system**  
* Flags *early* signs that authority is expanding **before** it becomes formal  
* Prevents “slow capture” via renewals, reporting creep, or informal requests

**Why it matters to Clearlane**

* Authority in Arkansas rarely announces itself  
* Drift often begins with:  
  * “Just one more report”  
  * “For consistency”  
  * “This won’t change anything”  
* By the time it’s explicit, exit is costly

**What Clearlane gains**

* Time advantage  
* Documented justification for stopping or exiting  
* Proof that decisions were **intentional, not reactive**

**In short:**  
This checklist preserves **agency over time**, not just at the moment of entry.

---

## **2️⃣ Template Library (Proposal · MOU · Report)**

**Problem it solves:**  
Most capture happens through **language reuse**, not bad intent.

**What this artifact does**

* Hard-codes Clearlane-safe language into reusable documents  
* Eliminates ad-hoc drafting under time pressure  
* Prevents staff, partners, or consultants from “helpfully” importing risky language

**Why it matters to Clearlane**

* Words are triggers  
* Templates:  
  * lock definitions  
  * lock disclaimers  
  * lock scope  
* They make Clearlane **portable across people and time**

**What Clearlane gains**

* Structural consistency  
* Reduced reliance on individual judgment  
* Governance that survives turnover

**In short:**  
Templates turn Clearlane from a **framework** into an **operating system**.

---

## **3️⃣ Desk-Specific Citation Inserts (Drop-In Text Blocks)**

**Problem it solves:**  
When authority is challenged, most organizations either over-submit or freeze.

**What this artifact does**

* Provides **pre-approved, desk-targeted authority language**  
* Lets NAMI respond immediately and calmly to:  
  * DHS assertions  
  * ADH scope creep  
  * Audit overreach  
  * Committee pressure

**Why it matters to Clearlane**

* Authority disputes are won by **precision**, not volume  
* These inserts:  
  * cite just enough authority  
  * bound scope without antagonizing  
  * avoid accidentally conceding jurisdiction

**What Clearlane gains**

* Speed without risk  
* Confidence in response  
* Written proof of boundary enforcement

**In short:**  
Citation inserts let Clearlane **assert boundaries without escalation**.

---

## **How They Work Together (System View)**

| Artifact | Solves | Protects |
| ----- | ----- | ----- |
| Early-Warning Checklist | Temporal drift | Future agency |
| Template Library | Language contamination | Structural integrity |
| Citation Inserts | Authority challenges | Jurisdictional boundaries |

Together, they ensure Clearlane is:

* **Preventive** (before entry)  
* **Durable** (over time)  
* **Defensible** (under scrutiny)

---

## **Canonical Summary**

**Clearlane is not just about seeing authority.**  
**These artifacts ensure NAMI can act on that sight — repeatedly, safely, and without capture.**

If you want a recommendation:  
**Build them in this order:**

1. Early-Warning Checklist  
2. Template Library  
3. Citation Inserts

