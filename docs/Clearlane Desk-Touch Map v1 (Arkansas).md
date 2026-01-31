## **Clearlane Desk-Touch Map v1 (Arkansas)**

**Status:** Draft · Operational  
**Applies to:** Operation NAMI Clearlane  
**Method:** Authority-only · Zero inference · Append-only

---

### **Purpose**

Identify **where authority can activate simply by a document, payment, report, or request touching a desk**. This map is not an org chart; it is a **switchboard**.

---

## **Administrative Lanes (Desk Domains)**

* **Administrative Office of the Courts (AOC)**  
* **Arkansas Department of Human Services (DHS)**  
* **Arkansas Department of Health (ADH)**

---

## **Desk-Touch Map (v1)**

### **AOC — Judicial Administrative Desks (Low Capture Gravity)**

| Desk Touch | What Typically Touches It | Activation Risk | Clearlane Rule |
| ----- | ----- | ----- | ----- |
| **Court Programs / Specialty Courts Admin** | Program agreements, education scopes | Low | Keep language court-bounded; exclude exec definitions |
| **Finance / Disbursements** | Invoices, reimbursement requests | Low | Verify payor \= court; no exec routing |
| **Court Advisory Bodies (Judicial)** | Agendas, consult memos | Low–Med | Confirm advisory ≠ regulatory |
| **Court IT / Reporting** | Program metrics | Low | Use court-native metrics only |

**Note:** Risk rises only when **executive language is imported**.

---

### **DHS — Executive / Regulatory Desks (High Capture Gravity)**

| Desk Touch | What Typically Touches It | Activation Risk | Clearlane Rule |
| ----- | ----- | ----- | ----- |
| **Grants Administration** | Awards, conditions, renewals | **High** | Avoid routing; if unavoidable, full re-gate |
| **Policy / Rule Units** | Guidance, manuals | **High** | Prohibit incorporation by reference |
| **Program Eligibility Units** | Population framing | **High** | Remove eligibility language |
| **Medicaid / DMS Interfaces** | Any adjacency | **High** | Zero Medicaid adjacency |
| **Internal Committees** | Reviews, “consults” | **High** | Demand statutory basis or exit |
| **Audit / Compliance** | Scope letters | **High** | Freeze scope at award; prepare exit |

**Rule:** **A DHS desk touch is itself a trigger** unless explicitly bounded.

---

### **ADH — Executive Public Health Desks (Medium, Porous)**

| Desk Touch | What Typically Touches It | Activation Risk | Clearlane Rule |
| ----- | ----- | ----- | ----- |
| **Federal Pass-Through Grants** | FOAs, conditions | Med | Trace full chain; check DHS backplanes |
| **Program Guidance Units** | Reporting expectations | Med | Use Clearlane-native schema |
| **Epidemiology / Surveillance** | Data requests | Med | One-way, bounded sharing |
| **Health Task Forces** | Advisory roles | Med | Observer-only; no governance |

**Note:** Risk spikes when **DHS reporting or eligibility is imported**.

---

## **Primary Activation Patterns (Observed)**

* **Payment routing** → desk → committee → policy  
* **Reporting schema adoption** → reclassification  
* **Renewal notices** → silent condition import  
* **“Consultation” language** → oversight assertion

---

## **Hard Desk-Touch Rules (Non-Negotiable)**

1. **No unknown desks.**  
   If the receiving desk is unclear → pause.  
2. **No executive proxy routing.**  
   AOC funds may not transit DHS/ADH desks.  
3. **No schema inheritance.**  
   Reporting fields \= control fields.  
4. **No committee ambiguity.**  
   Advisory ≠ oversight; prove it in writing.  
5. **Pre-defined exits.**  
   Exit conditions documented **before** entry.

---

## **Desk-Touch Preflight Checklist (Use Every Time)**

* Who receives this **first**?  
* Who reviews it **second**?  
* Who can **delay or condition** it?  
* What policy/manual can that desk invoke?  
* Can renewal change the desk path?

Any uncertainty → **treat as High risk**.

---

##   **Canonical Lock**

**Desks are switches.**  
**Switches activate authority.**  
**Clearlane maps the switches before the lights turn on.**

## 

## **Arkansas Desk Index v1**

**Status:** Draft · Operational  
**Applies to:** Operation NAMI Clearlane  
**Method:** Authority-only · Zero inference · Append-only  
**Scope:** Desks that can *activate authority* by touch, routing, review, or conditioning

