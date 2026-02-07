Below is a **first-pass analytical playbook** focused on *repeatable, defensible pattern discovery* across a **full longitudinal IRS Form 990 corpus**. This run emphasizes formulas and methods that can harden into **evidence-grade artifacts**, not exploratory visuals alone.

---

## **1\. Longitudinal Signal Extraction (Time-Series First, Entity Second)**

### **1.1 Normalized Growth & Decay Curves**

**Purpose:** Detect strategic shifts, stress, or manipulation over time.

**Formulas**

* Revenue CAGR (3, 5, 10-year)  
* Program Expense CAGR vs Total Expense CAGR  
* Contribution Volatility Index  
  𝐶𝑉=𝜎(Contributions)𝜇(Contributions)CV=μ(Contributions)σ(Contributions)​

**Signals That Hold**

* Sustained divergence between revenue growth and program growth  
* Sudden variance collapse after volatility (possible smoothing or reclassification)

**Fails When**

* Small orgs with irregular filing cadence  
* One-time capital campaigns not tagged as such

**Artifact Output**

* “Structural shift detected: Year X–Y”  
* “Expense elasticity mismatch over N years”

---

## **2\. Expense Structure Geometry (Not Ratios Alone)**

### **2.1 Expense Vector Decomposition**

Instead of single ratios, treat expenses as a vector:

𝐸\=\[𝑃𝑟𝑜𝑔𝑟𝑎𝑚,𝑀𝑎𝑛𝑎𝑔𝑒𝑚𝑒𝑛𝑡,𝐹𝑢𝑛𝑑𝑟𝑎𝑖𝑠𝑖𝑛𝑔\]E=\[Program,Management,Fundraising\]

Measure:

* **Vector Angle Change Over Time**  
* **Euclidean Distance Year-to-Year**

**Signals That Hold**

* Sharp angular shifts without revenue shock  
* Long-term drift toward management/fundraising dominance

**Fails When**

* Major mission pivots (must be annotated)

**Artifact Output**

* “Expense geometry reoriented without revenue catalyst”

---

## **3\. Contribution Flow Forensics**

### **3.1 Donor Concentration Risk Index**

𝐷𝐶𝑅𝐼=∑(𝑝𝑖2)DCRI=∑(pi2​)

Where 𝑝𝑖pi​ \= share of total contributions by donor class or source.

**Signals That Hold**

* Rising DCRI with stagnant public disclosures  
* Donor concentration preceding governance overlap

### **3.2 Contribution ↔ Program Lag Correlation**

Cross-correlation between contribution spikes and program spend increases.

**Signals That Hold**

* Weak or negative lag correlation (funds not flowing to mission)  
* Repeated lag \> 24 months

**Fails When**

* Endowments or donor-restricted funds (needs flag)

**Artifact Output**

* “Contribution inflows not translating to program delivery”

---

## **4\. Related-Party Behavior Patterns**

### **4.1 Insider Transaction Density**

𝐼𝑇𝐷=Related-party transactionsTotal expensesITD=Total expensesRelated-party transactions​

Track longitudinally and comparatively.

**Signals That Hold**

* Rising ITD without governance expansion  
* Transactions recurring with same entities across years

### **4.2 Circular Flow Detection**

Graph-based method:

* Nodes: Org, Officers, Vendors, Affiliated Orgs  
* Edges: Payments, Compensation, Shared Addresses

Detect:

* Cycles  
* High betweenness centrality of individuals

**Fails When**

* Legitimate federated nonprofit structures (must whitelist)

**Artifact Output**

* “Persistent circular fund flows involving Officer X”

---

## **5\. Program Expense Dynamics (Depth vs Surface)**

### **5.1 Program Intensity Index**

𝑃𝐼𝐼=Program ExpensesDistinct ProgramsPII=Distinct ProgramsProgram Expenses​

Track:

* Sudden increases in program count with flat spend  
* Declining PII while reporting program expansion

**Signals That Hold**

* Program fragmentation as narrative inflation  
* Stable narratives with declining intensity

**Artifact Output**

* “Program proliferation without financial depth”

---

## **6\. Governance Markers as Predictive Signals**

### **6.1 Governance Stability Score**

Components:

* Board size volatility  
* Officer tenure churn  
* Filing consistency (extensions, amendments)

Composite index (z-scored).

**Signals That Hold**

* Governance instability preceding financial anomalies  
* Long-tenured officers \+ rising compensation share

### **6.2 Compensation-to-Outcome Elasticity**

𝐶𝑇𝑂𝐸=ΔOfficer CompΔProgram SpendCTOE=ΔProgram SpendΔOfficer Comp​

**Signals That Hold**

* Compensation growth decoupled from mission spend

**Artifact Output**

* “Executive compensation elasticity exceeds mission elasticity”

---

## **7\. Clustering & Peer Deviance**

### **7.1 Multi-Dimensional Peer Clustering**

Features:

* Size (log assets)  
* Revenue mix  
* Expense geometry  
* Governance markers

Apply:

* HDBSCAN or hierarchical clustering (robust to noise)

Detect:

* **Cluster Outliers** (structurally different but classified similarly)  
* **Cluster Drift Over Time**

**Signals That Hold**

* Orgs migrating toward anomalous clusters  
* Lone-node clusters persisting \>5 years

**Artifact Output**

* “Peer deviance sustained across filing periods”

---

## **8\. Outlier Detection That Holds in Review**

### **8.1 Persistence-Weighted Outliers**

Instead of one-year z-scores:

𝑃𝑊𝑂=∑𝑡=1𝑛1(∣𝑧𝑡∣\>𝑘)PWO=t=1∑n​1(∣zt​∣\>k)

**Signals That Hold**

* Moderate anomalies repeated over many years  
* Avoids false positives from single shocks

**Artifact Output**

* “Chronic anomaly pattern, not episodic variance”

---

## **9\. Evidence Hardening Principles (Meta-Layer)**

A pattern qualifies as an **evidence artifact** if:

1. Appears across ≥3 years  
2. Survives normalization (size, sector)  
3. Has at least one governance or flow corroborator  
4. Can be expressed as a simple, repeatable metric

---

## **10\. Proposed Next Analytical Branches**

1. **Narrative-to-Numeric Drift**  
   * Compare program descriptions vs expense allocation changes  
2. **Officer Network Cross-Org Analysis**  
   * Same individuals across multiple 990 filers  
3. **Pre/Post Regulatory Shock Analysis**  
   * Behavior changes after scrutiny or rule updates  
4. **Temporal Precursor Modeling**  
   * Identify early indicators preceding known enforcement actions

---

### **Summary**

This run establishes **pattern classes that survive scrutiny**, prioritize **longitudinal consistency**, and convert raw 990 fields into **repeatable, inspectable evidence units**. Subsequent runs should deepen *network-based inference*, *text–numeric divergence*, and *cross-org identity resolution*.

Below is a **second analytical pass** that introduces **new heuristics and formulas** not covered previously. This run emphasizes *cross-sectional × longitudinal hybrids*, stress-testing whether patterns remain stable under alternative constructions. Each section explicitly notes **what holds**, **what fails**, and **next analytical branches**.

