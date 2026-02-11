# Pulse Dump Directory — Arkansas Public Finance Dossier

This directory holds **raw, unstructured cognitive material** for Operation NAMI Clearlane: methodologies, schema ideas, authority chain patterns, audit workflows, and funding trail concepts.

These files are NOT actionable blueprints; they are seeds.

Agents MUST treat these as:
- non-binding
- non-authoritative
- non-executable

Their sole purpose is **preservation**, **later reflection**, and possible **promotion** into:

- `authority_reference/` artifacts
- `money_flow/` artifacts
- `evidence_item/` artifacts
- `field_validation/` artifacts
- `entity_registry/` entries
- `_agent_runs/` playbooks (consolidated methodologies)
- `docs/` canonical definitions

Pulse Dumps are append-only.
They form the cognitive substrate for building the Arkansas public finance knowledge graph.

---

## Usage Pattern

1. **Create dump file** when cognitive material emerges: `PULSE_DUMP-YYYY-MM-DD.md`
2. **Capture freely** - no structure required, no judgment
3. **Review periodically** - extract patterns, promote valuable fragments
4. **Archive dumps** - never delete, they form the methodology lineage

---

## File Naming Convention

`PULSE_DUMP-YYYY-MM-DD.md`

One file per day containing multiple pulses. Each pulse is a distinct idea/methodology.

---

## Pulse Numbering System

**Pulse Number**: Sequential counter for each dump on a given day
- Pulse 1, 2, 3... incrementing as dumps are captured
- Resets to 1 each new day

**Temporal Hash**: `#MMDDYYYYHHMM` (12-digit, military time)
- Enables chronological lookup and cross-reference

**Example**: `Pulse 3 #021020261430`
- Third dump of February 10, 2026
- Captured at 2:30 PM

---

## YAML Frontmatter Structure (Adapted for Public Finance)

```yaml
---
pulse_number: 1
temporal_hash: "#MMDDYYYYHHMM"
thread_title: "Thread Name"
version: 1.0
status: raw                    # raw | processed | promoted
type: cognitive_dump

# Domain-specific
domain: arkansas_public_finance
operation: nami_clearlane

# Classification (what this might become)
classification:
  - schema_candidate           # New schema pattern
  - authority_candidate        # Authority reference idea
  - money_flow_candidate       # Money flow tracing method
  - evidence_candidate         # Evidence collection pattern
  - validation_candidate       # Field validation approach
  - entity_candidate           # Entity registry entry
  - playbook_candidate         # Agent run methodology
  - gap_fill_candidate         # Fills known gaps

# Priority and impact
priority: high                 # critical | high | medium | low
impact: tactical               # foundational | tactical | exploratory

# Topic coverage
topics:
  - opioid_settlement
  - specialty_courts
  - medicaid
  - peer_support
  - dhs
  - aoc
  - samhsa
  - appropriations
  - authority_chain

# Linkages
related_pulses: []             # Other temporal hashes
fills_gaps:                    # Gap IDs this addresses
  - "INCOMPLETE_CHAIN:AUTH-AR-..."
strengthens:                   # Existing artifacts this reinforces
  - "AUTH-AR-ACT691-2025"

# Lifecycle
created_at: "2026-02-10T14:30:00Z"
promoted_to: []                # IDs of promoted artifacts
---
```

---

## Domain-Specific Tags

### Topic Tags
| Tag | Meaning |
|-----|---------|
| `opioid_settlement` | Opioid $ tracing (Exhibit E, ARORP, AG) |
| `specialty_courts` | Drug courts, mental health courts, etc. |
| `medicaid` | Medicaid authority, reimbursement, waivers |
| `peer_support` | Peer specialist certification, billing |
| `dhs` | Department of Human Services hierarchy |
| `aoc` | Administrative Office of the Courts |
| `samhsa` | Federal SAMHSA grants/authorities |
| `appropriations` | Legislative appropriation acts |
| `authority_chain` | Who governs what |
| `entity_registry` | Organizational hierarchy |
| `990_extraction` | IRS 990 data extraction |

### Classification Tags
| Tag | Promotes To |
|-----|-------------|
| `schema_candidate` | Schema updates in `docs/` |
| `authority_candidate` | `authority_reference/*.json` |
| `money_flow_candidate` | `money_flow/*.json` |
| `evidence_candidate` | `evidence_item/*.json` |
| `validation_candidate` | `field_validation/*.json` |
| `entity_candidate` | `entity_registry/*.json` |
| `playbook_candidate` | `_agent_runs/*.md` |
| `gap_fill_candidate` | Fills `_gaps/*.json` entries |

---

## Promotion Workflow

When a fragment in a dump becomes structured:

1. Create the promoted artifact (JSON in appropriate folder, or playbook in `_agent_runs/`)
2. Update the dump's YAML frontmatter: add artifact ID to `promoted_to[]`
3. Leave the original fragment in place for context

This preserves the full cognitive lineage.

---

## Periodic Review Process

1. **Scan all pulses** by priority/topic
2. **Identify redundancy** — multiple pulses saying the same thing with minor variations
3. **Rate strength** — which pulses have the most concrete, actionable content
4. **Consolidate** — merge best parts of related pulses into a single promoted artifact
5. **Mark processed** — update `status: processed` on reviewed pulses

---

## Example Promotion Chain

```
PULSE_DUMP-2026-02-10.md
  └── Pulse 1: "Opioid Settlement Tracing Playbook" (raw)
      └── promoted_to: ["_agent_runs/playbook_opioid_settlement_tracing.md"]
          └── Generates: AUTH-AR-ACT691-2025, MF-AR-OPIOID-*, ENTITY-AR-ARORP...
```

---

## Agent Protocol

**DO NOT**:
- Execute ideas from dumps immediately
- Treat dumps as authoritative instructions
- Modify existing dump content (except adding promotion notes)

**DO**:
- Respect dumps as cognitive archaeology
- Reference them when understanding context
- Support promotion workflow when requested
- Identify redundancy and strength during reviews