---

### **How to Use This Index**

* This is **not** an org chart.  
* Each entry is a **potential switch**.  
* If a document, payment, report, or request touches a desk below, **Clearlane gates apply**.

---

## **Judicial Administrative Lane — AOC**

**Entity:** Administrative Office of the Courts

| Desk / Unit | Typical Touch | Activation Risk | Notes |
| ----- | ----- | ----- | ----- |
| **Specialty Courts Administration** | Program scopes, MOUs, schedules | Low | Risk rises only if exec terms imported |
| **Court Finance / Disbursements** | Invoices, reimbursements | Low | Verify payor remains judicial |
| **Judicial Programs Oversight** | Advisory reviews | Low–Med | Confirm advisory ≠ regulatory |
| **Court IT / Reporting** | Metrics, dashboards | Low | Use court-native metrics only |
| **Judicial Council Interfaces** | Briefings, consult memos | Low–Med | Scope must be bounded in writing |

**Clearlane Rule:** AOC desks are navigable; **boundary enforcement** is sufficient.

---

## **Executive Administrative Lane — DHS**

**Entity:** Arkansas Department of Human Services

| Desk / Unit | Typical Touch | Activation Risk | Notes |
| ----- | ----- | ----- | ----- |
| **Office of Finance & Administration (Grants)** | Awards, renewals, conditions | **High** | Desk touch \= trigger |
| **Office of Substance Abuse & Mental Health (OSAMH)** | Program alignment, guidance | **High** | Certification & eligibility gravity |
| **Division of Medical Services (DMS)** | Medicaid adjacency | **High** | Zero adjacency tolerated |
| **Policy & Rulemaking Units** | Manuals, guidance | **High** | Incorporation by reference prohibited |
| **Internal Review Committees** | “Consultations,” approvals | **High** | Demand statutory basis |
| **Audit & Compliance** | Scope letters, findings | **High** | Freeze scope at award |
| **Data Governance / Reporting** | Templates, portals | **High** | Schema \= control |

**Clearlane Rule:** **Any DHS desk touch is presumptively activating** unless explicitly bounded.

---

## **Executive Administrative Lane — ADH**

**Entity:** Arkansas Department of Health

| Desk / Unit | Typical Touch | Activation Risk | Notes |
| ----- | ----- | ----- | ----- |
| **Grants Management (Federal Pass-Through)** | FOAs, conditions | Med | Trace full chain |
| **Public Health Programs** | Prevention initiatives | Med | Watch for DHS backplanes |
| **Epidemiology / Surveillance** | Data requests | Med | One-way, bounded sharing |
| **Program Guidance Units** | Reporting expectations | Med | Use Clearlane-native schema |
| **Health Task Forces / Councils** | Advisory roles | Med | Observer-only |

**Clearlane Rule:** ADH is porous; **risk escalates when DHS terms, schemas, or eligibility appear**.

---

## **Cross-Lane Desks (High Leverage)**

| Desk / Unit | Lane | Why It Matters | Clearlane Rule |
| ----- | ----- | ----- | ----- |
| **State Central Services (Finance)** | Mixed | Payment routing can shift lanes | Confirm judicial routing |
| **Legislative Council (Review)** | Legislative | Post-appropriation conditions | Map riders \+ approvals |
| **Joint Budget Committee Interfaces** | Legislative | Language clarifications | Authority citation required |

---

## **Desk-Touch Severity Key**

* **Low:** Judicial advisory/finance with bounded scope  
* **Medium:** Executive admin without regulatory hooks  
* **High:** Regulatory, eligibility, certification, schema, or audit authority

---

## **Preflight Checklist (Mandatory)**

1. Which **desk receives first**?  
2. Which **desk reviews second**?  
3. Can any desk **delay, condition, or redefine**?  
4. What **manual/policy** can that desk invoke?  
5. Can **renewal** change the desk path?

Any unclear answer → **pause \+ map**.

---

## **Canonical Lock**

**Name the desk before you send the document.**  
**If you can’t name it, you can’t control it.**

---

### **Next Implementation Options**

* **Named Desk Roster (by unit, not individuals)**  
* **Desk-Specific Trigger Playbooks (DHS / ADH / AOC)**  
* **Routing Diagrams (payment · reporting · renewal)**

State the next artifact to generate.