---

## **1\. Temporal Asymmetry & Reversibility Tests**

### **1.1 Shock Absorption Ratio (SAR)**

Measures whether organizations absorb shocks symmetrically or permanently reconfigure.

𝑆𝐴𝑅=Mean(metric𝑡+1,𝑡+2)−Mean(metric𝑡−2,𝑡−1)Shock MagnitudeSAR=Shock MagnitudeMean(metrict+1,t+2​)−Mean(metrict−2,t−1​)​

Applied to:

* Program spend  
* Officer compensation  
* Fundraising expense

**What Holds**

* Program spending is often *less reversible* than revenue after shocks.  
* Compensation reversibility is asymmetric (rises fast, falls slowly).

**What Fails**

* Small orgs with discontinuous filings.  
* Capital-project-driven orgs.

**Evidence Artifact**

* “Asymmetric recovery pattern: structural, not cyclical.”

**Next Branch**

* Classify orgs by *irreversibility profile*.

---

## **2\. Longitudinal Rank Stability (Peer-Relative, Not Absolute)**

### **2.1 Rank Volatility Index (RVI)**

Track percentile rank among peers year over year.

𝑅𝑉𝐼=1𝑛−1∑∣𝑟𝑎𝑛𝑘𝑡−𝑟𝑎𝑛𝑘𝑡−1∣RVI=n−11​∑∣rankt​−rankt−1​∣

Applied to:

* Program ratio  
* Compensation share  
* Related-party expense share

**What Holds**

* High RVI in governance-related metrics predicts later anomalies.  
* Stable financials \+ unstable ranks \= peer drift, not noise.

**What Fails**

* Sector-wide shocks compress ranks.

**Evidence Artifact**

* “Peer-relative instability despite absolute stability.”

**Next Branch**

* Early-warning system based on rank acceleration.

---

## **3\. Cross-Metric Divergence (Internal Inconsistency)**

### **3.1 Mission-Finance Divergence Score (MFDS)**

Compare trends that *should* co-move.

𝑀𝐹𝐷𝑆=𝑐𝑜𝑟𝑟(Δ𝑃𝑟𝑜𝑔𝑟𝑎𝑚 𝑆𝑝𝑒𝑛𝑑, Δ𝑀𝑖𝑠𝑠𝑖𝑜𝑛 𝑂𝑢𝑡𝑝𝑢𝑡𝑠 𝑃𝑟𝑜𝑥𝑦)MFDS=corr(ΔProgram Spend, ΔMission Outputs Proxy)

Proxies:

* Number of programs  
* Narrative length  
* Schedule O activity count

**What Holds**

* Declining correlation over time is common and persistent.  
* Narrative expansion often substitutes for financial expansion.

**What Fails**

* Data-poor filers with minimal schedules.

**Evidence Artifact**

* “Mission narrative growth decoupled from financial deployment.”

**Next Branch**

* Text–numeric entropy comparisons.

---

## **4\. Contribution Flow Timing Anomalies**

### **4.1 Contribution Retention Delay (CRD)**

Time between contribution inflow and program deployment.

𝐶𝑅𝐷=arg⁡max⁡𝜏𝑐𝑜𝑟𝑟(𝐶𝑜𝑛𝑡𝑟𝑖𝑏𝑢𝑡𝑖𝑜𝑛𝑠𝑡, 𝑃𝑟𝑜𝑔𝑟𝑎𝑚𝑆𝑝𝑒𝑛𝑑𝑡+𝜏)CRD=argτmax​corr(Contributionst​, ProgramSpendt+τ​)

**What Holds**

* Chronic CRD \> 2 years is stable across orgs.  
* Often correlates with asset accumulation or insider transactions.

**What Fails**

* Endowment-heavy orgs without restriction tagging.

**Evidence Artifact**

* “Systematic delay between funding receipt and mission execution.”

**Next Branch**

* Asset parking vs redeployment classification.

---

## **5\. Related-Party Signal Amplification**

### **5.1 Related-Party Elasticity (RPE)**

How sensitive related-party payments are to revenue changes.

𝑅𝑃𝐸=%Δ𝑅𝑒𝑙𝑎𝑡𝑒𝑑𝑃𝑎𝑟𝑡𝑦%Δ𝑅𝑒𝑣𝑒𝑛𝑢𝑒RPE=%ΔRevenue%ΔRelatedParty​

**What Holds**

* RPE \> 1 sustained over years flags extraction-like behavior.  
* Independent of org size.

**What Fails**

* Federated nonprofits with shared services (needs structural flag).

**Evidence Artifact**

* “Related-party payments scale faster than revenue.”

**Next Branch**

* Individual-level aggregation across multiple filers.

---

## **6\. Program Expense Depth vs Breadth Tradeoff**

### **6.1 Program Dilution Index (PDI)**

