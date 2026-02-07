# UX Concepts for Tricia Navigation

**Status:** IDEAS/PLANNING
**Primary User:** Tricia (NAMI Arkansas operational navigation)
**Context:** Mobile-first, field use, quick reference

---

## Core Requirements

1. **Mobile-friendly** - Works on phone in the field
2. **Quick lookup** - Find authority/flow in seconds
3. **Offline capable** - Core data cached locally
4. **Visual** - Sankey, org charts, timelines
5. **Actionable** - "What do I do next?" answers

---

## UX Ideas (Capture Space)

### Idea: [Name]
- **Type:** [Dashboard/Search/Visual/Alert/Reference]
- **Platform:** [Mobile/Desktop/Both]
- **Priority:** [High/Medium/Low]
- **Description:** 

---

### Idea: Authority Chain Lookup
- **Type:** Search/Reference
- **Platform:** Mobile
- **Priority:** HIGH
- **Description:** 
  - Input: "Peer support certification"
  - Output: Visual chain showing who controls what
  - Tap any node for details

---

### Idea: Money Flow Tracer
- **Type:** Visual
- **Platform:** Both
- **Priority:** HIGH
- **Description:**
  - Start at any source/destination
  - See all flows in/out
  - Color by restriction (Medicaid, DHS-controlled, etc.)

---

### Idea: "Who Approves This?" Quick Answer
- **Type:** Search/Reference
- **Platform:** Mobile
- **Priority:** HIGH
- **Description:**
  - Voice or text: "Who approves peer certification?"
  - Returns: Kirk Lane → OSAMH → DHS Secretary chain
  - Shows alternative pathways if they exist

---

### Idea: Alert Dashboard
- **Type:** Dashboard
- **Platform:** Desktop
- **Priority:** MEDIUM
- **Description:**
  - Shows gaps in coverage
  - Highlights missing validations
  - Flags expiring authorities

---

### Idea: Meeting Prep Card
- **Type:** Reference
- **Platform:** Mobile
- **Priority:** HIGH
- **Description:**
  - Before meeting with official X
  - Shows: their position, what they control, relevant flows
  - Key talking points
  - Related artifacts to reference

---

## Implementation Options

### Option A: Static HTML (Current)
- `explorer.html` already works
- Add mobile CSS
- Add search/filter

### Option B: PWA (Progressive Web App)
- Offline support
- Home screen install
- Push notifications

### Option C: React/Vue App
- Full interactivity
- Complex visualizations
- Requires build step

### Option D: Claude Artifacts
- On-demand generation
- Always current
- Requires API access

---

## Add Your Ideas Below

(Keep adding here, we'll organize later)

---