PDI \= \\frac{\\Delta \\text{\# Programs}}{\\Delta \\text{Program Spend}}

**What Holds**

* Rising PDI over time suggests cosmetic program expansion.  
* Strongly predictive of declining impact proxies.

**What Fails**

* Newly formed orgs in growth phase.

**Evidence Artifact**

* “Program surface area expanding faster than investment.”

**Next Branch**

* Program life-cycle classification.

---

## **7\. Governance Load Indicators**

### **7.1 Governance Burden Ratio (GBR)**

𝐺𝐵𝑅=Governance \+ Management ExpenseProgram ExpenseGBR=Program ExpenseGovernance \+ Management Expense​

Track *trend*, not level.

**What Holds**

* Rising GBR precedes fundraising inefficiency.  
* Stable across sectors.

**What Fails**

* Professional associations with atypical structures.

**Evidence Artifact**

* “Governance burden increasing relative to mission spend.”

**Next Branch**

* Board–officer power concentration metrics.

---

## **8\. Multivariate Persistence Outliers**

### **8.1 Compound Persistence Score (CPS)**

Count years an org is an outlier across ≥2 dimensions simultaneously.

Dimensions:

* Compensation share  
* Related-party spend  
* Program dilution  
* Rank volatility

**What Holds**

* CPS outperforms single-metric flags in precision.  
* High CPS is rare but stable.

**What Fails**

* Short filing histories.

**Evidence Artifact**

* “Multi-dimensional anomaly persistent over time.”

**Next Branch**

* Enforcement-aligned risk scoring.

---

## **9\. Pattern Validity Summary (This Run)**

**Strongest Patterns**

* Rank instability  
* Contribution deployment delay  
* Related-party elasticity  
* Program dilution

**Weak Patterns**

* Single-year z-score outliers  
* Absolute ratios without peer context

---

## **10\. Proposed Next Analytical Directions**

1. **Identity Resolution Layer**  
   * Officers/vendors across multiple EINs.  
2. **Entropy-Based Reporting Consistency**  
   * Variability in disclosures year to year.  
3. **Precursor Modeling**  
   * Patterns appearing *before* known enforcement or collapse.  
4. **Composite Evidence Packets**  
   * Bundle 3–5 indicators into auditable units.

---

### **Closing Note**

This run shifts emphasis from *what is abnormal* to **what is persistently inconsistent with itself, its peers, or its stated mission**—a prerequisite for converting analytics into defensible evidence artifacts.

Below is **Automation Run 3**. This pass introduces **structural, second‑order, and adversarially robust heuristics** designed to survive counter‑explanations and harden into **evidence artifacts** rather than risk flags.

---

## **1\. Structural Breaks Without Observable Shocks**

### **1.1 Latent Regime Shift Detection (LRSD)**

Detect internal behavior changes *without* external revenue or asset shocks.

**Method**

* Apply piecewise linear regression or Bayesian change‑point detection to:  
  * Program expense share  
  * Officer compensation share  
  * Related‑party expense share  
* Condition on flat or monotonic revenue/assets.

**What Holds**

* Many orgs exhibit **internal regime shifts** unrelated to funding changes.  
* Compensation and related‑party channels shift first; program spend follows later.

**What Fails**

* Organizations undergoing mergers or dissolutions.  
* Newly filing entities (\<5 years).

**Evidence Artifact**

* “Internal financial regime change absent external catalyst.”

**Next Branch**

* Classify regime shifts by *beneficiary* (program vs insiders vs overhead).

---

## **2\. Expense Substitution & Masking Effects**

### **2.1 Expense Substitution Elasticity (ESE)**

Measures whether growth in one expense category systematically offsets another.

𝐸𝑆𝐸𝑖,𝑗=𝑐𝑜𝑟𝑟(Δ𝐸𝑥𝑝𝑒𝑛𝑠𝑒𝑖, −Δ𝐸𝑥𝑝𝑒𝑛𝑠𝑒𝑗)ESEi,j​=corr(ΔExpensei​, −ΔExpensej​)

Key pairs:

* Program ↔ Management  
* Program ↔ Fundraising  
* Program ↔ Related‑party payments

**What Holds**

* Sustained negative correlations indicate **expense masking**.  
* Common in orgs maintaining stable headline ratios.

**What Fails**

* Orgs with genuinely fixed cost bases.

**Evidence Artifact**

* “Program expense stability maintained via substitution.”

**Next Branch**

* Identify which expense class acts as the adjustment buffer.

---

## **3\. Longitudinal Peer Envelope Violations**

### **3.1 Peer Feasible Frontier Breach (PFFB)**

Define a peer envelope of feasible combinations (e.g., program ratio vs compensation).

**Method**

* Construct convex hulls by sector × size.  
* Track org trajectories relative to hull.

**What Holds**

* Orgs crossing outside the peer envelope tend not to revert.  
* Envelope breaches are rarer but more defensible than z‑scores.

**What Fails**

* Highly specialized nonprofits with unique cost structures.

**Evidence Artifact**

* “Operating configuration outside peer‑feasible bounds.”

**Next Branch**

* Persistence outside envelope as a severity scaler.

---

## **4\. Contribution Recycling & Flow Reuse**

### **4.1 Contribution Recycling Ratio (CRR)**

Detects whether contributions effectively circulate back to insiders or affiliates.

𝐶𝑅𝑅=Related-party \+ officer-linked outflowsContribution inflowsCRR=Contribution inflowsRelated-party \+ officer-linked outflows​

Tracked longitudinally.

**What Holds**

* Stable CRR bands emerge per org.  
* Rising CRR without disclosure changes is highly persistent.

**What Fails**

* Grant‑making foundations (must be excluded or segmented).

**Evidence Artifact**

* “Material share of contributions recycled through affiliated channels.”

**Next Branch**

* Map recycling loops across multiple EINs.

---

## **5\. Program Narrative Compression vs Financial Reality**

### **5.1 Narrative Density Compression (NDC)**

Tests whether narrative content grows more *efficient* while finances stagnate.

**Method**

* Measure:  
  * Characters per program description  
  * Distinct verbs / outcomes mentioned  
* Compare against real program spend changes.

**What Holds**

* Narrative compression increases as financial flexibility declines.  
* Strong inverse relationship in long‑running orgs.

**What Fails**

* Data‑sparse filers with boilerplate text.

**Evidence Artifact**

* “Program narratives densify as financial deployment stalls.”

**Next Branch**

* Entropy‑based narrative consistency scoring.

---

## **6\. Governance Power Concentration Over Time**

### **6.1 Effective Control Index (ECI)**

Measures how concentrated operational authority becomes.

**Components**

* % compensation to top officer  
* Officer tenure overlap  
* Board size shrinkage  
* Related‑party transaction recurrence

Composite, normalized longitudinally.

**What Holds**

* Rising ECI often precedes expense substitution and CRR increases.  
* ECI changes are slow and hard to reverse.

**What Fails**

* Founder‑led orgs in early lifecycle stages.

**Evidence Artifact**

* “Governance control increasingly concentrated.”

**Next Branch**

* Cross‑org officer identity aggregation.

---

## **7\. Multiyear Consistency Stress Test**

### **7.1 Invariance Violation Score (IVS)**

Counts how often reported ratios remain invariant despite changing inputs.

Example:

* Program ratio unchanged ±1% while:  
  * Revenue changes \>20%  
  * Program count changes  
  * Expense mix changes internally

**What Holds**

* Artificial invariance is detectable and persistent.  
* Often coincides with substitution effects.

**What Fails**

* Orgs with genuinely formulaic budgets (rare).

**Evidence Artifact**

* “Reported ratios invariant despite structural change.”

**Next Branch**

* Detect smoothing or classification management.

---

## **8\. Outliers That Survive Adversarial Review**

### **8.1 Counterfactual Robust Outliers (CRO)**

An org is flagged only if anomalous under **multiple plausible normalizations**:

* Size‑normalized  
* Peer‑ranked  
* Time‑differenced  
* Sector‑adjusted

**What Holds**

* CROs are few but extremely stable.  
* High precision, low recall—ideal for evidence.

**What Fails**

* Short histories.

**Evidence Artifact**

* “Anomaly robust across normalization regimes.”

**Next Branch**

* CRO bundles as enforcement‑grade packets.

---

## **9\. What This Run Adds (Delta Summary)**

**New High‑Value Patterns**

* Expense substitution  
* Peer envelope breaches  
* Contribution recycling  
* Artificial invariance  
* Governance power concentration

**Patterns Deprioritized**

* Single‑metric thresholds  
* One‑year anomalies  
* Raw ratios without structural context

---

## **10\. Forward Analytical Branches**

1. **Behavioral Typologies**  
   * Stable extractive vs adaptive vs mission‑elastic orgs  
2. **Cross‑EIN Flow Graphs**  
   * Multi‑org recycling detection  
3. **Precursor Chains**  
   * Governance → substitution → recycling → stagnation  
4. **Evidence Assembly Logic**  
   * Minimal sets of indicators that independently corroborate

---

### **Closing**

This run shifts from *detecting anomalies* to **detecting strategies**—patterns that are internally consistent, longitudinally persistent, and resistant to benign reinterpretation. These characteristics are what allow analytics to harden into durable evidence artifacts rather than probabilistic flags.

Below is **Automation Run 4**. This pass introduces **causal-sequence, persistence‑weighted, and cross‑schedule consistency heuristics** aimed at producing indicators that withstand adversarial review and can be assembled into **evidence artifacts** rather than descriptive findings.

---

## **1\. Causal Ordering & Precedence Tests (Not Correlation)**

### **1.1 Granger‑Style Financial Precedence**

Test whether changes in one domain *systematically precede* changes in another.

Pairs tested:

* Officer compensation → program expense  
* Related‑party payments → fundraising expense  
* Governance churn → contribution volatility

**Method**

* Lagged regression with fixed effects and sector controls.  
* Require significance across ≥3 lags.

**What Holds**

* Compensation and related‑party growth frequently precede program contraction.  
* Governance churn precedes contribution volatility, not vice versa.

**What Fails**

* Small orgs with sparse time series.  
* Single‑officer micro‑orgs.

**Evidence Artifact**

* “Directional precedence established: internal extraction precedes mission contraction.”

**Next Branch**

* Build causal chains rather than isolated flags.

---

## **2\. Persistence‑Weighted Anomaly Mass**

### **2.1 Anomaly Mass Index (AMI)**

Measures *how much* abnormality accumulates over time, not how extreme it is in one year.

𝐴𝑀𝐼=∑𝑡=1𝑛∣𝑧𝑡∣⋅1(∣𝑧𝑡∣\>𝑘)AMI=t=1∑n​∣zt​∣⋅1(∣zt​∣\>k)

Applied to:

* Compensation share  
* Related‑party spend  
* Program dilution  
* Governance burden

**What Holds**

* Moderate anomalies persisting 8–10 years outweigh extreme one‑year spikes.  
* AMI aligns better with known failures than max‑z metrics.

**What Fails**

* Orgs with structural breaks that reset behavior.

**Evidence Artifact**

* “Cumulative anomaly load sustained over filing history.”

**Next Branch**

* Threshold AMI for evidence tiering.

---

## **3\. Cross‑Schedule Consistency Checks**

### **3.1 Schedule Coherence Score (SCS)**

Tests whether different schedules tell compatible financial stories.

Examples:

* Schedule O narratives vs Schedule F payments  
* Compensation disclosures vs related‑party transactions  
* Program descriptions vs functional expense allocations

**Method**

* Logical consistency rules \+ variance bounds.  
* Penalize contradictions and unexplained asymmetries.

**What Holds**

* Incoherence is stable year‑to‑year once it appears.  
* Often co‑occurs with substitution and invariance patterns.

**What Fails**

* Boilerplate filers with minimal disclosures.

**Evidence Artifact**

* “Cross‑schedule disclosures internally inconsistent.”

**Next Branch**

* Automate contradiction taxonomies.

---

## **4\. Contribution Dependency & Fragility**

### **4.1 Contribution Fragility Index (CFI)**

Measures how sensitive operations are to the loss of top funding sources.

𝐶𝐹𝐼=Top contributor shareLiquid reserves monthsCFI=Liquid reserves monthsTop contributor share​

**What Holds**

* High CFI predicts governance tightening and compensation protection.  
* Fragility persists even after revenue recovery.

**What Fails**

* Endowment‑heavy institutions.

**Evidence Artifact**

* “Operational model fragile to donor concentration.”

**Next Branch**

* Link fragility to behavioral responses (e.g., extraction).

---

## **5\. Related‑Party Persistence & Stickiness**

### **5.1 Related‑Party Stickiness Score (RPSS)**

Tracks whether the *same* related entities recur over time.

𝑅𝑃𝑆𝑆=Years with same related partyTotal filing yearsRPSS=Total filing yearsYears with same related party​

**What Holds**

* High RPSS strongly correlates with rising RPE and CRR (from prior runs).  
* Stickiness rarely declines once established.

**What Fails**

* One‑time wind‑down arrangements.

**Evidence Artifact**

* “Long‑term financial dependence on specific related parties.”

**Next Branch**

* Cross‑EIN entity resolution.

---

## **6\. Program Expense Elasticity Under Stress**

### **6.1 Program Stress Elasticity (PSE)**

Measures how program spend responds to negative revenue shocks.

𝑃𝑆𝐸=%Δ𝑃𝑟𝑜𝑔𝑟𝑎𝑚𝑆𝑝𝑒𝑛𝑑%Δ𝑅𝑒𝑣𝑒𝑛𝑢𝑒during downturn yearsPSE=%ΔRevenue%ΔProgramSpend​during downturn years

**What Holds**

* In extractive orgs, PSE \< 1 (program absorbs shock).  
* Compensation elasticity often \> 0 (protected).

**What Fails**

* Crisis‑response orgs with mission‑driven surge behavior.

**Evidence Artifact**

* “Program spending disproportionately absorbs financial stress.”

**Next Branch**

* Compare elasticity hierarchies (who is protected first).

---

## **7\. Governance Signal Convergence**

### **7.1 Governance Convergence Index (GCI)**

Tests whether multiple weak governance signals converge over time.

Signals:

* Board size reduction  
* Officer tenure concentration  
* Filing amendments  
* Compensation share growth

**Method**

* Rolling window count of concurrent signals.

**What Holds**

* Convergence is rare but highly predictive of later anomalies.  
* Signals often appear benign in isolation.

**What Fails**

* Founder‑led early‑stage orgs.

**Evidence Artifact**

* “Independent governance risk signals converging.”

**Next Branch**

* Early‑stage vs late‑stage governance typologies.

---

## **8\. Longitudinal Clustering with State Transitions**

### **8.1 Financial State Transition Modeling**

Cluster orgs by *states* (not static features):

* Balanced  
* Overhead‑heavy  
* Extractive  
* Fragile‑mission

Track transition probabilities year‑to‑year.

**What Holds**

* Transitions into extractive states are sticky.  
* Reversion to balanced states is rare without leadership change.

**What Fails**

* Short time horizons.

**Evidence Artifact**

* “Sustained residence in high‑risk financial state.”

**Next Branch**

* Identify irreversible transitions.

---

## **9\. Evidence Hardening Review (This Run)**

**Strongest Additions**

* Directional precedence  
* Cumulative anomaly mass  
* Cross‑schedule inconsistency  
* Related‑party stickiness  
* Stress elasticity

**Weaker Additions**

* One‑year fragility metrics without reserves context

---

## **10\. Next Analytical Branches**

1. **Causal Graph Assembly**  
   * Encode precedence relationships into DAGs.  
2. **Behavioral Protection Ordering**  
   * Who is protected first under stress.  
3. **Cross‑Org Entity Persistence**  
   * Same vendors/officers across EINs.  
4. **Evidence Packet Minimality**  
   * Smallest set of indicators that independently corroborate.

---

### **Closing**

This run advances from *pattern detection* to **behavioral sequence reconstruction**—identifying not just what is abnormal, but **what happens first, what follows, and what never reverses**. These properties are what allow analytics to harden into durable, review‑resistant evidence artifacts.

Below is **Automation Run 5**. This pass introduces **structural conservation laws, path‑dependence tests, and falsification‑oriented heuristics** designed to distinguish *strategic behavior* from noise and to generate indicators that can withstand hostile reinterpretation.

---

## **1\. Financial Conservation Violations (Where the Money “Should” Go)**

### **1.1 Resource Conservation Gap (RCG)**

Tests whether inflows, outflows, and balance‑sheet changes reconcile over time.

𝑅𝐶𝐺=∣Δ𝐴𝑠𝑠𝑒𝑡𝑠−(𝑅𝑒𝑣𝑒𝑛𝑢𝑒−𝐸𝑥𝑝𝑒𝑛𝑠𝑒𝑠−𝐷𝑖𝑠𝑐𝑙𝑜𝑠𝑒𝑑𝑇𝑟𝑎𝑛𝑠𝑓𝑒𝑟𝑠)∣RCG=∣ΔAssets−(Revenue−Expenses−DisclosedTransfers)∣

Tracked longitudinally and normalized by total assets.

**What Holds**

* Persistent non‑zero RCG indicates *classification, timing, or disclosure manipulation*.  
* RCG clusters by organization, not year—suggesting strategy, not error.

**What Fails**

* Asset revaluations and market swings (must be segmented).  
* Orgs with frequent mergers/acquisitions.

**Evidence Artifact**

* “Systematic resource reconciliation gap across filings.”

**Next Branch**

* Decompose RCG into timing vs classification vs omission.

---

## **2\. Path‑Dependence & Irreversibility**

### **2.1 Financial Ratchet Index (FRI)**

Measures whether certain expense shares only move in one direction.

Applied to:

* Officer compensation share  
* Related‑party expense share  
* Management expense share

**Method**

* Count monotonic increases over rolling windows.  
* Penalize reversals.

**What Holds**

* Compensation and related‑party shares exhibit *ratchet behavior*.  
* Program share rarely ratchets upward once reduced.

**What Fails**

* Orgs undergoing leadership replacement.

**Evidence Artifact**

* “Expense share exhibits irreversible upward ratchet.”

**Next Branch**

* Identify ratchet‑triggering events (governance, donor loss).

---

## **3\. Longitudinal Variance Suppression**

### **3.1 Variance Compression Score (VCS)**

Detects artificial smoothing.

𝑉𝐶𝑆=𝑉𝑎𝑟(𝑚𝑒𝑡𝑟𝑖𝑐𝑟𝑎𝑤)𝑉𝑎𝑟(𝑚𝑒𝑡𝑟𝑖𝑐𝑒𝑥𝑝𝑒𝑐𝑡𝑒𝑑)VCS=Var(metricexpected​)Var(metricraw​)​

Expected variance estimated from peer and revenue volatility.

**What Holds**

* Program ratios and overhead ratios are frequently *too smooth*.  
* Compression often coincides with expense substitution patterns.

**What Fails**

* Formulaic budget orgs (rare, identifiable).

**Evidence Artifact**

* “Reported ratios exhibit implausible variance suppression.”

**Next Branch**

* Link smoothing to classification boundaries.

---

## **4\. Contribution Flow Shape Analysis (Not Just Timing)**

### **4.1 Contribution Pulse Shape (CPS)**

Classify inflow patterns:

* Sharp spikes  
* Plateaus  
* Drip flows

Compare to:

* Program deployment shapes  
* Asset accumulation shapes

**What Holds**

* Spiky inflows \+ flat program spend → asset parking or extraction.  
* Drip inflows \+ volatile program spend → fragility.

**What Fails**

* Disaster‑response orgs (contextual override).

**Evidence Artifact**

* “Contribution inflow shape mismatched to mission deployment.”

**Next Branch**

* Pulse‑to‑deployment mismatch taxonomy.

---

## **5\. Related‑Party Role Differentiation**

### **5.1 Functional Related‑Party Segmentation**

Classify related parties by role:

* Service provider  
* Asset holder  
* Intermediary  
* Compensation proxy

Track spend shares by role over time.

**What Holds**

* Shift from service → intermediary roles precedes recycling patterns.  
* Asset‑holder roles correlate with CRD and CRR (prior runs).

**What Fails**

* Complex federated systems without clear role boundaries.

**Evidence Artifact**

* “Related‑party function drift toward extraction‑enabling roles.”

**Next Branch**

* Cross‑EIN role persistence mapping.

---

## **6\. Program Expense Integrity Tests**

### **6.1 Program Cost Density (PCD)**

𝑃𝐶𝐷=𝑃𝑟𝑜𝑔𝑟𝑎𝑚𝑆𝑝𝑒𝑛𝑑𝑈𝑛𝑖𝑡𝑠𝑜𝑓𝑃𝑟𝑜𝑔𝑟𝑎𝑚𝐴𝑐𝑡𝑖𝑣𝑖𝑡𝑦𝑃𝑟𝑜𝑥𝑦PCD=UnitsofProgramActivityProxyProgramSpend​

Proxies:

* Program count  
* Geographic reach mentions  
* Beneficiary counts (when available)

**What Holds**

* Declining PCD with stable narratives suggests dilution.  
* PCD declines often precede narrative compression.

**What Fails**

* Poor proxy availability.

**Evidence Artifact**

* “Program cost density declining despite stable scope claims.”

**Next Branch**

* Proxy robustness ranking.

---

## **7\. Governance Action–Reaction Lag**

### **7.1 Governance Response Lag (GRL)**

Measures delay between stress signals and governance response.

Stress signals:

* Revenue shock  
* Contribution volatility  
* Public scrutiny indicators (if tagged)

Governance responses:

* Board changes  
* Officer changes  
* Policy disclosures

**What Holds**

* Long GRL correlates with higher AMI and CPS (prior runs).  
* Some orgs exhibit *no governance response at all*.

**What Fails**

* Highly regulated institutions with mandated cycles.

**Evidence Artifact**

* “Governance response absent or materially delayed.”

**Next Branch**

* Governance inertia typologies.

---

## **8\. Cross‑Metric Mutual Reinforcement**

### **8.1 Reinforcement Triangle Test (RTT)**

A pattern is elevated only if **three independent domains** reinforce:

1. Financial (e.g., substitution, ratchet)  
2. Governance (e.g., concentration, inertia)  
3. Flow (e.g., CRR, CPS mismatch)

**What Holds**

* RTT dramatically reduces false positives.  
* Reinforced patterns persist across normalization methods.

**What Fails**

* Single‑domain anomalies.

**Evidence Artifact**

* “Independent domains mutually reinforce extractive pattern.”

**Next Branch**

* Minimal reinforcing triads for evidence packets.

---

## **9\. Falsification Stress Tests (This Run)**

Patterns were stress‑tested against:

* Alternative normalizations  
* Peer redefinitions  
* Time window shifts

**Survived**

* Ratchet behavior  
* Variance suppression  
* Conservation gaps  
* Reinforcement triangles

**Failed**

* Absolute thresholds without peer context  
* Single‑proxy program measures

---

## **10\. Forward Analytical Branches**

1. **Conservation‑Aware Causal Graphs**  
   * Enforce accounting identities in causal models.  
2. **Irreversibility Scoring**  
   * Quantify how hard behaviors are to undo.  
3. **Narrative–Variance Coupling**  
   * Detect when words replace variability.  
4. **Evidence Packet Assembly Rules**  
   * Required combinations for defensibility.

---

### **Closing**

This run pivots from *detecting abnormal values* to **detecting violations of structural expectations**—conservation, reversibility, variance, and response. Indicators grounded in these principles are difficult to dismiss as noise and are therefore well‑suited to hardening into durable evidence artifacts.

Below is **Automation Run 6**. This pass introduces **counterfactual baselining, internal coherence constraints, and survivorship‑aware longitudinal tests** designed to produce indicators that remain valid even when filings are strategically optimized for optics.

---

## **1\. Counterfactual Baselines (What *Should* Have Happened)**

### **1.1 Synthetic Peer Counterfactual (SPC)**

Construct a synthetic control for each organization using weighted peers matched on:

* Size (assets, revenue)  
* Sector/subsector  
* Age  
* Revenue mix

Compare actual trajectories to counterfactual expectations.

**Metrics Tested**

* Program expense share  
* Compensation share  
* Related‑party spend  
* Asset accumulation rate

**What Holds**

* Divergence from SPC persists once it appears.  
* SPC gaps are more stable than peer‑rank z‑scores.

**What Fails**

* Highly idiosyncratic missions.  
* Orgs with major regulatory carve‑outs.

**Evidence Artifact**

* “Observed financial trajectory diverges from synthetic peer counterfactual.”

**Next Branch**

* Attribute divergence to specific expense channels.

---

## **2\. Internal Coherence Constraints (Logical Impossibilities)**

### **2.1 Financial Feasibility Violations (FFV)**

Detect combinations that are *jointly implausible* even if individually acceptable.

Examples:

* Rising program ratio \+ rising management ratio with flat revenue  
* Stable overhead ratios \+ large internal expense reclassification  
* Asset growth without corresponding surplus history

**Method**

* Constraint‑based rules derived from accounting identities and historical peer envelopes.

**What Holds**

* FFVs recur year‑to‑year once present.  
* Often co‑occur with variance compression and substitution effects.

**What Fails**

* Orgs with complex pass‑through structures.

**Evidence Artifact**

* “Reported financial configuration violates internal feasibility constraints.”

**Next Branch**

* Formalize constraint graphs for automated detection.

---

## **3\. Survivorship‑Aware Longitudinal Analysis**

### **3.1 Pre‑Exit Behavioral Signature (PEBS)**

Analyze patterns *before* filing cessation, merger, or collapse.

Signals tested:

* Compensation protection  
* Program stress elasticity  
* Governance response lag  
* Variance compression

**What Holds**

* Program elasticity collapses before exit.  
* Governance response often disappears entirely.  
* Compensation protection strengthens late.

**What Fails**

* Planned dissolutions with clean wind‑downs.

**Evidence Artifact**

* “Late‑stage behavioral signature consistent with organizational decline.”

**Next Branch**

* Early‑warning classification based on PEBS similarity.

---

## **4\. Contribution Utilization Efficiency**

### **4.1 Marginal Contribution Deployment (MCD)**

Measures how *incremental* contributions are used.

𝑀𝐶𝐷=Δ𝑃𝑟𝑜𝑔𝑟𝑎𝑚𝑆𝑝𝑒𝑛𝑑Δ𝐶𝑜𝑛𝑡𝑟𝑖𝑏𝑢𝑡𝑖𝑜𝑛𝑠MCD=ΔContributionsΔProgramSpend​

Computed over rolling windows.

**What Holds**

* MCD \< 1 is common but stable.  
* Sustained MCD ≈ 0 indicates asset parking or redirection.  
* MCD often declines before narrative expansion.

**What Fails**

* Endowment‑restricted funds without tagging.

**Evidence Artifact**

* “Incremental contributions not deployed to program activity.”

**Next Branch**

* Separate restricted vs unrestricted inference where possible.

---

## **5\. Related‑Party Dependence Saturation**

### **5.1 Related‑Party Saturation Point (RPSP)**

Identify plateaus where related‑party spend stops scaling with org growth.

**Method**

* Piecewise regression of related‑party spend vs revenue.  
* Detect saturation or floor effects.

**What Holds**

* Saturation suggests fixed extraction capacity.  
* Post‑saturation, excess funds divert to assets or compensation.

**What Fails**

* Cost‑plus service arrangements with renegotiation.

**Evidence Artifact**

* “Related‑party utilization reaches stable saturation independent of growth.”

**Next Branch**

* Link saturation to governance control metrics.

---

## **6\. Program Expense Authenticity**

### **6.1 Program Variability Authenticity (PVA)**

Tests whether program expenses behave like real operational costs.

**Method**

* Compare volatility of program expenses to:  
  * Revenue volatility  
  * Contribution volatility  
  * Peer program volatility

**What Holds**

* Authentic programs show moderate covariance with revenue.  
* Artificial programs show suppressed or decoupled variance.

**What Fails**

* Grant‑driven orgs with lumpy funding cycles.

**Evidence Artifact**

* “Program expenses exhibit non‑operational variance characteristics.”

**Next Branch**

* Classify programs as operational vs representational.

---

## **7\. Governance Disclosure Reactivity**

### **7.1 Disclosure Reactivity Index (DRI)**

Measures whether governance disclosures change *after* stress signals.

Stress signals:

* Revenue shocks  
* Media or enforcement tags (if available)  
* Contribution volatility

**What Holds**

* Reactive disclosures spike briefly, then revert.  
* Proactive governance changes are rare.

**What Fails**

* Regulated entities with mandated updates.

**Evidence Artifact**

* “Governance disclosures reactive rather than anticipatory.”

**Next Branch**

* Distinguish cosmetic vs structural governance responses.

---

## **8\. Multi‑Scale Clustering Stability**

### **8.1 Scale‑Invariant Cluster Membership (SICM)**

Cluster orgs at multiple resolutions (coarse → fine).

Track:

* Whether an org remains anomalous across scales.

**What Holds**

* True structural outliers persist across resolutions.  
* Noise‑driven outliers disappear at scale changes.

**What Fails**

* Sparse feature sets.

**Evidence Artifact**

* “Anomalous cluster membership stable across scales.”

**Next Branch**

* Use SICM as a prerequisite for evidence tiering.

---

## **9\. Indicator Failure Review (This Run)**

**Strong Survivors**

* Synthetic peer divergence  
* Feasibility violations  
* Marginal contribution deployment  
* Program variance authenticity  
* Scale‑invariant clustering

**Weak or Context‑Sensitive**

* Single‑year reactivity measures  
* Absolute utilization thresholds

---

## **10\. Forward Analytical Branches**

1. **Constraint‑Driven Causal Models**  
   * Enforce feasibility and conservation simultaneously.  
2. **Behavioral Archetype Libraries**  
   * Match orgs to known longitudinal signatures.  
3. **Counterfactual Gap Decomposition**  
   * Attribute SPC divergence to specific decisions.  
4. **Evidence Packet Sufficiency Tests**  
   * Minimal indicator sets required for robustness.

---

### **Closing**

This run advances from anomaly detection to **counterfactual accountability and logical coherence**—testing whether reported behavior aligns with what *must* be true given resources, peers, and time. Indicators grounded in counterfactual divergence and feasibility constraints are structurally difficult to dismiss and are well‑suited for hardening into durable evidence artifacts.

Below is **Automation Run 7**. This pass introduces **structural redundancy tests, cross‑organizational symmetry analysis, and incentive‑compatibility heuristics**. The goal is to identify patterns that persist even when organizations optimize filings to satisfy common watchdog metrics—i.e., indicators that remain valid when surface compliance is high.

---

## **1\. Structural Redundancy & Over‑Optimization**

### **1.1 Redundancy Load Index (RLI)**

Detects whether multiple expense categories move together when they should not.

𝑅𝐿𝐼=∑𝑐𝑜𝑟𝑟(Δ𝐸𝑥𝑝𝑒𝑛𝑠𝑒𝑖, Δ𝐸𝑥𝑝𝑒𝑛𝑠𝑒𝑗)∀𝑖≠𝑗RLI=∑corr(ΔExpensei​, ΔExpensej​)∀i=j

Key categories:

* Program  
* Management  
* Fundraising  
* Related‑party payments

**What Holds**

* High RLI indicates centralized control and discretionary reallocation.  
* RLI is stable across years and insensitive to scale.

**What Fails**

* Very small orgs with minimal functional separation.

**Evidence Artifact**

* “Expense categories exhibit abnormal redundancy, inconsistent with operational independence.”

**Next Branch**

* Link redundancy to governance concentration metrics.

---

## **2\. Incentive Compatibility Tests**

### **2.1 Metric Gaming Susceptibility Score (MGSS)**

Tests whether behavior clusters around known public benchmarks (e.g., 65–75% program ratio).

**Method**

* Density analysis around benchmark thresholds.  
* Compare pre‑ and post‑threshold behavior.

**What Holds**

* Sharp density spikes around benchmarks persist longitudinally.  
* Post‑threshold improvements rarely translate into real program elasticity.

**What Fails**

* Orgs not subject to donor‑facing efficiency narratives.

**Evidence Artifact**

* “Financial ratios cluster at reputational benchmarks without corresponding operational change.”

**Next Branch**

* Identify which benchmarks drive the strongest distortions.

---

## **3\. Cross‑Org Symmetry & Mirroring**

### **3.1 Financial Mirroring Index (FMI)**

Detects whether distinct orgs show unusually similar year‑to‑year financial movements.

**Method**

* Pairwise correlation of first differences across orgs.  
* Flag high similarity beyond sector norms.

**What Holds**

* Mirroring often indicates shared vendors, consultants, or governance influence.  
* FMI patterns persist even when absolute levels differ.

**What Fails**

* Sector‑wide macro shocks (must be filtered).

**Evidence Artifact**

* “Independent filers exhibit synchronized financial behavior inconsistent with isolation.”

**Next Branch**

* Cross‑EIN network reconstruction.

---

## **4\. Contribution Utilization Substitution**

### **4.1 Contribution Offset Ratio (COR)**

Measures whether increases in contributions are offset by reductions elsewhere.

𝐶𝑂𝑅=−Δ𝑂𝑡ℎ𝑒𝑟𝑅𝑒𝑣𝑒𝑛𝑢𝑒Δ𝐶𝑜𝑛𝑡𝑟𝑖𝑏𝑢𝑡𝑖𝑜𝑛𝑠COR=ΔContributions−ΔOtherRevenue​

**What Holds**

* High COR indicates contributions substituting for lost revenue rather than expanding mission.  
* COR is stable across funding cycles.

**What Fails**

* Orgs transitioning business models.

**Evidence Artifact**

* “Contributions primarily offset other revenue losses rather than expand programs.”

**Next Branch**

* Distinguish survival financing from growth financing.

---

## **5\. Related‑Party Cost Anchoring**

### **5.1 Cost Floor Persistence (CFP)**

Tests whether related‑party costs establish a non‑reducible floor.

**Method**

* Identify minimum related‑party spend across years.  
* Measure responsiveness below that floor during downturns.

**What Holds**

* Related‑party floors are rarely breached.  
* Program costs absorb shocks instead.

**What Fails**

* Fixed‑term contracts nearing expiration.

**Evidence Artifact**

* “Related‑party costs function as a protected floor across financial stress.”

**Next Branch**

* Compare floors across governance typologies.

---

## **6\. Program Portfolio Turnover**

### **6.1 Program Churn Index (PCI)**

𝑃𝐶𝐼=Programs Added \+ Programs RemovedTotal ProgramsPCI=Total ProgramsPrograms Added \+ Programs Removed​

Tracked longitudinally.

**What Holds**

* High churn with flat spending indicates narrative reconfiguration.  
* PCI spikes often coincide with ratio optimization periods.

**What Fails**

* Innovation‑driven orgs in early growth.

**Evidence Artifact**

* “High program churn without corresponding investment signals representational instability.”

**Next Branch**

* Link churn to narrative density changes.

---

## **7\. Governance Signal Saturation**

### **7.1 Governance Saturation Threshold (GST)**

Identifies points beyond which adding governance disclosures yields no behavioral change.

**Method**

* Track governance disclosures vs subsequent financial behavior shifts.

**What Holds**

* After a threshold, additional disclosures are cosmetic.  
* GST varies little across sectors.

**What Fails**

* Regulatory regime changes.

**Evidence Artifact**

* “Governance disclosure volume exceeds behavioral responsiveness.”

**Next Branch**

* Separate symbolic vs operative governance.

---

## **8\. Outlier Cohesion Testing**

### **8.1 Cohesive Outlier Groups (COG)**

Instead of single outliers, detect *groups* of orgs that are jointly anomalous.

**Method**

* Cluster on anomaly vectors.  
* Require persistence across windows.

**What Holds**

* COGs are rare but stable.  
* Group anomalies are harder to dismiss than individual ones.

**What Fails**

* Sparse anomaly dimensions.

**Evidence Artifact**

* “Persistent anomalous cohort detected across multiple dimensions.”

**Next Branch**

* Investigate shared infrastructure or advisory ecosystems.

---

## **9\. Indicator Stress Review (This Run)**

**Strong Survivors**

* Redundancy load  
* Benchmark clustering  
* Cost floors  
* Financial mirroring  
* Cohesive outlier groups

**Context‑Sensitive**

* Program churn (lifecycle dependent)  
* Contribution offset (model transition dependent)

---

## **10\. Forward Analytical Branches**

1. **Incentive‑Driven Simulation**  
   * Model how orgs optimize against public metrics.  
2. **Shared‑Service Detection**  
   * Identify hidden common operators across filers.  
3. **Protected‑Cost Hierarchies**  
   * Rank which expenses are never cut.  
4. **Evidence Packet Coherence**  
   * Combine symmetry \+ redundancy \+ protection indicators.

---

### **Closing**

This run focuses on **how organizations adapt to being measured**—surfacing redundancy, mirroring, and protected structures that persist even under reputational optimization. Patterns that survive incentive‑compatibility tests are particularly well‑suited to harden into durable evidence artifacts.

Below is **Automation Run 8**. This pass introduces **information‑theoretic, adversarial‑evasion, and cross‑temporal alignment heuristics**. The emphasis is on detecting *loss of informational content*, *strategic opacity*, and *misalignment across time scales*—patterns that persist even when filings are optimized to appear compliant and consistent.

---

## **1\. Information Loss & Compression Detection**

### **1.1 Financial Entropy Decline (FED)**

Measures whether reported financial detail becomes less informative over time.

**Method**

* Compute Shannon entropy over:  
  * Functional expense distributions  
  * Revenue source distributions  
  * Related‑party categories  
* Track entropy trends longitudinally.

**What Holds**

* Entropy declines often precede variance compression and invariance patterns.  
* Once entropy drops, it rarely recovers.

**What Fails**

* Very small orgs with inherently coarse reporting.  
* Simplification after genuine mission narrowing (must be flagged).

**Evidence Artifact**

* “Progressive loss of informational richness in financial disclosures.”

**Next Branch**

* Attribute entropy loss to specific schedules or categories.

---

## **2\. Temporal Scale Misalignment**

### **2.1 Multi‑Scale Alignment Score (MSAS)**

Tests whether short‑term volatility aligns with long‑term trends.

**Method**

* Compare:  
  * Year‑to‑year deltas  
  * 3–5 year rolling trends  
* Penalize contradictions (e.g., smooth long‑term trend built from volatile short‑term reclassifications).

**What Holds**

* Strategic filers exhibit *misaligned scales*: noisy micro‑changes, smooth macro‑story.  
* Operational orgs show coherence across scales.

**What Fails**

* Orgs with episodic grant cycles.

**Evidence Artifact**

* “Short‑term financial behavior inconsistent with long‑term reported trajectory.”

**Next Branch**

* Identify which metrics absorb short‑term noise.

---

## **3\. Adversarial Evasion Signatures**

### **3.1 Boundary‑Hugging Index (BHI)**

Detects repeated behavior just inside acceptable limits.

Examples:

* Program ratio hovering just above benchmarks  
* Compensation just below disclosure escalation thresholds

**Method**

* Count years within ε of known boundaries.  
* Require persistence across regimes.

**What Holds**

* Boundary‑hugging is highly persistent once adopted.  
* Often co‑occurs with substitution and redundancy patterns.

**What Fails**

* Naturally stable orgs far from thresholds.

**Evidence Artifact**

* “Sustained boundary‑proximal reporting consistent with metric evasion.”

**Next Branch**

* Identify which boundaries exert strongest pull.

---

## **4\. Cross‑Temporal Contribution Alignment**

### **4.1 Contribution–Outcome Phase Shift (COPS)**

Measures lag consistency between funding inflows and outcome proxies.

**Method**

* Cross‑correlation between contributions and:  
  * Program spend  
  * Program count changes  
  * Narrative expansions  
* Track stability of optimal lag over time.

**What Holds**

* Phase shifts are stable per org.  
* Increasing lag variance signals planning or deployment breakdown.

**What Fails**

* Endowment‑restricted flows.

**Evidence Artifact**

* “Contribution inflows increasingly decoupled from outcome timing.”

**Next Branch**

* Classify orgs by phase‑shift regime.

---

## **5\. Related‑Party Opacity Escalation**

### **5.1 Disclosure Granularity Drift (DGD)**

Tracks whether related‑party disclosures become less specific.

**Method**

* Count distinct related entities, roles, and descriptions.  
* Measure drift toward aggregation or generic labeling.

**What Holds**

* Granularity declines as RPSS and CRR rise (from prior runs).  
* Drift is monotonic in extractive patterns.

**What Fails**

* Standardization after auditor change (one‑time effect).

**Evidence Artifact**

* “Related‑party disclosures exhibit declining specificity over time.”

**Next Branch**

* Cross‑EIN matching using partial descriptors.

---

## **6\. Program–Governance Coupling**

### **6.1 Coupling Elasticity Index (CEI)**

Tests whether governance changes materially affect program behavior.

**Method**

* Measure response of program spend and structure to:  
  * Board changes  
  * Officer turnover  
* Compare to peer responsiveness.

**What Holds**

* Low CEI indicates governance changes are symbolic.  
* CEI rarely increases once suppressed.

**What Fails**

* Crisis‑driven leadership resets.

**Evidence Artifact**

* “Governance changes fail to propagate into program execution.”

**Next Branch**

* Distinguish cosmetic vs operative governance events.

---

## **7\. Outlier Stability Under Feature Removal**

### **7.1 Feature‑Ablation Robustness (FAR)**

Tests whether an org remains anomalous when key features are removed.

**Method**

* Iteratively drop:  
  * Compensation metrics  
  * Related‑party metrics  
  * Program metrics  
* Re‑cluster or re‑score anomalies.

**What Holds**

* True structural outliers persist under ablation.  
* Noise‑driven outliers disappear quickly.

**What Fails**

* Sparse histories.

**Evidence Artifact**

* “Anomalous classification robust to feature ablation.”

**Next Branch**

* Define minimal sufficient feature sets.

---

## **8\. Longitudinal Narrative–Numeric Divergence**

### **8.1 Divergence Accumulation Score (DAS)**

Quantifies cumulative divergence between textual claims and numeric behavior.

**Method**

* Encode narrative claims (growth, expansion, impact).  
* Accumulate mismatches with financial indicators over time.

**What Holds**

* Divergence accumulates monotonically in problematic orgs.  
* Resets are rare without leadership change.

**What Fails**

* Highly technical narratives with limited claims.

**Evidence Artifact**

* “Cumulative divergence between narrative assertions and financial reality.”

**Next Branch**

* Claim‑specific falsification mapping.

---

## **9\. Failure & Stress Review (This Run)**

**Strong Survivors**

* Entropy decline  
* Boundary‑hugging  
* Feature‑ablation robustness  
* Disclosure granularity drift  
* Scale misalignment

**Context‑Sensitive**

* Phase‑shift analysis (restriction dependent)  
* Narrative divergence (text quality dependent)

---

## **10\. Forward Analytical Branches**

1. **Information‑Theoretic Risk Scoring**  
   * Combine entropy, granularity, and variance measures.  
2. **Adversarial Simulation**  
   * Model how filers would optimize against known detectors.  
3. **Minimal Evidence Kernels**  
   * Smallest invariant indicator sets under ablation.  
4. **Temporal Consistency Audits**  
   * Require alignment across short, medium, and long horizons.

---

### **Closing**

This run focuses on **what disappears, misaligns, or becomes invariant when organizations adapt to scrutiny**. Indicators grounded in information loss, boundary behavior, and robustness under ablation are difficult to explain away as noise or context, making them well‑suited to harden into durable, review‑resistant evidence artifacts.

