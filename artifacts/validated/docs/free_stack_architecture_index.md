# Zero-Cost Architectures for Clearlane + IRS Form 990 (GitHub + ChatGPT + Free Tools)

Compiled from the full thread. Includes a complete index with internal links to every section and subsection.

## Index

- [Run 1 - Core Zero-Cost Stack and Static Dashboards](#run-1-core-zero-cost-stack-and-static-dashboards)
  - [1. Baseline Principle (Why This Works Free)](#run-1-core-zero-cost-stack-and-static-dashboards-1-baseline-principle-why-this-works-free)
  - [2. Core Zero-Cost Stack (Recommended Default)](#run-1-core-zero-cost-stack-and-static-dashboards-2-core-zero-cost-stack-recommended-default)
    - [Infrastructure](#run-1-core-zero-cost-stack-and-static-dashboards-2-core-zero-cost-stack-recommended-default-infrastructure)
    - [Data formats](#run-1-core-zero-cost-stack-and-static-dashboards-2-core-zero-cost-stack-recommended-default-data-formats)
    - [UX outcome](#run-1-core-zero-cost-stack-and-static-dashboards-2-core-zero-cost-stack-recommended-default-ux-outcome)
  - [3. Architecture Patterns (Pick 1-2)](#run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2)
    - [A. Question -> Answer Cards (Fastest to Ship)](#run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-a-question-answer-cards-fastest-to-ship)
      - [How it works](#run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-a-question-answer-cards-fastest-to-ship-how-it-works)
      - [Tech](#run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-a-question-answer-cards-fastest-to-ship-tech)
      - [UX](#run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-a-question-answer-cards-fastest-to-ship-ux)
      - [Tradeoffs](#run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-a-question-answer-cards-fastest-to-ship-tradeoffs)
      - [Why it is ideal for Tricia](#run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-a-question-answer-cards-fastest-to-ship-why-it-is-ideal-for-tricia)
    - [B. Markdown-Driven Living Report Dashboard](#run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-b-markdown-driven-living-report-dashboard)
      - [How it works](#run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-b-markdown-driven-living-report-dashboard-how-it-works)
      - [Tech](#run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-b-markdown-driven-living-report-dashboard-tech)
      - [UX](#run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-b-markdown-driven-living-report-dashboard-ux)
      - [Tradeoffs](#run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-b-markdown-driven-living-report-dashboard-tradeoffs)
      - [Strength](#run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-b-markdown-driven-living-report-dashboard-strength)
    - [C. Client-Side Chat-Like Query Layer (Free but Structured)](#run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-c-client-side-chat-like-query-layer-free-but-structured)
      - [Important constraint](#run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-c-client-side-chat-like-query-layer-free-but-structured-important-constraint)
      - [How it works](#run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-c-client-side-chat-like-query-layer-free-but-structured-how-it-works)
      - [Example](#run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-c-client-side-chat-like-query-layer-free-but-structured-example)
      - [Tech](#run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-c-client-side-chat-like-query-layer-free-but-structured-tech)
      - [Tradeoffs](#run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-c-client-side-chat-like-query-layer-free-but-structured-tradeoffs)
      - [Why it is acceptable](#run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-c-client-side-chat-like-query-layer-free-but-structured-why-it-is-acceptable)
  - [4. Using ChatGPT (Free) Without an API](#run-1-core-zero-cost-stack-and-static-dashboards-4-using-chatgpt-free-without-an-api)
    - [Pattern - Bring Your Own Context AI Assist](#run-1-core-zero-cost-stack-and-static-dashboards-4-using-chatgpt-free-without-an-api-pattern-bring-your-own-context-ai-assist)
      - [Flow](#run-1-core-zero-cost-stack-and-static-dashboards-4-using-chatgpt-free-without-an-api-pattern-bring-your-own-context-ai-assist-flow)
      - [Why this matters](#run-1-core-zero-cost-stack-and-static-dashboards-4-using-chatgpt-free-without-an-api-pattern-bring-your-own-context-ai-assist-why-this-matters)
      - [UX trick](#run-1-core-zero-cost-stack-and-static-dashboards-4-using-chatgpt-free-without-an-api-pattern-bring-your-own-context-ai-assist-ux-trick)
  - [5. Visuals You Can Generate 100% Free](#run-1-core-zero-cost-stack-and-static-dashboards-5-visuals-you-can-generate-100-free)
  - [6. Data Refresh Paths (No Automation Costs)](#run-1-core-zero-cost-stack-and-static-dashboards-6-data-refresh-paths-no-automation-costs)
    - [Manual but Clean](#run-1-core-zero-cost-stack-and-static-dashboards-6-data-refresh-paths-no-automation-costs-manual-but-clean)
    - [Semi-Automated (Still Free)](#run-1-core-zero-cost-stack-and-static-dashboards-6-data-refresh-paths-no-automation-costs-semi-automated-still-free)
  - [7. Recommended Leave-Behind Package](#run-1-core-zero-cost-stack-and-static-dashboards-7-recommended-leave-behind-package)
  - [8. Fastest Path to a Working Demo (1-2 Days)](#run-1-core-zero-cost-stack-and-static-dashboards-8-fastest-path-to-a-working-demo-1-2-days)
    - [Day 1](#run-1-core-zero-cost-stack-and-static-dashboards-8-fastest-path-to-a-working-demo-1-2-days-day-1)
    - [Day 2](#run-1-core-zero-cost-stack-and-static-dashboards-8-fastest-path-to-a-working-demo-1-2-days-day-2)
  - [Bottom Line](#run-1-core-zero-cost-stack-and-static-dashboards-bottom-line)
- [Run 2 - Local-First and Prompt-Backed Patterns](#run-2-local-first-and-prompt-backed-patterns)
  - [1. Local-First AI Companion (Zero Hosting Dependency)](#run-2-local-first-and-prompt-backed-patterns-1-local-first-ai-companion-zero-hosting-dependency)
    - [What is new here](#run-2-local-first-and-prompt-backed-patterns-1-local-first-ai-companion-zero-hosting-dependency-what-is-new-here)
    - [Architecture](#run-2-local-first-and-prompt-backed-patterns-1-local-first-ai-companion-zero-hosting-dependency-architecture)
    - [UX](#run-2-local-first-and-prompt-backed-patterns-1-local-first-ai-companion-zero-hosting-dependency-ux)
    - [Why this matters](#run-2-local-first-and-prompt-backed-patterns-1-local-first-ai-companion-zero-hosting-dependency-why-this-matters)
    - [Tradeoffs](#run-2-local-first-and-prompt-backed-patterns-1-local-first-ai-companion-zero-hosting-dependency-tradeoffs)
    - [Fastest free implementation](#run-2-local-first-and-prompt-backed-patterns-1-local-first-ai-companion-zero-hosting-dependency-fastest-free-implementation)
  - [2. Prompt-Backed Dashboard (ChatGPT as a Brain, Not a Backend)](#run-2-local-first-and-prompt-backed-patterns-2-prompt-backed-dashboard-chatgpt-as-a-brain-not-a-backend)
    - [Core idea](#run-2-local-first-and-prompt-backed-patterns-2-prompt-backed-dashboard-chatgpt-as-a-brain-not-a-backend-core-idea)
    - [Architecture](#run-2-local-first-and-prompt-backed-patterns-2-prompt-backed-dashboard-chatgpt-as-a-brain-not-a-backend-architecture)
    - [Button behavior](#run-2-local-first-and-prompt-backed-patterns-2-prompt-backed-dashboard-chatgpt-as-a-brain-not-a-backend-button-behavior)
    - [Why this is different](#run-2-local-first-and-prompt-backed-patterns-2-prompt-backed-dashboard-chatgpt-as-a-brain-not-a-backend-why-this-is-different)
    - [Tradeoffs](#run-2-local-first-and-prompt-backed-patterns-2-prompt-backed-dashboard-chatgpt-as-a-brain-not-a-backend-tradeoffs)
  - [3. Static Question Router (Feels Like Chat, Is Not)](#run-2-local-first-and-prompt-backed-patterns-3-static-question-router-feels-like-chat-is-not)
    - [What is new](#run-2-local-first-and-prompt-backed-patterns-3-static-question-router-feels-like-chat-is-not-what-is-new)
    - [Architecture](#run-2-local-first-and-prompt-backed-patterns-3-static-question-router-feels-like-chat-is-not-architecture)
    - [Example](#run-2-local-first-and-prompt-backed-patterns-3-static-question-router-feels-like-chat-is-not-example)
    - [Why it works](#run-2-local-first-and-prompt-backed-patterns-3-static-question-router-feels-like-chat-is-not-why-it-works)
    - [Tradeoffs](#run-2-local-first-and-prompt-backed-patterns-3-static-question-router-feels-like-chat-is-not-tradeoffs)
  - [4. GitHub Issues as a Question Log](#run-2-local-first-and-prompt-backed-patterns-4-github-issues-as-a-question-log)
    - [Underused but powerful](#run-2-local-first-and-prompt-backed-patterns-4-github-issues-as-a-question-log-underused-but-powerful)
    - [Architecture](#run-2-local-first-and-prompt-backed-patterns-4-github-issues-as-a-question-log-architecture)
    - [UX](#run-2-local-first-and-prompt-backed-patterns-4-github-issues-as-a-question-log-ux)
    - [Why this is clever](#run-2-local-first-and-prompt-backed-patterns-4-github-issues-as-a-question-log-why-this-is-clever)
    - [Tradeoffs](#run-2-local-first-and-prompt-backed-patterns-4-github-issues-as-a-question-log-tradeoffs)
  - [5. Markdown-Only Intelligence (No JS Required)](#run-2-local-first-and-prompt-backed-patterns-5-markdown-only-intelligence-no-js-required)
    - [For maximum longevity](#run-2-local-first-and-prompt-backed-patterns-5-markdown-only-intelligence-no-js-required-for-maximum-longevity)
    - [Architecture](#run-2-local-first-and-prompt-backed-patterns-5-markdown-only-intelligence-no-js-required-architecture)
    - [Enhancements](#run-2-local-first-and-prompt-backed-patterns-5-markdown-only-intelligence-no-js-required-enhancements)
    - [Why this matters](#run-2-local-first-and-prompt-backed-patterns-5-markdown-only-intelligence-no-js-required-why-this-matters)
    - [Tradeoffs](#run-2-local-first-and-prompt-backed-patterns-5-markdown-only-intelligence-no-js-required-tradeoffs)
  - [6. Semi-Automated Refresh (Still Free)](#run-2-local-first-and-prompt-backed-patterns-6-semi-automated-refresh-still-free)
    - [GitHub Actions pattern](#run-2-local-first-and-prompt-backed-patterns-6-semi-automated-refresh-still-free-github-actions-pattern)
    - [Output](#run-2-local-first-and-prompt-backed-patterns-6-semi-automated-refresh-still-free-output)
    - [Risk note](#run-2-local-first-and-prompt-backed-patterns-6-semi-automated-refresh-still-free-risk-note)
  - [7. What to Leave Behind (Critical)](#run-2-local-first-and-prompt-backed-patterns-7-what-to-leave-behind-critical)
  - [Bottom Line (New Insight)](#run-2-local-first-and-prompt-backed-patterns-bottom-line-new-insight)
- [Run 3 - Governance, Explainability, and Handoff Resilience](#run-3-governance-explainability-and-handoff-resilience)
  - [1. Schema-First Explorer (Data Before UI)](#run-3-governance-explainability-and-handoff-resilience-1-schema-first-explorer-data-before-ui)
    - [Core idea](#run-3-governance-explainability-and-handoff-resilience-1-schema-first-explorer-data-before-ui-core-idea)
    - [Architecture](#run-3-governance-explainability-and-handoff-resilience-1-schema-first-explorer-data-before-ui-architecture)
    - [UX](#run-3-governance-explainability-and-handoff-resilience-1-schema-first-explorer-data-before-ui-ux)
    - [Why this is new](#run-3-governance-explainability-and-handoff-resilience-1-schema-first-explorer-data-before-ui-why-this-is-new)
    - [Tradeoffs](#run-3-governance-explainability-and-handoff-resilience-1-schema-first-explorer-data-before-ui-tradeoffs)
    - [Fastest free implementation](#run-3-governance-explainability-and-handoff-resilience-1-schema-first-explorer-data-before-ui-fastest-free-implementation)
  - [2. Decision Notebook (Questions as First-Class Objects)](#run-3-governance-explainability-and-handoff-resilience-2-decision-notebook-questions-as-first-class-objects)
    - [Core idea](#run-3-governance-explainability-and-handoff-resilience-2-decision-notebook-questions-as-first-class-objects-core-idea)
    - [Architecture](#run-3-governance-explainability-and-handoff-resilience-2-decision-notebook-questions-as-first-class-objects-architecture)
    - [UX](#run-3-governance-explainability-and-handoff-resilience-2-decision-notebook-questions-as-first-class-objects-ux)
    - [ChatGPT usage (free UI)](#run-3-governance-explainability-and-handoff-resilience-2-decision-notebook-questions-as-first-class-objects-chatgpt-usage-free-ui)
    - [Why this works](#run-3-governance-explainability-and-handoff-resilience-2-decision-notebook-questions-as-first-class-objects-why-this-works)
    - [Tradeoffs](#run-3-governance-explainability-and-handoff-resilience-2-decision-notebook-questions-as-first-class-objects-tradeoffs)
  - [3. Explainable Metric Library (Anti-Black-Box)](#run-3-governance-explainability-and-handoff-resilience-3-explainable-metric-library-anti-black-box)
    - [Core idea](#run-3-governance-explainability-and-handoff-resilience-3-explainable-metric-library-anti-black-box-core-idea)
    - [Architecture](#run-3-governance-explainability-and-handoff-resilience-3-explainable-metric-library-anti-black-box-architecture)
    - [UX](#run-3-governance-explainability-and-handoff-resilience-3-explainable-metric-library-anti-black-box-ux)
    - [Why it is different](#run-3-governance-explainability-and-handoff-resilience-3-explainable-metric-library-anti-black-box-why-it-is-different)
    - [Tradeoffs](#run-3-governance-explainability-and-handoff-resilience-3-explainable-metric-library-anti-black-box-tradeoffs)
  - [4. Browser-Only Pivot Table Interface](#run-3-governance-explainability-and-handoff-resilience-4-browser-only-pivot-table-interface)
    - [Core idea](#run-3-governance-explainability-and-handoff-resilience-4-browser-only-pivot-table-interface-core-idea)
    - [Architecture](#run-3-governance-explainability-and-handoff-resilience-4-browser-only-pivot-table-interface-architecture)
    - [UX](#run-3-governance-explainability-and-handoff-resilience-4-browser-only-pivot-table-interface-ux)
    - [ChatGPT assist (optional)](#run-3-governance-explainability-and-handoff-resilience-4-browser-only-pivot-table-interface-chatgpt-assist-optional)
    - [Tradeoffs](#run-3-governance-explainability-and-handoff-resilience-4-browser-only-pivot-table-interface-tradeoffs)
  - [5. Narrated Timeline (Temporal Sensemaking)](#run-3-governance-explainability-and-handoff-resilience-5-narrated-timeline-temporal-sensemaking)
    - [Core idea](#run-3-governance-explainability-and-handoff-resilience-5-narrated-timeline-temporal-sensemaking-core-idea)
    - [Architecture](#run-3-governance-explainability-and-handoff-resilience-5-narrated-timeline-temporal-sensemaking-architecture)
    - [UX](#run-3-governance-explainability-and-handoff-resilience-5-narrated-timeline-temporal-sensemaking-ux)
    - [Why this matters](#run-3-governance-explainability-and-handoff-resilience-5-narrated-timeline-temporal-sensemaking-why-this-matters)
    - [Tradeoffs](#run-3-governance-explainability-and-handoff-resilience-5-narrated-timeline-temporal-sensemaking-tradeoffs)
  - [6. Zero-Cost Refresh Strategy (New Angle)](#run-3-governance-explainability-and-handoff-resilience-6-zero-cost-refresh-strategy-new-angle)
    - [Pattern - Human-in-the-Loop Updates](#run-3-governance-explainability-and-handoff-resilience-6-zero-cost-refresh-strategy-new-angle-pattern-human-in-the-loop-updates)
  - [7. Minimal AI Boundary Rule (Critical)](#run-3-governance-explainability-and-handoff-resilience-7-minimal-ai-boundary-rule-critical)
  - [Bottom Line (New Insight)](#run-3-governance-explainability-and-handoff-resilience-bottom-line-new-insight)
- [Run 4 - Browser-Side Analytics and Transparent Querying](#run-4-browser-side-analytics-and-transparent-querying)
  - [1. Browser-Embedded Analytics Engine (DuckDB-Wasm)](#run-4-browser-side-analytics-and-transparent-querying-1-browser-embedded-analytics-engine-duckdb-wasm)
    - [Core idea](#run-4-browser-side-analytics-and-transparent-querying-1-browser-embedded-analytics-engine-duckdb-wasm-core-idea)
    - [Architecture](#run-4-browser-side-analytics-and-transparent-querying-1-browser-embedded-analytics-engine-duckdb-wasm-architecture)
    - [UX](#run-4-browser-side-analytics-and-transparent-querying-1-browser-embedded-analytics-engine-duckdb-wasm-ux)
    - [Why this is new](#run-4-browser-side-analytics-and-transparent-querying-1-browser-embedded-analytics-engine-duckdb-wasm-why-this-is-new)
    - [Tradeoffs](#run-4-browser-side-analytics-and-transparent-querying-1-browser-embedded-analytics-engine-duckdb-wasm-tradeoffs)
    - [Fastest free implementation](#run-4-browser-side-analytics-and-transparent-querying-1-browser-embedded-analytics-engine-duckdb-wasm-fastest-free-implementation)
  - [2. Static SQL-as-Documentation Dashboard](#run-4-browser-side-analytics-and-transparent-querying-2-static-sql-as-documentation-dashboard)
    - [Core idea](#run-4-browser-side-analytics-and-transparent-querying-2-static-sql-as-documentation-dashboard-core-idea)
    - [Architecture](#run-4-browser-side-analytics-and-transparent-querying-2-static-sql-as-documentation-dashboard-architecture)
    - [UX](#run-4-browser-side-analytics-and-transparent-querying-2-static-sql-as-documentation-dashboard-ux)
    - [ChatGPT usage (free UI)](#run-4-browser-side-analytics-and-transparent-querying-2-static-sql-as-documentation-dashboard-chatgpt-usage-free-ui)
    - [Tradeoffs](#run-4-browser-side-analytics-and-transparent-querying-2-static-sql-as-documentation-dashboard-tradeoffs)
  - [3. CSV-First Explorer with Web Metadata (CSVW)](#run-4-browser-side-analytics-and-transparent-querying-3-csv-first-explorer-with-web-metadata-csvw)
    - [Core idea](#run-4-browser-side-analytics-and-transparent-querying-3-csv-first-explorer-with-web-metadata-csvw-core-idea)
    - [Architecture](#run-4-browser-side-analytics-and-transparent-querying-3-csv-first-explorer-with-web-metadata-csvw-architecture)
    - [UX](#run-4-browser-side-analytics-and-transparent-querying-3-csv-first-explorer-with-web-metadata-csvw-ux)
    - [Why this matters](#run-4-browser-side-analytics-and-transparent-querying-3-csv-first-explorer-with-web-metadata-csvw-why-this-matters)
    - [Tradeoffs](#run-4-browser-side-analytics-and-transparent-querying-3-csv-first-explorer-with-web-metadata-csvw-tradeoffs)
  - [4. GitHub Discussions as the Primary UX](#run-4-browser-side-analytics-and-transparent-querying-4-github-discussions-as-the-primary-ux)
    - [Core idea](#run-4-browser-side-analytics-and-transparent-querying-4-github-discussions-as-the-primary-ux-core-idea)
    - [Architecture](#run-4-browser-side-analytics-and-transparent-querying-4-github-discussions-as-the-primary-ux-architecture)
    - [UX](#run-4-browser-side-analytics-and-transparent-querying-4-github-discussions-as-the-primary-ux-ux)
    - [Why it is different](#run-4-browser-side-analytics-and-transparent-querying-4-github-discussions-as-the-primary-ux-why-it-is-different)
    - [Tradeoffs](#run-4-browser-side-analytics-and-transparent-querying-4-github-discussions-as-the-primary-ux-tradeoffs)
  - [5. Observable-Style Notebooks, Exported Static](#run-4-browser-side-analytics-and-transparent-querying-5-observable-style-notebooks-exported-static)
    - [Core idea](#run-4-browser-side-analytics-and-transparent-querying-5-observable-style-notebooks-exported-static-core-idea)
    - [Architecture](#run-4-browser-side-analytics-and-transparent-querying-5-observable-style-notebooks-exported-static-architecture)
    - [UX](#run-4-browser-side-analytics-and-transparent-querying-5-observable-style-notebooks-exported-static-ux)
    - [Why it is valuable](#run-4-browser-side-analytics-and-transparent-querying-5-observable-style-notebooks-exported-static-why-it-is-valuable)
    - [Tradeoffs](#run-4-browser-side-analytics-and-transparent-querying-5-observable-style-notebooks-exported-static-tradeoffs)
  - [6. Service-Worker-Powered Offline Mode](#run-4-browser-side-analytics-and-transparent-querying-6-service-worker-powered-offline-mode)
    - [Core idea](#run-4-browser-side-analytics-and-transparent-querying-6-service-worker-powered-offline-mode-core-idea)
    - [Architecture](#run-4-browser-side-analytics-and-transparent-querying-6-service-worker-powered-offline-mode-architecture)
    - [UX](#run-4-browser-side-analytics-and-transparent-querying-6-service-worker-powered-offline-mode-ux)
    - [Tradeoffs](#run-4-browser-side-analytics-and-transparent-querying-6-service-worker-powered-offline-mode-tradeoffs)
  - [7. Release-Based Data Snapshots (Governance-First)](#run-4-browser-side-analytics-and-transparent-querying-7-release-based-data-snapshots-governance-first)
    - [Core idea](#run-4-browser-side-analytics-and-transparent-querying-7-release-based-data-snapshots-governance-first-core-idea)
    - [Architecture](#run-4-browser-side-analytics-and-transparent-querying-7-release-based-data-snapshots-governance-first-architecture)
    - [UX](#run-4-browser-side-analytics-and-transparent-querying-7-release-based-data-snapshots-governance-first-ux)
    - [Why this is important](#run-4-browser-side-analytics-and-transparent-querying-7-release-based-data-snapshots-governance-first-why-this-is-important)
  - [8. Manual + Semi-Automated Refresh (New Variant)](#run-4-browser-side-analytics-and-transparent-querying-8-manual-semi-automated-refresh-new-variant)
    - [Pattern](#run-4-browser-side-analytics-and-transparent-querying-8-manual-semi-automated-refresh-new-variant-pattern)
    - [Result](#run-4-browser-side-analytics-and-transparent-querying-8-manual-semi-automated-refresh-new-variant-result)
  - [Bottom Line (New Insight)](#run-4-browser-side-analytics-and-transparent-querying-bottom-line-new-insight)
- [Run 5 - Progressive UX and Ambiguity Reduction](#run-5-progressive-ux-and-ambiguity-reduction)
  - [1. Progressive Disclosure Dashboard (Beginner -> Power User)](#run-5-progressive-ux-and-ambiguity-reduction-1-progressive-disclosure-dashboard-beginner-power-user)
    - [Core idea](#run-5-progressive-ux-and-ambiguity-reduction-1-progressive-disclosure-dashboard-beginner-power-user-core-idea)
    - [Architecture](#run-5-progressive-ux-and-ambiguity-reduction-1-progressive-disclosure-dashboard-beginner-power-user-architecture)
    - [UX](#run-5-progressive-ux-and-ambiguity-reduction-1-progressive-disclosure-dashboard-beginner-power-user-ux)
    - [Tradeoffs](#run-5-progressive-ux-and-ambiguity-reduction-1-progressive-disclosure-dashboard-beginner-power-user-tradeoffs)
    - [Fastest free implementation](#run-5-progressive-ux-and-ambiguity-reduction-1-progressive-disclosure-dashboard-beginner-power-user-fastest-free-implementation)
  - [2. Narrative-First, Data-Second Briefing Pages](#run-5-progressive-ux-and-ambiguity-reduction-2-narrative-first-data-second-briefing-pages)
    - [Core idea](#run-5-progressive-ux-and-ambiguity-reduction-2-narrative-first-data-second-briefing-pages-core-idea)
    - [Architecture](#run-5-progressive-ux-and-ambiguity-reduction-2-narrative-first-data-second-briefing-pages-architecture)
    - [ChatGPT usage (free UI)](#run-5-progressive-ux-and-ambiguity-reduction-2-narrative-first-data-second-briefing-pages-chatgpt-usage-free-ui)
    - [Why this is distinct](#run-5-progressive-ux-and-ambiguity-reduction-2-narrative-first-data-second-briefing-pages-why-this-is-distinct)
    - [Tradeoffs](#run-5-progressive-ux-and-ambiguity-reduction-2-narrative-first-data-second-briefing-pages-tradeoffs)
  - [3. Deterministic Why Buttons (No AI in the Loop)](#run-5-progressive-ux-and-ambiguity-reduction-3-deterministic-why-buttons-no-ai-in-the-loop)
    - [Core idea](#run-5-progressive-ux-and-ambiguity-reduction-3-deterministic-why-buttons-no-ai-in-the-loop-core-idea)
    - [Architecture](#run-5-progressive-ux-and-ambiguity-reduction-3-deterministic-why-buttons-no-ai-in-the-loop-architecture)
    - [UX](#run-5-progressive-ux-and-ambiguity-reduction-3-deterministic-why-buttons-no-ai-in-the-loop-ux)
    - [Optional ChatGPT assist](#run-5-progressive-ux-and-ambiguity-reduction-3-deterministic-why-buttons-no-ai-in-the-loop-optional-chatgpt-assist)
    - [Tradeoffs](#run-5-progressive-ux-and-ambiguity-reduction-3-deterministic-why-buttons-no-ai-in-the-loop-tradeoffs)
  - [4. Static Faceted Search (Browse Like a Catalog)](#run-5-progressive-ux-and-ambiguity-reduction-4-static-faceted-search-browse-like-a-catalog)
    - [Core idea](#run-5-progressive-ux-and-ambiguity-reduction-4-static-faceted-search-browse-like-a-catalog-core-idea)
    - [Architecture](#run-5-progressive-ux-and-ambiguity-reduction-4-static-faceted-search-browse-like-a-catalog-architecture)
    - [UX](#run-5-progressive-ux-and-ambiguity-reduction-4-static-faceted-search-browse-like-a-catalog-ux)
    - [Why it works](#run-5-progressive-ux-and-ambiguity-reduction-4-static-faceted-search-browse-like-a-catalog-why-it-works)
    - [Tradeoffs](#run-5-progressive-ux-and-ambiguity-reduction-4-static-faceted-search-browse-like-a-catalog-tradeoffs)
  - [5. Copy-Exactly-This AI Assist Blocks](#run-5-progressive-ux-and-ambiguity-reduction-5-copy-exactly-this-ai-assist-blocks)
    - [Core idea](#run-5-progressive-ux-and-ambiguity-reduction-5-copy-exactly-this-ai-assist-blocks-core-idea)
    - [Architecture](#run-5-progressive-ux-and-ambiguity-reduction-5-copy-exactly-this-ai-assist-blocks-architecture)
    - [UX](#run-5-progressive-ux-and-ambiguity-reduction-5-copy-exactly-this-ai-assist-blocks-ux)
    - [Tradeoffs](#run-5-progressive-ux-and-ambiguity-reduction-5-copy-exactly-this-ai-assist-blocks-tradeoffs)
  - [6. HTML-Only Charts (No JS Libraries)](#run-5-progressive-ux-and-ambiguity-reduction-6-html-only-charts-no-js-libraries)
    - [Core idea](#run-5-progressive-ux-and-ambiguity-reduction-6-html-only-charts-no-js-libraries-core-idea)
    - [Architecture](#run-5-progressive-ux-and-ambiguity-reduction-6-html-only-charts-no-js-libraries-architecture)
    - [UX](#run-5-progressive-ux-and-ambiguity-reduction-6-html-only-charts-no-js-libraries-ux)
    - [Tradeoffs](#run-5-progressive-ux-and-ambiguity-reduction-6-html-only-charts-no-js-libraries-tradeoffs)
  - [7. Data as Attachments Model (Email-Safe, Tool-Agnostic)](#run-5-progressive-ux-and-ambiguity-reduction-7-data-as-attachments-model-email-safe-tool-agnostic)
    - [Core idea](#run-5-progressive-ux-and-ambiguity-reduction-7-data-as-attachments-model-email-safe-tool-agnostic-core-idea)
    - [Architecture](#run-5-progressive-ux-and-ambiguity-reduction-7-data-as-attachments-model-email-safe-tool-agnostic-architecture)
    - [UX](#run-5-progressive-ux-and-ambiguity-reduction-7-data-as-attachments-model-email-safe-tool-agnostic-ux)
    - [Tradeoffs](#run-5-progressive-ux-and-ambiguity-reduction-7-data-as-attachments-model-email-safe-tool-agnostic-tradeoffs)
  - [8. Human-Readable Change Logs (Often Missing, Very Valuable)](#run-5-progressive-ux-and-ambiguity-reduction-8-human-readable-change-logs-often-missing-very-valuable)
    - [Core idea](#run-5-progressive-ux-and-ambiguity-reduction-8-human-readable-change-logs-often-missing-very-valuable-core-idea)
    - [Architecture](#run-5-progressive-ux-and-ambiguity-reduction-8-human-readable-change-logs-often-missing-very-valuable-architecture)
    - [UX](#run-5-progressive-ux-and-ambiguity-reduction-8-human-readable-change-logs-often-missing-very-valuable-ux)
    - [Tradeoffs](#run-5-progressive-ux-and-ambiguity-reduction-8-human-readable-change-logs-often-missing-very-valuable-tradeoffs)
  - [Bottom Line (New Insight)](#run-5-progressive-ux-and-ambiguity-reduction-bottom-line-new-insight)
- [Run 6 - Search, Portability, and Works-Anywhere UX](#run-6-search-portability-and-works-anywhere-ux)
  - [1. Static Search-First Data Portal (Search Beats Chat)](#run-6-search-portability-and-works-anywhere-ux-1-static-search-first-data-portal-search-beats-chat)
    - [Core idea](#run-6-search-portability-and-works-anywhere-ux-1-static-search-first-data-portal-search-beats-chat-core-idea)
    - [Architecture](#run-6-search-portability-and-works-anywhere-ux-1-static-search-first-data-portal-search-beats-chat-architecture)
    - [UX](#run-6-search-portability-and-works-anywhere-ux-1-static-search-first-data-portal-search-beats-chat-ux)
    - [Tradeoffs](#run-6-search-portability-and-works-anywhere-ux-1-static-search-first-data-portal-search-beats-chat-tradeoffs)
    - [Fastest free implementation](#run-6-search-portability-and-works-anywhere-ux-1-static-search-first-data-portal-search-beats-chat-fastest-free-implementation)
  - [2. Spreadsheet-as-UI with Static Publishing](#run-6-search-portability-and-works-anywhere-ux-2-spreadsheet-as-ui-with-static-publishing)
    - [Core idea](#run-6-search-portability-and-works-anywhere-ux-2-spreadsheet-as-ui-with-static-publishing-core-idea)
    - [Architecture](#run-6-search-portability-and-works-anywhere-ux-2-spreadsheet-as-ui-with-static-publishing-architecture)
    - [UX](#run-6-search-portability-and-works-anywhere-ux-2-spreadsheet-as-ui-with-static-publishing-ux)
    - [ChatGPT usage (free UI)](#run-6-search-portability-and-works-anywhere-ux-2-spreadsheet-as-ui-with-static-publishing-chatgpt-usage-free-ui)
    - [Tradeoffs](#run-6-search-portability-and-works-anywhere-ux-2-spreadsheet-as-ui-with-static-publishing-tradeoffs)
  - [3. Static PDF + Interactive Companion Site](#run-6-search-portability-and-works-anywhere-ux-3-static-pdf-interactive-companion-site)
    - [Core idea](#run-6-search-portability-and-works-anywhere-ux-3-static-pdf-interactive-companion-site-core-idea)
    - [Architecture](#run-6-search-portability-and-works-anywhere-ux-3-static-pdf-interactive-companion-site-architecture)
    - [UX](#run-6-search-portability-and-works-anywhere-ux-3-static-pdf-interactive-companion-site-ux)
    - [Tradeoffs](#run-6-search-portability-and-works-anywhere-ux-3-static-pdf-interactive-companion-site-tradeoffs)
  - [4. Field-Guide UX (Reference, Not Dashboard)](#run-6-search-portability-and-works-anywhere-ux-4-field-guide-ux-reference-not-dashboard)
    - [Core idea](#run-6-search-portability-and-works-anywhere-ux-4-field-guide-ux-reference-not-dashboard-core-idea)
    - [Architecture](#run-6-search-portability-and-works-anywhere-ux-4-field-guide-ux-reference-not-dashboard-architecture)
    - [UX](#run-6-search-portability-and-works-anywhere-ux-4-field-guide-ux-reference-not-dashboard-ux)
    - [Tradeoffs](#run-6-search-portability-and-works-anywhere-ux-4-field-guide-ux-reference-not-dashboard-tradeoffs)
  - [5. Client-Side Compare Anything Tool](#run-6-search-portability-and-works-anywhere-ux-5-client-side-compare-anything-tool)
    - [Core idea](#run-6-search-portability-and-works-anywhere-ux-5-client-side-compare-anything-tool-core-idea)
    - [Architecture](#run-6-search-portability-and-works-anywhere-ux-5-client-side-compare-anything-tool-architecture)
    - [UX](#run-6-search-portability-and-works-anywhere-ux-5-client-side-compare-anything-tool-ux)
    - [ChatGPT assist](#run-6-search-portability-and-works-anywhere-ux-5-client-side-compare-anything-tool-chatgpt-assist)
    - [Tradeoffs](#run-6-search-portability-and-works-anywhere-ux-5-client-side-compare-anything-tool-tradeoffs)
  - [6. Pre-Computed Insight Library (No Runtime Logic)](#run-6-search-portability-and-works-anywhere-ux-6-pre-computed-insight-library-no-runtime-logic)
    - [Core idea](#run-6-search-portability-and-works-anywhere-ux-6-pre-computed-insight-library-no-runtime-logic-core-idea)
    - [Architecture](#run-6-search-portability-and-works-anywhere-ux-6-pre-computed-insight-library-no-runtime-logic-architecture)
    - [UX](#run-6-search-portability-and-works-anywhere-ux-6-pre-computed-insight-library-no-runtime-logic-ux)
    - [Tradeoffs](#run-6-search-portability-and-works-anywhere-ux-6-pre-computed-insight-library-no-runtime-logic-tradeoffs)
  - [7. Manual Refresh with Guardrails (New Variant)](#run-6-search-portability-and-works-anywhere-ux-7-manual-refresh-with-guardrails-new-variant)
    - [Pattern](#run-6-search-portability-and-works-anywhere-ux-7-manual-refresh-with-guardrails-new-variant-pattern)
    - [Result](#run-6-search-portability-and-works-anywhere-ux-7-manual-refresh-with-guardrails-new-variant-result)
  - [8. Export Everything Philosophy](#run-6-search-portability-and-works-anywhere-ux-8-export-everything-philosophy)
    - [Core idea](#run-6-search-portability-and-works-anywhere-ux-8-export-everything-philosophy-core-idea)
    - [Architecture](#run-6-search-portability-and-works-anywhere-ux-8-export-everything-philosophy-architecture)
    - [UX](#run-6-search-portability-and-works-anywhere-ux-8-export-everything-philosophy-ux)
    - [Tradeoffs](#run-6-search-portability-and-works-anywhere-ux-8-export-everything-philosophy-tradeoffs)
  - [Bottom Line (New Insight)](#run-6-search-portability-and-works-anywhere-ux-bottom-line-new-insight)
- [Run 7 - Distribution Channels and Reuse](#run-7-distribution-channels-and-reuse)
  - [1. Static API via Versioned JSON Endpoints (API Without a Server)](#run-7-distribution-channels-and-reuse-1-static-api-via-versioned-json-endpoints-api-without-a-server)
    - [Core idea](#run-7-distribution-channels-and-reuse-1-static-api-via-versioned-json-endpoints-api-without-a-server-core-idea)
    - [Architecture](#run-7-distribution-channels-and-reuse-1-static-api-via-versioned-json-endpoints-api-without-a-server-architecture)
    - [UX](#run-7-distribution-channels-and-reuse-1-static-api-via-versioned-json-endpoints-api-without-a-server-ux)
    - [ChatGPT usage (free UI)](#run-7-distribution-channels-and-reuse-1-static-api-via-versioned-json-endpoints-api-without-a-server-chatgpt-usage-free-ui)
    - [Tradeoffs](#run-7-distribution-channels-and-reuse-1-static-api-via-versioned-json-endpoints-api-without-a-server-tradeoffs)
    - [Fastest free implementation](#run-7-distribution-channels-and-reuse-1-static-api-via-versioned-json-endpoints-api-without-a-server-fastest-free-implementation)
  - [2. RSS / Atom Feeds as an Insight Delivery Channel](#run-7-distribution-channels-and-reuse-2-rss-atom-feeds-as-an-insight-delivery-channel)
    - [Core idea](#run-7-distribution-channels-and-reuse-2-rss-atom-feeds-as-an-insight-delivery-channel-core-idea)
    - [Architecture](#run-7-distribution-channels-and-reuse-2-rss-atom-feeds-as-an-insight-delivery-channel-architecture)
    - [UX](#run-7-distribution-channels-and-reuse-2-rss-atom-feeds-as-an-insight-delivery-channel-ux)
    - [Why this is different](#run-7-distribution-channels-and-reuse-2-rss-atom-feeds-as-an-insight-delivery-channel-why-this-is-different)
    - [Tradeoffs](#run-7-distribution-channels-and-reuse-2-rss-atom-feeds-as-an-insight-delivery-channel-tradeoffs)
  - [3. Browser Extension as the UX (Static + Local)](#run-7-distribution-channels-and-reuse-3-browser-extension-as-the-ux-static-local)
    - [Core idea](#run-7-distribution-channels-and-reuse-3-browser-extension-as-the-ux-static-local-core-idea)
    - [Architecture](#run-7-distribution-channels-and-reuse-3-browser-extension-as-the-ux-static-local-architecture)
    - [UX](#run-7-distribution-channels-and-reuse-3-browser-extension-as-the-ux-static-local-ux)
    - [Tradeoffs](#run-7-distribution-channels-and-reuse-3-browser-extension-as-the-ux-static-local-tradeoffs)
    - [Fastest free implementation](#run-7-distribution-channels-and-reuse-3-browser-extension-as-the-ux-static-local-fastest-free-implementation)
  - [4. JSON-LD / Linked-Data Publishing (Machine-Readable First)](#run-7-distribution-channels-and-reuse-4-json-ld-linked-data-publishing-machine-readable-first)
    - [Core idea](#run-7-distribution-channels-and-reuse-4-json-ld-linked-data-publishing-machine-readable-first-core-idea)
    - [Architecture](#run-7-distribution-channels-and-reuse-4-json-ld-linked-data-publishing-machine-readable-first-architecture)
    - [UX](#run-7-distribution-channels-and-reuse-4-json-ld-linked-data-publishing-machine-readable-first-ux)
    - [ChatGPT usage](#run-7-distribution-channels-and-reuse-4-json-ld-linked-data-publishing-machine-readable-first-chatgpt-usage)
    - [Tradeoffs](#run-7-distribution-channels-and-reuse-4-json-ld-linked-data-publishing-machine-readable-first-tradeoffs)
  - [5. Docs-as-UI with Search-Only Interaction](#run-7-distribution-channels-and-reuse-5-docs-as-ui-with-search-only-interaction)
    - [Core idea](#run-7-distribution-channels-and-reuse-5-docs-as-ui-with-search-only-interaction-core-idea)
    - [Architecture](#run-7-distribution-channels-and-reuse-5-docs-as-ui-with-search-only-interaction-architecture)
    - [UX](#run-7-distribution-channels-and-reuse-5-docs-as-ui-with-search-only-interaction-ux)
    - [Tradeoffs](#run-7-distribution-channels-and-reuse-5-docs-as-ui-with-search-only-interaction-tradeoffs)
  - [6. Read-Only Codespace / Devcontainer (Analysis Without Setup)](#run-7-distribution-channels-and-reuse-6-read-only-codespace-devcontainer-analysis-without-setup)
    - [Core idea](#run-7-distribution-channels-and-reuse-6-read-only-codespace-devcontainer-analysis-without-setup-core-idea)
    - [Architecture](#run-7-distribution-channels-and-reuse-6-read-only-codespace-devcontainer-analysis-without-setup-architecture)
    - [UX](#run-7-distribution-channels-and-reuse-6-read-only-codespace-devcontainer-analysis-without-setup-ux)
    - [Tradeoffs](#run-7-distribution-channels-and-reuse-6-read-only-codespace-devcontainer-analysis-without-setup-tradeoffs)
  - [7. Snapshot Microsites per Release (Disposable, Shareable)](#run-7-distribution-channels-and-reuse-7-snapshot-microsites-per-release-disposable-shareable)
    - [Core idea](#run-7-distribution-channels-and-reuse-7-snapshot-microsites-per-release-disposable-shareable-core-idea)
    - [Architecture](#run-7-distribution-channels-and-reuse-7-snapshot-microsites-per-release-disposable-shareable-architecture)
    - [UX](#run-7-distribution-channels-and-reuse-7-snapshot-microsites-per-release-disposable-shareable-ux)
    - [Tradeoffs](#run-7-distribution-channels-and-reuse-7-snapshot-microsites-per-release-disposable-shareable-tradeoffs)
  - [8. Manual + Semi-Automated Refresh (Distribution-Focused Variant)](#run-7-distribution-channels-and-reuse-8-manual-semi-automated-refresh-distribution-focused-variant)
    - [Pattern](#run-7-distribution-channels-and-reuse-8-manual-semi-automated-refresh-distribution-focused-variant-pattern)
    - [Result](#run-7-distribution-channels-and-reuse-8-manual-semi-automated-refresh-distribution-focused-variant-result)
  - [Bottom Line (New Insight)](#run-7-distribution-channels-and-reuse-bottom-line-new-insight)
- [Run 8 - Guided Interaction and Lowest Operational Risk](#run-8-guided-interaction-and-lowest-operational-risk)
  - [1. Guided Question Trails (Decision Trees, Not Chat)](#run-8-guided-interaction-and-lowest-operational-risk-1-guided-question-trails-decision-trees-not-chat)
    - [Core idea](#run-8-guided-interaction-and-lowest-operational-risk-1-guided-question-trails-decision-trees-not-chat-core-idea)
    - [Architecture](#run-8-guided-interaction-and-lowest-operational-risk-1-guided-question-trails-decision-trees-not-chat-architecture)
    - [UX](#run-8-guided-interaction-and-lowest-operational-risk-1-guided-question-trails-decision-trees-not-chat-ux)
    - [ChatGPT usage (optional)](#run-8-guided-interaction-and-lowest-operational-risk-1-guided-question-trails-decision-trees-not-chat-chatgpt-usage-optional)
    - [Tradeoffs](#run-8-guided-interaction-and-lowest-operational-risk-1-guided-question-trails-decision-trees-not-chat-tradeoffs)
    - [Fastest free implementation](#run-8-guided-interaction-and-lowest-operational-risk-1-guided-question-trails-decision-trees-not-chat-fastest-free-implementation)
  - [2. Constraint-Based Query Builder (Natural Language Without NLP)](#run-8-guided-interaction-and-lowest-operational-risk-2-constraint-based-query-builder-natural-language-without-nlp)
    - [Core idea](#run-8-guided-interaction-and-lowest-operational-risk-2-constraint-based-query-builder-natural-language-without-nlp-core-idea)
    - [Architecture](#run-8-guided-interaction-and-lowest-operational-risk-2-constraint-based-query-builder-natural-language-without-nlp-architecture)
    - [UX](#run-8-guided-interaction-and-lowest-operational-risk-2-constraint-based-query-builder-natural-language-without-nlp-ux)
    - [Why this matters](#run-8-guided-interaction-and-lowest-operational-risk-2-constraint-based-query-builder-natural-language-without-nlp-why-this-matters)
    - [Tradeoffs](#run-8-guided-interaction-and-lowest-operational-risk-2-constraint-based-query-builder-natural-language-without-nlp-tradeoffs)
  - [3. Explainers as the Primary Artifact System](#run-8-guided-interaction-and-lowest-operational-risk-3-explainers-as-the-primary-artifact-system)
    - [Core idea](#run-8-guided-interaction-and-lowest-operational-risk-3-explainers-as-the-primary-artifact-system-core-idea)
    - [Architecture](#run-8-guided-interaction-and-lowest-operational-risk-3-explainers-as-the-primary-artifact-system-architecture)
    - [UX](#run-8-guided-interaction-and-lowest-operational-risk-3-explainers-as-the-primary-artifact-system-ux)
    - [ChatGPT assist](#run-8-guided-interaction-and-lowest-operational-risk-3-explainers-as-the-primary-artifact-system-chatgpt-assist)
    - [Tradeoffs](#run-8-guided-interaction-and-lowest-operational-risk-3-explainers-as-the-primary-artifact-system-tradeoffs)
  - [4. Client-Side What Changed Diff Viewer](#run-8-guided-interaction-and-lowest-operational-risk-4-client-side-what-changed-diff-viewer)
    - [Core idea](#run-8-guided-interaction-and-lowest-operational-risk-4-client-side-what-changed-diff-viewer-core-idea)
    - [Architecture](#run-8-guided-interaction-and-lowest-operational-risk-4-client-side-what-changed-diff-viewer-architecture)
    - [UX](#run-8-guided-interaction-and-lowest-operational-risk-4-client-side-what-changed-diff-viewer-ux)
    - [Tradeoffs](#run-8-guided-interaction-and-lowest-operational-risk-4-client-side-what-changed-diff-viewer-tradeoffs)
  - [5. Single-Page Board View (Opinionated, Read-Only)](#run-8-guided-interaction-and-lowest-operational-risk-5-single-page-board-view-opinionated-read-only)
    - [Core idea](#run-8-guided-interaction-and-lowest-operational-risk-5-single-page-board-view-opinionated-read-only-core-idea)
    - [Architecture](#run-8-guided-interaction-and-lowest-operational-risk-5-single-page-board-view-opinionated-read-only-architecture)
    - [UX](#run-8-guided-interaction-and-lowest-operational-risk-5-single-page-board-view-opinionated-read-only-ux)
    - [ChatGPT usage](#run-8-guided-interaction-and-lowest-operational-risk-5-single-page-board-view-opinionated-read-only-chatgpt-usage)
    - [Tradeoffs](#run-8-guided-interaction-and-lowest-operational-risk-5-single-page-board-view-opinionated-read-only-tradeoffs)
  - [6. Form-Factor-Specific UX (Mobile-First, Desktop-Second)](#run-8-guided-interaction-and-lowest-operational-risk-6-form-factor-specific-ux-mobile-first-desktop-second)
    - [Core idea](#run-8-guided-interaction-and-lowest-operational-risk-6-form-factor-specific-ux-mobile-first-desktop-second-core-idea)
    - [Architecture](#run-8-guided-interaction-and-lowest-operational-risk-6-form-factor-specific-ux-mobile-first-desktop-second-architecture)
    - [UX](#run-8-guided-interaction-and-lowest-operational-risk-6-form-factor-specific-ux-mobile-first-desktop-second-ux)
    - [Tradeoffs](#run-8-guided-interaction-and-lowest-operational-risk-6-form-factor-specific-ux-mobile-first-desktop-second-tradeoffs)
  - [7. Zero-JS Fallback Mode (Graceful Degradation)](#run-8-guided-interaction-and-lowest-operational-risk-7-zero-js-fallback-mode-graceful-degradation)
    - [Core idea](#run-8-guided-interaction-and-lowest-operational-risk-7-zero-js-fallback-mode-graceful-degradation-core-idea)
    - [Architecture](#run-8-guided-interaction-and-lowest-operational-risk-7-zero-js-fallback-mode-graceful-degradation-architecture)
    - [UX](#run-8-guided-interaction-and-lowest-operational-risk-7-zero-js-fallback-mode-graceful-degradation-ux)
    - [Tradeoffs](#run-8-guided-interaction-and-lowest-operational-risk-7-zero-js-fallback-mode-graceful-degradation-tradeoffs)
  - [8. Manual Refresh With Explicit Effective Date Labels](#run-8-guided-interaction-and-lowest-operational-risk-8-manual-refresh-with-explicit-effective-date-labels)
    - [Core idea](#run-8-guided-interaction-and-lowest-operational-risk-8-manual-refresh-with-explicit-effective-date-labels-core-idea)
    - [Architecture](#run-8-guided-interaction-and-lowest-operational-risk-8-manual-refresh-with-explicit-effective-date-labels-architecture)
    - [UX](#run-8-guided-interaction-and-lowest-operational-risk-8-manual-refresh-with-explicit-effective-date-labels-ux)
    - [Tradeoffs](#run-8-guided-interaction-and-lowest-operational-risk-8-manual-refresh-with-explicit-effective-date-labels-tradeoffs)
  - [Bottom Line (New Insight)](#run-8-guided-interaction-and-lowest-operational-risk-bottom-line-new-insight)

---

<a id="run-1-core-zero-cost-stack-and-static-dashboards"></a>
# Run 1 - Core Zero-Cost Stack and Static Dashboards

A strictly free architecture map for letting Tricia explore Clearlane Dossier artifacts and IRS Form 990 data using only no-cost tools. Everything below works with static hosting, public repos, or local-only usage and avoids paid APIs, servers, or subscriptions.

<a id="run-1-core-zero-cost-stack-and-static-dashboards-1-baseline-principle-why-this-works-free"></a>
## 1. Baseline Principle (Why This Works Free)

Leverage comes from pre-structuring data once and letting the browser do the work.

- Pre-structure data once (JSON / CSV / Markdown)
- Let the browser compute and render (JS + static files)
- Use ChatGPT as a thinking layer, not an API dependency
- Host on GitHub Pages (no backend, no secrets, no runtime costs)

<a id="run-1-core-zero-cost-stack-and-static-dashboards-2-core-zero-cost-stack-recommended-default"></a>
## 2. Core Zero-Cost Stack (Recommended Default)

<a id="run-1-core-zero-cost-stack-and-static-dashboards-2-core-zero-cost-stack-recommended-default-infrastructure"></a>
### Infrastructure

- GitHub repo
- GitHub Pages for static hosting
- Browser-only JavaScript (no Node, no server)

<a id="run-1-core-zero-cost-stack-and-static-dashboards-2-core-zero-cost-stack-recommended-default-data-formats"></a>
### Data formats

- clearlane/*.json - normalized dossier artifacts
- irs990/*.json or .csv - extracted Form 990 fields
- index.md - human-readable narrative + links

<a id="run-1-core-zero-cost-stack-and-static-dashboards-2-core-zero-cost-stack-recommended-default-ux-outcome"></a>
### UX outcome

- Phone-friendly static site
- Click -> question -> answer + chart
- No login required

<a id="run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2"></a>
## 3. Architecture Patterns (Pick 1-2)

<a id="run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-a-question-answer-cards-fastest-to-ship"></a>
### A. Question -> Answer Cards (Fastest to Ship)

<a id="run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-a-question-answer-cards-fastest-to-ship-how-it-works"></a>
#### How it works

- Predefine 20-50 common questions (funding sources, expenses YoY, etc.)
- Each question maps to a JS function, a chart spec, and a short Markdown explanation

<a id="run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-a-question-answer-cards-fastest-to-ship-tech"></a>
#### Tech

- Vanilla JS
- Chart.js (free CDN)
- JSON data

<a id="run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-a-question-answer-cards-fastest-to-ship-ux"></a>
#### UX

- Big buttons
- One tap = answer + visual
- Works well on phone

<a id="run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-a-question-answer-cards-fastest-to-ship-tradeoffs"></a>
#### Tradeoffs

- No free-text queries
- Requires upfront curation (stable once done)

<a id="run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-a-question-answer-cards-fastest-to-ship-why-it-is-ideal-for-tricia"></a>
#### Why it is ideal for Tricia

- No learning curve
- Predictable outputs
- Avoids bad AI answers

<a id="run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-b-markdown-driven-living-report-dashboard"></a>
### B. Markdown-Driven Living Report Dashboard

<a id="run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-b-markdown-driven-living-report-dashboard-how-it-works"></a>
#### How it works

- Markdown pages embed charts via JS
- Sections read like a report (Overview, Financials, Relationships, Timeline)

<a id="run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-b-markdown-driven-living-report-dashboard-tech"></a>
#### Tech

- GitHub Pages
- Jekyll (default) or plain HTML
- CSV -> JS -> charts

<a id="run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-b-markdown-driven-living-report-dashboard-ux"></a>
#### UX

- Scrollable narrative
- Embedded visuals
- Bookmarkable sections

<a id="run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-b-markdown-driven-living-report-dashboard-tradeoffs"></a>
#### Tradeoffs

- Not conversational
- Updates require GitHub commit

<a id="run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-b-markdown-driven-living-report-dashboard-strength"></a>
#### Strength

- Extremely durable
- Great leave-behind artifact

<a id="run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-c-client-side-chat-like-query-layer-free-but-structured"></a>
### C. Client-Side Chat-Like Query Layer (Free but Structured)

<a id="run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-c-client-side-chat-like-query-layer-free-but-structured-important-constraint"></a>
#### Important constraint

- No free, unlimited ChatGPT API calls. The chat must be structured, not generative.

<a id="run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-c-client-side-chat-like-query-layer-free-but-structured-how-it-works"></a>
#### How it works

- Input box accepts natural-ish language
- JS matches intent to predefined queries, filters, and aggregations
- Response renders as explanation + chart/table

<a id="run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-c-client-side-chat-like-query-layer-free-but-structured-example"></a>
#### Example

- User types: "Show revenue trends after 2020"
- System matches keywords/date, runs aggregation, displays chart

<a id="run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-c-client-side-chat-like-query-layer-free-but-structured-tech"></a>
#### Tech

- Simple keyword matching or Lunr.js
- Chart.js or Vega-Lite
- JSON data

<a id="run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-c-client-side-chat-like-query-layer-free-but-structured-tradeoffs"></a>
#### Tradeoffs

- Not true AI
- But feels conversational and is deterministic

<a id="run-1-core-zero-cost-stack-and-static-dashboards-3-architecture-patterns-pick-1-2-c-client-side-chat-like-query-layer-free-but-structured-why-it-is-acceptable"></a>
#### Why it is acceptable

- Predictable
- Explainable
- No hallucinations

<a id="run-1-core-zero-cost-stack-and-static-dashboards-4-using-chatgpt-free-without-an-api"></a>
## 4. Using ChatGPT (Free) Without an API

<a id="run-1-core-zero-cost-stack-and-static-dashboards-4-using-chatgpt-free-without-an-api-pattern-bring-your-own-context-ai-assist"></a>
### Pattern - Bring Your Own Context AI Assist

<a id="run-1-core-zero-cost-stack-and-static-dashboards-4-using-chatgpt-free-without-an-api-pattern-bring-your-own-context-ai-assist-flow"></a>
#### Flow

- Site provides: download dataset / copy summary
- Tricia pastes into ChatGPT (free UI)
- Prompt templates guide analysis (funding concentration, risk signals, etc.)

<a id="run-1-core-zero-cost-stack-and-static-dashboards-4-using-chatgpt-free-without-an-api-pattern-bring-your-own-context-ai-assist-why-this-matters"></a>
#### Why this matters

- Zero cost
- No keys
- No maintenance
- ChatGPT optional, not required

<a id="run-1-core-zero-cost-stack-and-static-dashboards-4-using-chatgpt-free-without-an-api-pattern-bring-your-own-context-ai-assist-ux-trick"></a>
#### UX trick

- Add a Copy for AI button that copies curated JSON/Markdown plus a ready-to-use prompt

<a id="run-1-core-zero-cost-stack-and-static-dashboards-5-visuals-you-can-generate-100-free"></a>
## 5. Visuals You Can Generate 100% Free

- Bar charts (revenue, expenses)
- Line charts (multi-year trends)
- Pie charts (funding sources)
- Timelines (filings, leadership changes)
- Simple relationship maps (SVG)

All browser-rendered. No server.

<a id="run-1-core-zero-cost-stack-and-static-dashboards-6-data-refresh-paths-no-automation-costs"></a>
## 6. Data Refresh Paths (No Automation Costs)

<a id="run-1-core-zero-cost-stack-and-static-dashboards-6-data-refresh-paths-no-automation-costs-manual-but-clean"></a>
### Manual but Clean

- Drop new 990 CSV into repo
- GitHub Pages rebuilds automatically

<a id="run-1-core-zero-cost-stack-and-static-dashboards-6-data-refresh-paths-no-automation-costs-semi-automated-still-free"></a>
### Semi-Automated (Still Free)

- GitHub Actions (free tier)
- Scheduled script pulls IRS bulk data, normalizes fields, commits JSON

<a id="run-1-core-zero-cost-stack-and-static-dashboards-7-recommended-leave-behind-package"></a>
## 7. Recommended Leave-Behind Package

- GitHub repo
- Live GitHub Pages URL
- /data folder (human-readable)
- /questions folder (documented logic)
- README: how to update data, ask questions, and use ChatGPT with this

Goal: no credentials, no dependencies, survives personnel and budget changes.

<a id="run-1-core-zero-cost-stack-and-static-dashboards-8-fastest-path-to-a-working-demo-1-2-days"></a>
## 8. Fastest Path to a Working Demo (1-2 Days)

<a id="run-1-core-zero-cost-stack-and-static-dashboards-8-fastest-path-to-a-working-demo-1-2-days-day-1"></a>
### Day 1

- Normalize Clearlane + 990 into JSON
- Build 10 question cards
- Deploy GitHub Pages

<a id="run-1-core-zero-cost-stack-and-static-dashboards-8-fastest-path-to-a-working-demo-1-2-days-day-2"></a>
### Day 2

- Add charts
- Add Copy for AI buttons
- Mobile polish

<a id="run-1-core-zero-cost-stack-and-static-dashboards-bottom-line"></a>
## Bottom Line

Most reliable free solution is not a live AI system. It is a static, explainable, question-driven dashboard that optionally pairs with ChatGPT free UI.

<a id="run-2-local-first-and-prompt-backed-patterns"></a>
# Run 2 - Local-First and Prompt-Backed Patterns

A set of strictly free architectures that extend beyond the baseline, focusing on interaction patterns, durability, and ask-a-question affordances without relying on paid APIs, servers, or fragile tooling.

<a id="run-2-local-first-and-prompt-backed-patterns-1-local-first-ai-companion-zero-hosting-dependency"></a>
## 1. Local-First AI Companion (Zero Hosting Dependency)

<a id="run-2-local-first-and-prompt-backed-patterns-1-local-first-ai-companion-zero-hosting-dependency-what-is-new-here"></a>
### What is new here

- Instead of hosting intelligence, you ship intelligence.

<a id="run-2-local-first-and-prompt-backed-patterns-1-local-first-ai-companion-zero-hosting-dependency-architecture"></a>
### Architecture

- GitHub repo contains Clearlane + 990 data (CSV/JSON) and a static HTML app
- User opens index.html locally (no internet required)
- Optional ChatGPT usage is manual copy/paste

<a id="run-2-local-first-and-prompt-backed-patterns-1-local-first-ai-companion-zero-hosting-dependency-ux"></a>
### UX

- Search bar + filters
- Buttons like Summarize this section / Explain anomalies that copy curated data slices + prompts

<a id="run-2-local-first-and-prompt-backed-patterns-1-local-first-ai-companion-zero-hosting-dependency-why-this-matters"></a>
### Why this matters

- Survives hosting changes
- Works offline
- No browser security issues with local data

<a id="run-2-local-first-and-prompt-backed-patterns-1-local-first-ai-companion-zero-hosting-dependency-tradeoffs"></a>
### Tradeoffs

- No live chat, but very future-proof

<a id="run-2-local-first-and-prompt-backed-patterns-1-local-first-ai-companion-zero-hosting-dependency-fastest-free-implementation"></a>
### Fastest free implementation

- 1 HTML file
- 1 JS file
- No build step

<a id="run-2-local-first-and-prompt-backed-patterns-2-prompt-backed-dashboard-chatgpt-as-a-brain-not-a-backend"></a>
## 2. Prompt-Backed Dashboard (ChatGPT as a Brain, Not a Backend)

<a id="run-2-local-first-and-prompt-backed-patterns-2-prompt-backed-dashboard-chatgpt-as-a-brain-not-a-backend-core-idea"></a>
### Core idea

- Every insight has a paired prompt, not a paired API call.

<a id="run-2-local-first-and-prompt-backed-patterns-2-prompt-backed-dashboard-chatgpt-as-a-brain-not-a-backend-architecture"></a>
### Architecture

- GitHub Pages static site
- Each chart card includes a visualization and an Ask AI about this button

<a id="run-2-local-first-and-prompt-backed-patterns-2-prompt-backed-dashboard-chatgpt-as-a-brain-not-a-backend-button-behavior"></a>
### Button behavior

- Copies context + compressed table + task prompt for analysis; user pastes into ChatGPT free UI

<a id="run-2-local-first-and-prompt-backed-patterns-2-prompt-backed-dashboard-chatgpt-as-a-brain-not-a-backend-why-this-is-different"></a>
### Why this is different

- Standardizes how AI is used
- Consistent, explainable answers
- Less hallucination via complete context

<a id="run-2-local-first-and-prompt-backed-patterns-2-prompt-backed-dashboard-chatgpt-as-a-brain-not-a-backend-tradeoffs"></a>
### Tradeoffs

- Requires user action, but avoids automation fragility

<a id="run-2-local-first-and-prompt-backed-patterns-3-static-question-router-feels-like-chat-is-not"></a>
## 3. Static Question Router (Feels Like Chat, Is Not)

<a id="run-2-local-first-and-prompt-backed-patterns-3-static-question-router-feels-like-chat-is-not-what-is-new"></a>
### What is new

- A routing layer that makes static data feel conversational.

<a id="run-2-local-first-and-prompt-backed-patterns-3-static-question-router-feels-like-chat-is-not-architecture"></a>
### Architecture

- Single input box
- JS intent classifier (keywords, dates, financial terms)
- Routes question to known query module

<a id="run-2-local-first-and-prompt-backed-patterns-3-static-question-router-feels-like-chat-is-not-example"></a>
### Example

- Input: "How dependent is funding on one source?"
- Routes to funding_concentration.js, runs aggregation, displays chart + explanation

<a id="run-2-local-first-and-prompt-backed-patterns-3-static-question-router-feels-like-chat-is-not-why-it-works"></a>
### Why it works

- Most real questions are repetitive
- Deterministic answers > generative ones

<a id="run-2-local-first-and-prompt-backed-patterns-3-static-question-router-feels-like-chat-is-not-tradeoffs"></a>
### Tradeoffs

- Limited vocabulary, but extremely trustworthy

<a id="run-2-local-first-and-prompt-backed-patterns-4-github-issues-as-a-question-log"></a>
## 4. GitHub Issues as a Question Log

<a id="run-2-local-first-and-prompt-backed-patterns-4-github-issues-as-a-question-log-underused-but-powerful"></a>
### Underused but powerful

<a id="run-2-local-first-and-prompt-backed-patterns-4-github-issues-as-a-question-log-architecture"></a>
### Architecture

- Public GitHub repo with Issues enabled
- Each issue = a question
- Issue templates include question + data slice links + suggested ChatGPT prompt

<a id="run-2-local-first-and-prompt-backed-patterns-4-github-issues-as-a-question-log-ux"></a>
### UX

- Tricia opens an issue, pastes question, uses prompt in ChatGPT, posts summary back into issue

<a id="run-2-local-first-and-prompt-backed-patterns-4-github-issues-as-a-question-log-why-this-is-clever"></a>
### Why this is clever

- Institutional memory
- Zero extra UI
- Searchable forever

<a id="run-2-local-first-and-prompt-backed-patterns-4-github-issues-as-a-question-log-tradeoffs"></a>
### Tradeoffs

- Not flashy, but near-zero maintenance

<a id="run-2-local-first-and-prompt-backed-patterns-5-markdown-only-intelligence-no-js-required"></a>
## 5. Markdown-Only Intelligence (No JS Required)

<a id="run-2-local-first-and-prompt-backed-patterns-5-markdown-only-intelligence-no-js-required-for-maximum-longevity"></a>
### For maximum longevity

<a id="run-2-local-first-and-prompt-backed-patterns-5-markdown-only-intelligence-no-js-required-architecture"></a>
### Architecture

- Markdown files only
- Tables + narrative
- Mermaid diagrams rendered by GitHub

<a id="run-2-local-first-and-prompt-backed-patterns-5-markdown-only-intelligence-no-js-required-enhancements"></a>
### Enhancements

- Each section ends with an AI prompt and key metrics table

<a id="run-2-local-first-and-prompt-backed-patterns-5-markdown-only-intelligence-no-js-required-why-this-matters"></a>
### Why this matters

- Markdown survives frameworks
- GitHub renders it reliably
- Zero attack surface

<a id="run-2-local-first-and-prompt-backed-patterns-5-markdown-only-intelligence-no-js-required-tradeoffs"></a>
### Tradeoffs

- No interactivity, but absolute reliability

<a id="run-2-local-first-and-prompt-backed-patterns-6-semi-automated-refresh-still-free"></a>
## 6. Semi-Automated Refresh (Still Free)

<a id="run-2-local-first-and-prompt-backed-patterns-6-semi-automated-refresh-still-free-github-actions-pattern"></a>
### GitHub Actions pattern

- Scheduled job pulls IRS bulk 990 data, normalizes to repo schema, commits JSON

<a id="run-2-local-first-and-prompt-backed-patterns-6-semi-automated-refresh-still-free-output"></a>
### Output

- Static site updates automatically
- No third-party services

<a id="run-2-local-first-and-prompt-backed-patterns-6-semi-automated-refresh-still-free-risk-note"></a>
### Risk note

- IRS schema changes require manual review; failure mode is no update, not breakage

<a id="run-2-local-first-and-prompt-backed-patterns-7-what-to-leave-behind-critical"></a>
## 7. What to Leave Behind (Critical)

- Static site URL
- GitHub repo
- /data folder with comments
- /prompts folder (plain text)
- README: how to update, ask questions, and use ChatGPT responsibly

No credentials. No dependencies. No single point of failure.

<a id="run-2-local-first-and-prompt-backed-patterns-bottom-line-new-insight"></a>
## Bottom Line (New Insight)

Optimal free architecture is AI-assisted, not AI-dependent: a thinking surface that structures questions and constrains answers, with AI as an optional amplifier.

<a id="run-3-governance-explainability-and-handoff-resilience"></a>
# Run 3 - Governance, Explainability, and Handoff Resilience

Strictly free architectures emphasizing governance safety, explainability, and handoff resilience with no servers, credentials, or automation dependencies beyond GitHub.

<a id="run-3-governance-explainability-and-handoff-resilience-1-schema-first-explorer-data-before-ui"></a>
## 1. Schema-First Explorer (Data Before UI)

<a id="run-3-governance-explainability-and-handoff-resilience-1-schema-first-explorer-data-before-ui-core-idea"></a>
### Core idea

- Lock the data contract first, then let multiple free UIs emerge around it.

<a id="run-3-governance-explainability-and-handoff-resilience-1-schema-first-explorer-data-before-ui-architecture"></a>
### Architecture

- GitHub repo defines clearlane.schema.json and irs990.schema.json
- Datasets validated against JSON Schema
- GitHub Pages renders tables, charts, and schema documentation

<a id="run-3-governance-explainability-and-handoff-resilience-1-schema-first-explorer-data-before-ui-ux"></a>
### UX

- Browse meaningful fields, not raw rows
- Tooltips explain origin/meaning
- Click field -> see derived insights

<a id="run-3-governance-explainability-and-handoff-resilience-1-schema-first-explorer-data-before-ui-why-this-is-new"></a>
### Why this is new

- Starts with semantic stability to prevent silent drift

<a id="run-3-governance-explainability-and-handoff-resilience-1-schema-first-explorer-data-before-ui-tradeoffs"></a>
### Tradeoffs

- More upfront modeling, less wow, more trust

<a id="run-3-governance-explainability-and-handoff-resilience-1-schema-first-explorer-data-before-ui-fastest-free-implementation"></a>
### Fastest free implementation

- JSON Schema
- Static schema viewer
- Chart.js

<a id="run-3-governance-explainability-and-handoff-resilience-2-decision-notebook-questions-as-first-class-objects"></a>
## 2. Decision Notebook (Questions as First-Class Objects)

<a id="run-3-governance-explainability-and-handoff-resilience-2-decision-notebook-questions-as-first-class-objects-core-idea"></a>
### Core idea

- Make the system decision-centric rather than data-centric.

<a id="run-3-governance-explainability-and-handoff-resilience-2-decision-notebook-questions-as-first-class-objects-architecture"></a>
### Architecture

- Markdown files like decisions/001-funding-risk.md
- Each includes question, data references, computation logic, and embedded charts

<a id="run-3-governance-explainability-and-handoff-resilience-2-decision-notebook-questions-as-first-class-objects-ux"></a>
### UX

- Reads like a briefing book
- Each page answers one question completely

<a id="run-3-governance-explainability-and-handoff-resilience-2-decision-notebook-questions-as-first-class-objects-chatgpt-usage-free-ui"></a>
### ChatGPT usage (free UI)

- Each decision ends with a prompt: paste section into ChatGPT for alternative interpretations

<a id="run-3-governance-explainability-and-handoff-resilience-2-decision-notebook-questions-as-first-class-objects-why-this-works"></a>
### Why this works

- Executives think in decisions, not dashboards; Markdown survives

<a id="run-3-governance-explainability-and-handoff-resilience-2-decision-notebook-questions-as-first-class-objects-tradeoffs"></a>
### Tradeoffs

- No ad-hoc exploration; requires editorial discipline

<a id="run-3-governance-explainability-and-handoff-resilience-3-explainable-metric-library-anti-black-box"></a>
## 3. Explainable Metric Library (Anti-Black-Box)

<a id="run-3-governance-explainability-and-handoff-resilience-3-explainable-metric-library-anti-black-box-core-idea"></a>
### Core idea

- Every metric is transparent, inspectable, and reusable.

<a id="run-3-governance-explainability-and-handoff-resilience-3-explainable-metric-library-anti-black-box-architecture"></a>
### Architecture

- /metrics folder with one file per metric
- Each metric includes definition, formula, source fields, limitations, and chart example

<a id="run-3-governance-explainability-and-handoff-resilience-3-explainable-metric-library-anti-black-box-ux"></a>
### UX

- Metric browser
- Click metric -> chart + narrative + raw numbers

<a id="run-3-governance-explainability-and-handoff-resilience-3-explainable-metric-library-anti-black-box-why-it-is-different"></a>
### Why it is different

- Eliminates confusion about meaning; good for regulated contexts

<a id="run-3-governance-explainability-and-handoff-resilience-3-explainable-metric-library-anti-black-box-tradeoffs"></a>
### Tradeoffs

- Slower to build initially, strong governance payoff

<a id="run-3-governance-explainability-and-handoff-resilience-4-browser-only-pivot-table-interface"></a>
## 4. Browser-Only Pivot Table Interface

<a id="run-3-governance-explainability-and-handoff-resilience-4-browser-only-pivot-table-interface-core-idea"></a>
### Core idea

- Let the browser do what Excel does without Excel.

<a id="run-3-governance-explainability-and-handoff-resilience-4-browser-only-pivot-table-interface-architecture"></a>
### Architecture

- Static HTML + JS
- CSV committed to repo
- Client-side pivot logic (rows, columns, filters)

<a id="run-3-governance-explainability-and-handoff-resilience-4-browser-only-pivot-table-interface-ux"></a>
### UX

- Drag-and-drop fields
- Instant aggregations
- Export view as CSV or image

<a id="run-3-governance-explainability-and-handoff-resilience-4-browser-only-pivot-table-interface-chatgpt-assist-optional"></a>
### ChatGPT assist (optional)

- Copy summary + pivot output and paste into ChatGPT for analysis

<a id="run-3-governance-explainability-and-handoff-resilience-4-browser-only-pivot-table-interface-tradeoffs"></a>
### Tradeoffs

- No natural language input; powerful for analysts

<a id="run-3-governance-explainability-and-handoff-resilience-5-narrated-timeline-temporal-sensemaking"></a>
## 5. Narrated Timeline (Temporal Sensemaking)

<a id="run-3-governance-explainability-and-handoff-resilience-5-narrated-timeline-temporal-sensemaking-core-idea"></a>
### Core idea

- Make time the primary axis; most risk is temporal.

<a id="run-3-governance-explainability-and-handoff-resilience-5-narrated-timeline-temporal-sensemaking-architecture"></a>
### Architecture

- Timeline JSON: filings, leadership changes, revenue inflections
- Static timeline component on GitHub Pages

<a id="run-3-governance-explainability-and-handoff-resilience-5-narrated-timeline-temporal-sensemaking-ux"></a>
### UX

- Scrollable timeline
- Expandable events
- Charts update as you scrub time

<a id="run-3-governance-explainability-and-handoff-resilience-5-narrated-timeline-temporal-sensemaking-why-this-matters"></a>
### Why this matters

- Humans reason about change better than totals; strong storytelling value

<a id="run-3-governance-explainability-and-handoff-resilience-5-narrated-timeline-temporal-sensemaking-tradeoffs"></a>
### Tradeoffs

- Less flexible than dashboards

<a id="run-3-governance-explainability-and-handoff-resilience-6-zero-cost-refresh-strategy-new-angle"></a>
## 6. Zero-Cost Refresh Strategy (New Angle)

<a id="run-3-governance-explainability-and-handoff-resilience-6-zero-cost-refresh-strategy-new-angle-pattern-human-in-the-loop-updates"></a>
### Pattern - Human-in-the-Loop Updates

- New 990 data added via PR
- PR template requires summary, anomalies, validation checklist
- GitHub history becomes an audit log

<a id="run-3-governance-explainability-and-handoff-resilience-7-minimal-ai-boundary-rule-critical"></a>
## 7. Minimal AI Boundary Rule (Critical)

- Use ChatGPT only for summarization, alternative explanations, and narrative framing
- Never use ChatGPT for calculations, primary facts, or derived metrics

This preserves trust and avoids AI dependency.

<a id="run-3-governance-explainability-and-handoff-resilience-bottom-line-new-insight"></a>
## Bottom Line (New Insight)

Strong free systems optimize for interpretive stability (schemas, decisions, metrics, timelines) so AI can augment understanding without becoming a dependency.

<a id="run-4-browser-side-analytics-and-transparent-querying"></a>
# Run 4 - Browser-Side Analytics and Transparent Querying

Strictly free architectures emphasizing query power, transparency, and operability with computation moved to the browser and no backend services.

<a id="run-4-browser-side-analytics-and-transparent-querying-1-browser-embedded-analytics-engine-duckdb-wasm"></a>
## 1. Browser-Embedded Analytics Engine (DuckDB-Wasm)

<a id="run-4-browser-side-analytics-and-transparent-querying-1-browser-embedded-analytics-engine-duckdb-wasm-core-idea"></a>
### Core idea

- Run real analytics entirely in the browser: no backend, no API, no cost.

<a id="run-4-browser-side-analytics-and-transparent-querying-1-browser-embedded-analytics-engine-duckdb-wasm-architecture"></a>
### Architecture

- Static site on GitHub Pages
- Data shipped as CSV/Parquet
- DuckDB-Wasm executes SQL client-side
- Charts rendered with Vega-Lite

<a id="run-4-browser-side-analytics-and-transparent-querying-1-browser-embedded-analytics-engine-duckdb-wasm-ux"></a>
### UX

- SQL editor (presets + editable)
- Dropdowns for common queries
- Instant charted results

<a id="run-4-browser-side-analytics-and-transparent-querying-1-browser-embedded-analytics-engine-duckdb-wasm-why-this-is-new"></a>
### Why this is new

- True ad-hoc analysis without servers; deterministic results

<a id="run-4-browser-side-analytics-and-transparent-querying-1-browser-embedded-analytics-engine-duckdb-wasm-tradeoffs"></a>
### Tradeoffs

- Heavier initial load; SQL literacy helps (presets mitigate)

<a id="run-4-browser-side-analytics-and-transparent-querying-1-browser-embedded-analytics-engine-duckdb-wasm-fastest-free-implementation"></a>
### Fastest free implementation

- Static HTML
- DuckDB-Wasm CDN
- Vega-Lite JSON specs

<a id="run-4-browser-side-analytics-and-transparent-querying-2-static-sql-as-documentation-dashboard"></a>
## 2. Static SQL-as-Documentation Dashboard

<a id="run-4-browser-side-analytics-and-transparent-querying-2-static-sql-as-documentation-dashboard-core-idea"></a>
### Core idea

- Every insight is backed by visible SQL, not hidden logic.

<a id="run-4-browser-side-analytics-and-transparent-querying-2-static-sql-as-documentation-dashboard-architecture"></a>
### Architecture

- Markdown pages with question + SQL query (executed client-side) + result table + chart

<a id="run-4-browser-side-analytics-and-transparent-querying-2-static-sql-as-documentation-dashboard-ux"></a>
### UX

- Scrollable report
- Readers can inspect exact computations
- Copy SQL for reuse

<a id="run-4-browser-side-analytics-and-transparent-querying-2-static-sql-as-documentation-dashboard-chatgpt-usage-free-ui"></a>
### ChatGPT usage (free UI)

- Copy button: Explain this query and result (complete context)

<a id="run-4-browser-side-analytics-and-transparent-querying-2-static-sql-as-documentation-dashboard-tradeoffs"></a>
### Tradeoffs

- Less friendly than buttons; extremely auditable

<a id="run-4-browser-side-analytics-and-transparent-querying-3-csv-first-explorer-with-web-metadata-csvw"></a>
## 3. CSV-First Explorer with Web Metadata (CSVW)

<a id="run-4-browser-side-analytics-and-transparent-querying-3-csv-first-explorer-with-web-metadata-csvw-core-idea"></a>
### Core idea

- Make CSVs self-describing so any tool can understand them.

<a id="run-4-browser-side-analytics-and-transparent-querying-3-csv-first-explorer-with-web-metadata-csvw-architecture"></a>
### Architecture

- CSV files + CSVW metadata (JSON)
- Pages render tables/charts and pull field descriptions from metadata

<a id="run-4-browser-side-analytics-and-transparent-querying-3-csv-first-explorer-with-web-metadata-csvw-ux"></a>
### UX

- Click column -> definition, source, caveats
- Client-side filters and sorts

<a id="run-4-browser-side-analytics-and-transparent-querying-3-csv-first-explorer-with-web-metadata-csvw-why-this-matters"></a>
### Why this matters

- Interoperable with Excel/R/Python; zero lock-in

<a id="run-4-browser-side-analytics-and-transparent-querying-3-csv-first-explorer-with-web-metadata-csvw-tradeoffs"></a>
### Tradeoffs

- Less flashy; very strong interoperability

<a id="run-4-browser-side-analytics-and-transparent-querying-4-github-discussions-as-the-primary-ux"></a>
## 4. GitHub Discussions as the Primary UX

<a id="run-4-browser-side-analytics-and-transparent-querying-4-github-discussions-as-the-primary-ux-core-idea"></a>
### Core idea

- Use GitHub itself as the interface: no custom app required.

<a id="run-4-browser-side-analytics-and-transparent-querying-4-github-discussions-as-the-primary-ux-architecture"></a>
### Architecture

- Repo with Discussions enabled
- Categories: Questions, Findings, Data Updates

<a id="run-4-browser-side-analytics-and-transparent-querying-4-github-discussions-as-the-primary-ux-ux"></a>
### UX

- Each discussion links to data files, charts, and prompt templates

<a id="run-4-browser-side-analytics-and-transparent-querying-4-github-discussions-as-the-primary-ux-why-it-is-different"></a>
### Why it is different

- Zero UI code; built-in search/threading/history; knowledge base

<a id="run-4-browser-side-analytics-and-transparent-querying-4-github-discussions-as-the-primary-ux-tradeoffs"></a>
### Tradeoffs

- Not visual-first; relies on GitHub familiarity

<a id="run-4-browser-side-analytics-and-transparent-querying-5-observable-style-notebooks-exported-static"></a>
## 5. Observable-Style Notebooks, Exported Static

<a id="run-4-browser-side-analytics-and-transparent-querying-5-observable-style-notebooks-exported-static-core-idea"></a>
### Core idea

- Exploratory notebooks -> frozen static artifacts.

<a id="run-4-browser-side-analytics-and-transparent-querying-5-observable-style-notebooks-exported-static-architecture"></a>
### Architecture

- Free public notebooks (JS + data)
- Export to static HTML
- Host on GitHub Pages

<a id="run-4-browser-side-analytics-and-transparent-querying-5-observable-style-notebooks-exported-static-ux"></a>
### UX

- Interactive charts
- Step-by-step narrative
- Sliders and filters

<a id="run-4-browser-side-analytics-and-transparent-querying-5-observable-style-notebooks-exported-static-why-it-is-valuable"></a>
### Why it is valuable

- Excellent for discovery; static export removes runtime dependency

<a id="run-4-browser-side-analytics-and-transparent-querying-5-observable-style-notebooks-exported-static-tradeoffs"></a>
### Tradeoffs

- Notebook authoring discipline required; not ideal for very large data

<a id="run-4-browser-side-analytics-and-transparent-querying-6-service-worker-powered-offline-mode"></a>
## 6. Service-Worker-Powered Offline Mode

<a id="run-4-browser-side-analytics-and-transparent-querying-6-service-worker-powered-offline-mode-core-idea"></a>
### Core idea

- Once loaded, the site works offline.

<a id="run-4-browser-side-analytics-and-transparent-querying-6-service-worker-powered-offline-mode-architecture"></a>
### Architecture

- Service Worker caches data, JS, and chart assets

<a id="run-4-browser-side-analytics-and-transparent-querying-6-service-worker-powered-offline-mode-ux"></a>
### UX

- Load once; use anywhere; ideal for briefings/travel

<a id="run-4-browser-side-analytics-and-transparent-querying-6-service-worker-powered-offline-mode-tradeoffs"></a>
### Tradeoffs

- Cache invalidation complexity

<a id="run-4-browser-side-analytics-and-transparent-querying-7-release-based-data-snapshots-governance-first"></a>
## 7. Release-Based Data Snapshots (Governance-First)

<a id="run-4-browser-side-analytics-and-transparent-querying-7-release-based-data-snapshots-governance-first-core-idea"></a>
### Core idea

- Every dataset version is immutable and referenced.

<a id="run-4-browser-side-analytics-and-transparent-querying-7-release-based-data-snapshots-governance-first-architecture"></a>
### Architecture

- GitHub Releases: v2024-990, v2025-990, etc
- Each includes data, checksum, summary notes

<a id="run-4-browser-side-analytics-and-transparent-querying-7-release-based-data-snapshots-governance-first-ux"></a>
### UX

- Dashboard switches between releases; clear what-changed visibility

<a id="run-4-browser-side-analytics-and-transparent-querying-7-release-based-data-snapshots-governance-first-why-this-is-important"></a>
### Why this is important

- Prevents silent revisions; supports audits and comparisons

<a id="run-4-browser-side-analytics-and-transparent-querying-8-manual-semi-automated-refresh-new-variant"></a>
## 8. Manual + Semi-Automated Refresh (New Variant)

<a id="run-4-browser-side-analytics-and-transparent-querying-8-manual-semi-automated-refresh-new-variant-pattern"></a>
### Pattern

- GitHub Action validates structure and schema only
- Humans approve and merge data PRs
- Pages rebuild automatically

<a id="run-4-browser-side-analytics-and-transparent-querying-8-manual-semi-automated-refresh-new-variant-result"></a>
### Result

- Free, reviewable, no blind automation

<a id="run-4-browser-side-analytics-and-transparent-querying-bottom-line-new-insight"></a>
## Bottom Line (New Insight)

Most powerful zero-cost systems shift computation to the browser and knowledge to versioned artifacts, keeping AI optional as an interpretive layer.

<a id="run-5-progressive-ux-and-ambiguity-reduction"></a>
# Run 5 - Progressive UX and Ambiguity Reduction

Strictly free architectures focusing on progressive disclosure UX, explainability under constraint, and minimal cognitive load.

<a id="run-5-progressive-ux-and-ambiguity-reduction-1-progressive-disclosure-dashboard-beginner-power-user"></a>
## 1. Progressive Disclosure Dashboard (Beginner -> Power User)

<a id="run-5-progressive-ux-and-ambiguity-reduction-1-progressive-disclosure-dashboard-beginner-power-user-core-idea"></a>
### Core idea

- One static site supports multiple sophistication levels.

<a id="run-5-progressive-ux-and-ambiguity-reduction-1-progressive-disclosure-dashboard-beginner-power-user-architecture"></a>
### Architecture

- Static site on GitHub Pages
- Same JSON/CSV data
- Three layers: overview cards, interactive charts, raw tables/exports

<a id="run-5-progressive-ux-and-ambiguity-reduction-1-progressive-disclosure-dashboard-beginner-power-user-ux"></a>
### UX

- Default shows answers; Show details reveals assumptions, calculations, raw numbers

<a id="run-5-progressive-ux-and-ambiguity-reduction-1-progressive-disclosure-dashboard-beginner-power-user-tradeoffs"></a>
### Tradeoffs

- More UI planning upfront; strong usability payoff

<a id="run-5-progressive-ux-and-ambiguity-reduction-1-progressive-disclosure-dashboard-beginner-power-user-fastest-free-implementation"></a>
### Fastest free implementation

- Plain HTML + CSS
- Chart.js
- Simple JS state toggles

<a id="run-5-progressive-ux-and-ambiguity-reduction-2-narrative-first-data-second-briefing-pages"></a>
## 2. Narrative-First, Data-Second Briefing Pages

<a id="run-5-progressive-ux-and-ambiguity-reduction-2-narrative-first-data-second-briefing-pages-core-idea"></a>
### Core idea

- Users read analysis first, then inspect data if needed.

<a id="run-5-progressive-ux-and-ambiguity-reduction-2-narrative-first-data-second-briefing-pages-architecture"></a>
### Architecture

- Markdown pages rendered by GitHub Pages
- Structure: exec summary, key claims, supporting charts, linked sources

<a id="run-5-progressive-ux-and-ambiguity-reduction-2-narrative-first-data-second-briefing-pages-chatgpt-usage-free-ui"></a>
### ChatGPT usage (free UI)

- Each claim includes a copyable prompt: "Challenge or validate this claim using the data below."

<a id="run-5-progressive-ux-and-ambiguity-reduction-2-narrative-first-data-second-briefing-pages-why-this-is-distinct"></a>
### Why this is distinct

- Reverses dashboard flow; anchors meaning first

<a id="run-5-progressive-ux-and-ambiguity-reduction-2-narrative-first-data-second-briefing-pages-tradeoffs"></a>
### Tradeoffs

- Less exploratory; strong clarity/alignment

<a id="run-5-progressive-ux-and-ambiguity-reduction-3-deterministic-why-buttons-no-ai-in-the-loop"></a>
## 3. Deterministic Why Buttons (No AI in the Loop)

<a id="run-5-progressive-ux-and-ambiguity-reduction-3-deterministic-why-buttons-no-ai-in-the-loop-core-idea"></a>
### Core idea

- Anticipate why-questions and answer deterministically.

<a id="run-5-progressive-ux-and-ambiguity-reduction-3-deterministic-why-buttons-no-ai-in-the-loop-architecture"></a>
### Architecture

- Each metric/chart has a Why does this look like this button
- Reveals predefined explanation, contributors, limitations

<a id="run-5-progressive-ux-and-ambiguity-reduction-3-deterministic-why-buttons-no-ai-in-the-loop-ux"></a>
### UX

- No typing; consistent answers; no AI dependency

<a id="run-5-progressive-ux-and-ambiguity-reduction-3-deterministic-why-buttons-no-ai-in-the-loop-optional-chatgpt-assist"></a>
### Optional ChatGPT assist

- Copy block to ask ChatGPT for alternative explanations

<a id="run-5-progressive-ux-and-ambiguity-reduction-3-deterministic-why-buttons-no-ai-in-the-loop-tradeoffs"></a>
### Tradeoffs

- Requires upfront reasoning work; extremely reliable

<a id="run-5-progressive-ux-and-ambiguity-reduction-4-static-faceted-search-browse-like-a-catalog"></a>
## 4. Static Faceted Search (Browse Like a Catalog)

<a id="run-5-progressive-ux-and-ambiguity-reduction-4-static-faceted-search-browse-like-a-catalog-core-idea"></a>
### Core idea

- Users browse via facets instead of asking in natural language.

<a id="run-5-progressive-ux-and-ambiguity-reduction-4-static-faceted-search-browse-like-a-catalog-architecture"></a>
### Architecture

- Static JSON index of topics/entities/years/risk types
- Client-side faceted search UI (checkboxes, sliders)

<a id="run-5-progressive-ux-and-ambiguity-reduction-4-static-faceted-search-browse-like-a-catalog-ux"></a>
### UX

- Filter by year, revenue range, funding concentration; results update instantly

<a id="run-5-progressive-ux-and-ambiguity-reduction-4-static-faceted-search-browse-like-a-catalog-why-it-works"></a>
### Why it works

- Avoids ambiguity; scales with content growth

<a id="run-5-progressive-ux-and-ambiguity-reduction-4-static-faceted-search-browse-like-a-catalog-tradeoffs"></a>
### Tradeoffs

- Not conversational; highly discoverable

<a id="run-5-progressive-ux-and-ambiguity-reduction-5-copy-exactly-this-ai-assist-blocks"></a>
## 5. Copy-Exactly-This AI Assist Blocks

<a id="run-5-progressive-ux-and-ambiguity-reduction-5-copy-exactly-this-ai-assist-blocks-core-idea"></a>
### Core idea

- Remove prompt ambiguity entirely.

<a id="run-5-progressive-ux-and-ambiguity-reduction-5-copy-exactly-this-ai-assist-blocks-architecture"></a>
### Architecture

- Prewritten prompt + bounded data excerpt; user copies verbatim into ChatGPT

<a id="run-5-progressive-ux-and-ambiguity-reduction-5-copy-exactly-this-ai-assist-blocks-ux"></a>
### UX

- No prompt skill required; consistent outputs

<a id="run-5-progressive-ux-and-ambiguity-reduction-5-copy-exactly-this-ai-assist-blocks-tradeoffs"></a>
### Tradeoffs

- Less flexibility; maximum predictability

<a id="run-5-progressive-ux-and-ambiguity-reduction-6-html-only-charts-no-js-libraries"></a>
## 6. HTML-Only Charts (No JS Libraries)

<a id="run-5-progressive-ux-and-ambiguity-reduction-6-html-only-charts-no-js-libraries-core-idea"></a>
### Core idea

- Extreme minimalism for longevity.

<a id="run-5-progressive-ux-and-ambiguity-reduction-6-html-only-charts-no-js-libraries-architecture"></a>
### Architecture

- Pre-rendered SVG charts committed to repo
- Updated only when data changes
- Embedded in Markdown/HTML

<a id="run-5-progressive-ux-and-ambiguity-reduction-6-html-only-charts-no-js-libraries-ux"></a>
### UX

- Instant load; no JS failures

<a id="run-5-progressive-ux-and-ambiguity-reduction-6-html-only-charts-no-js-libraries-tradeoffs"></a>
### Tradeoffs

- No interactivity; manual regeneration required

<a id="run-5-progressive-ux-and-ambiguity-reduction-7-data-as-attachments-model-email-safe-tool-agnostic"></a>
## 7. Data as Attachments Model (Email-Safe, Tool-Agnostic)

<a id="run-5-progressive-ux-and-ambiguity-reduction-7-data-as-attachments-model-email-safe-tool-agnostic-core-idea"></a>
### Core idea

- Treat datasets as immutable attachments, not live feeds.

<a id="run-5-progressive-ux-and-ambiguity-reduction-7-data-as-attachments-model-email-safe-tool-agnostic-architecture"></a>
### Architecture

- Each release includes ZIP of CSV/JSON plus static HTML viewer

<a id="run-5-progressive-ux-and-ambiguity-reduction-7-data-as-attachments-model-email-safe-tool-agnostic-ux"></a>
### UX

- Download once; works offline; share via email/file transfer

<a id="run-5-progressive-ux-and-ambiguity-reduction-7-data-as-attachments-model-email-safe-tool-agnostic-tradeoffs"></a>
### Tradeoffs

- No live updates; very resilient

<a id="run-5-progressive-ux-and-ambiguity-reduction-8-human-readable-change-logs-often-missing-very-valuable"></a>
## 8. Human-Readable Change Logs (Often Missing, Very Valuable)

<a id="run-5-progressive-ux-and-ambiguity-reduction-8-human-readable-change-logs-often-missing-very-valuable-core-idea"></a>
### Core idea

- Every data change is explained in plain language.

<a id="run-5-progressive-ux-and-ambiguity-reduction-8-human-readable-change-logs-often-missing-very-valuable-architecture"></a>
### Architecture

- CHANGELOG.md per dataset with what changed, why, and impact on metrics

<a id="run-5-progressive-ux-and-ambiguity-reduction-8-human-readable-change-logs-often-missing-very-valuable-ux"></a>
### UX

- Builds trust; prevents confusion over shifting numbers

<a id="run-5-progressive-ux-and-ambiguity-reduction-8-human-readable-change-logs-often-missing-very-valuable-tradeoffs"></a>
### Tradeoffs

- Requires discipline; high credibility payoff

<a id="run-5-progressive-ux-and-ambiguity-reduction-bottom-line-new-insight"></a>
## Bottom Line (New Insight)

Highest leverage at zero cost is less ambiguity: deterministic explanations, progressive disclosure, and constrained AI usage with clear boundaries.

<a id="run-6-search-portability-and-works-anywhere-ux"></a>
# Run 6 - Search, Portability, and Works-Anywhere UX

Strictly free architectures focusing on search, portability, and low-friction adoption with only static assets and browser execution.

<a id="run-6-search-portability-and-works-anywhere-ux-1-static-search-first-data-portal-search-beats-chat"></a>
## 1. Static Search-First Data Portal (Search Beats Chat)

<a id="run-6-search-portability-and-works-anywhere-ux-1-static-search-first-data-portal-search-beats-chat-core-idea"></a>
### Core idea

- Most users need fast, precise search across structured facts.

<a id="run-6-search-portability-and-works-anywhere-ux-1-static-search-first-data-portal-search-beats-chat-architecture"></a>
### Architecture

- Normalize data into small JSON documents
- Static site on GitHub Pages
- Client-side full-text + fielded search (index built at commit time)

<a id="run-6-search-portability-and-works-anywhere-ux-1-static-search-first-data-portal-search-beats-chat-ux"></a>
### UX

- Single search box
- Filters auto-appear (year, revenue band, risk flags)
- Click result -> summary page with charts

<a id="run-6-search-portability-and-works-anywhere-ux-1-static-search-first-data-portal-search-beats-chat-tradeoffs"></a>
### Tradeoffs

- Not conversational; extremely fast and predictable

<a id="run-6-search-portability-and-works-anywhere-ux-1-static-search-first-data-portal-search-beats-chat-fastest-free-implementation"></a>
### Fastest free implementation

- Prebuilt search index committed to repo
- Lightweight JS search library
- Plain HTML templates

<a id="run-6-search-portability-and-works-anywhere-ux-2-spreadsheet-as-ui-with-static-publishing"></a>
## 2. Spreadsheet-as-UI with Static Publishing

<a id="run-6-search-portability-and-works-anywhere-ux-2-spreadsheet-as-ui-with-static-publishing-core-idea"></a>
### Core idea

- Use spreadsheets as the authoring and interaction layer.

<a id="run-6-search-portability-and-works-anywhere-ux-2-spreadsheet-as-ui-with-static-publishing-architecture"></a>
### Architecture

- Data maintained in CSV/XLSX
- Static HTML views generated from spreadsheets
- Published via GitHub

<a id="run-6-search-portability-and-works-anywhere-ux-2-spreadsheet-as-ui-with-static-publishing-ux"></a>
### UX

- Table-centric; familiar filters/sorting/totals
- Links from cells to deeper narrative pages

<a id="run-6-search-portability-and-works-anywhere-ux-2-spreadsheet-as-ui-with-static-publishing-chatgpt-usage-free-ui"></a>
### ChatGPT usage (free UI)

- Copy selected rows + prompt; no API calls

<a id="run-6-search-portability-and-works-anywhere-ux-2-spreadsheet-as-ui-with-static-publishing-tradeoffs"></a>
### Tradeoffs

- Visuals secondary; very low training cost

<a id="run-6-search-portability-and-works-anywhere-ux-3-static-pdf-interactive-companion-site"></a>
## 3. Static PDF + Interactive Companion Site

<a id="run-6-search-portability-and-works-anywhere-ux-3-static-pdf-interactive-companion-site-core-idea"></a>
### Core idea

- Pair a print-ready artifact with a lightweight interactive layer.

<a id="run-6-search-portability-and-works-anywhere-ux-3-static-pdf-interactive-companion-site-architecture"></a>
### Architecture

- PDF report committed to repo
- Companion static site with charts, tables, and downloads
- Cross-links between PDF sections and live views

<a id="run-6-search-portability-and-works-anywhere-ux-3-static-pdf-interactive-companion-site-ux"></a>
### UX

- Works for email/printing/board packets; site adds depth

<a id="run-6-search-portability-and-works-anywhere-ux-3-static-pdf-interactive-companion-site-tradeoffs"></a>
### Tradeoffs

- Two artifacts to maintain; great for formal review contexts

<a id="run-6-search-portability-and-works-anywhere-ux-4-field-guide-ux-reference-not-dashboard"></a>
## 4. Field-Guide UX (Reference, Not Dashboard)

<a id="run-6-search-portability-and-works-anywhere-ux-4-field-guide-ux-reference-not-dashboard-core-idea"></a>
### Core idea

- Treat the system as a reference manual, not an app.

<a id="run-6-search-portability-and-works-anywhere-ux-4-field-guide-ux-reference-not-dashboard-architecture"></a>
### Architecture

- Markdown pages: how to read a 990, key indicators, common risk patterns
- Each concept page links to examples and data slices

<a id="run-6-search-portability-and-works-anywhere-ux-4-field-guide-ux-reference-not-dashboard-ux"></a>
### UX

- Browse by concept; learn -> inspect -> verify

<a id="run-6-search-portability-and-works-anywhere-ux-4-field-guide-ux-reference-not-dashboard-tradeoffs"></a>
### Tradeoffs

- Not exploratory; strong educational value

<a id="run-6-search-portability-and-works-anywhere-ux-5-client-side-compare-anything-tool"></a>
## 5. Client-Side Compare Anything Tool

<a id="run-6-search-portability-and-works-anywhere-ux-5-client-side-compare-anything-tool-core-idea"></a>
### Core idea

- Comparison is the most common analytic action.

<a id="run-6-search-portability-and-works-anywhere-ux-5-client-side-compare-anything-tool-architecture"></a>
### Architecture

- Static data bundles
- Browser-only comparison engine for years/entities/metrics

<a id="run-6-search-portability-and-works-anywhere-ux-5-client-side-compare-anything-tool-ux"></a>
### UX

- Side-by-side tables
- Delta highlights
- Simple visual diffs

<a id="run-6-search-portability-and-works-anywhere-ux-5-client-side-compare-anything-tool-chatgpt-assist"></a>
### ChatGPT assist

- Copy explain differences block for narrative interpretation

<a id="run-6-search-portability-and-works-anywhere-ux-5-client-side-compare-anything-tool-tradeoffs"></a>
### Tradeoffs

- No free-text input; high signal for oversight

<a id="run-6-search-portability-and-works-anywhere-ux-6-pre-computed-insight-library-no-runtime-logic"></a>
## 6. Pre-Computed Insight Library (No Runtime Logic)

<a id="run-6-search-portability-and-works-anywhere-ux-6-pre-computed-insight-library-no-runtime-logic-core-idea"></a>
### Core idea

- All heavy thinking happens before deployment.

<a id="run-6-search-portability-and-works-anywhere-ux-6-pre-computed-insight-library-no-runtime-logic-architecture"></a>
### Architecture

- Insights computed offline
- Stored as JSON + Markdown
- Static site only renders results

<a id="run-6-search-portability-and-works-anywhere-ux-6-pre-computed-insight-library-no-runtime-logic-ux"></a>
### UX

- Instant load; no spinners; no browser computation risk

<a id="run-6-search-portability-and-works-anywhere-ux-6-pre-computed-insight-library-no-runtime-logic-tradeoffs"></a>
### Tradeoffs

- Must re-run analysis when data changes; maximum reliability

<a id="run-6-search-portability-and-works-anywhere-ux-7-manual-refresh-with-guardrails-new-variant"></a>
## 7. Manual Refresh with Guardrails (New Variant)

<a id="run-6-search-portability-and-works-anywhere-ux-7-manual-refresh-with-guardrails-new-variant-pattern"></a>
### Pattern

- Data updates only via pull request
- Checklist: source verified, schema unchanged, metrics reviewed
- GitHub Pages rebuilds

<a id="run-6-search-portability-and-works-anywhere-ux-7-manual-refresh-with-guardrails-new-variant-result"></a>
### Result

- Free, auditable, human-controlled

<a id="run-6-search-portability-and-works-anywhere-ux-8-export-everything-philosophy"></a>
## 8. Export Everything Philosophy

<a id="run-6-search-portability-and-works-anywhere-ux-8-export-everything-philosophy-core-idea"></a>
### Core idea

- Every view can be taken elsewhere.

<a id="run-6-search-portability-and-works-anywhere-ux-8-export-everything-philosophy-architecture"></a>
### Architecture

- Each chart/table includes CSV export, image export, and permalink

<a id="run-6-search-portability-and-works-anywhere-ux-8-export-everything-philosophy-ux"></a>
### UX

- Encourages reuse; no lock-in; works with email/slides/docs

<a id="run-6-search-portability-and-works-anywhere-ux-8-export-everything-philosophy-tradeoffs"></a>
### Tradeoffs

- Slightly more UI work; high downstream value

<a id="run-6-search-portability-and-works-anywhere-ux-bottom-line-new-insight"></a>
## Bottom Line (New Insight)

At zero cost, search, comparison, and reference often outperform chat. ChatGPT remains an optional interpretive lens, never infrastructure.

<a id="run-7-distribution-channels-and-reuse"></a>
# Run 7 - Distribution Channels and Reuse

Strictly free architectures emphasizing distribution, reuse outside the dashboard, and low-friction adoption, while keeping everything static and versioned.

<a id="run-7-distribution-channels-and-reuse-1-static-api-via-versioned-json-endpoints-api-without-a-server"></a>
## 1. Static API via Versioned JSON Endpoints (API Without a Server)

<a id="run-7-distribution-channels-and-reuse-1-static-api-via-versioned-json-endpoints-api-without-a-server-core-idea"></a>
### Core idea

- Expose Clearlane + 990 data as stable, versioned JSON URLs that behave like an API without running one.

<a id="run-7-distribution-channels-and-reuse-1-static-api-via-versioned-json-endpoints-api-without-a-server-architecture"></a>
### Architecture

- Publish JSON to predictable paths (for example: /api/v1/org/{id}.json, /api/v1/990/{ein}/{year}.json)
- Host via GitHub Pages
- No runtime logic

<a id="run-7-distribution-channels-and-reuse-1-static-api-via-versioned-json-endpoints-api-without-a-server-ux"></a>
### UX

- Dashboard consumes the same URLs
- Power users can bookmark/download/reuse links directly

<a id="run-7-distribution-channels-and-reuse-1-static-api-via-versioned-json-endpoints-api-without-a-server-chatgpt-usage-free-ui"></a>
### ChatGPT usage (free UI)

- Paste JSON contents into ChatGPT with a fixed prompt

<a id="run-7-distribution-channels-and-reuse-1-static-api-via-versioned-json-endpoints-api-without-a-server-tradeoffs"></a>
### Tradeoffs

- No dynamic querying; extremely robust and reusable

<a id="run-7-distribution-channels-and-reuse-1-static-api-via-versioned-json-endpoints-api-without-a-server-fastest-free-implementation"></a>
### Fastest free implementation

- Commit JSON
- Enable Pages
- Document endpoints in README

<a id="run-7-distribution-channels-and-reuse-2-rss-atom-feeds-as-an-insight-delivery-channel"></a>
## 2. RSS / Atom Feeds as an Insight Delivery Channel

<a id="run-7-distribution-channels-and-reuse-2-rss-atom-feeds-as-an-insight-delivery-channel-core-idea"></a>
### Core idea

- Turn data changes and findings into feeds, not dashboards.

<a id="run-7-distribution-channels-and-reuse-2-rss-atom-feeds-as-an-insight-delivery-channel-architecture"></a>
### Architecture

- Static RSS/Atom feeds generated at commit time: new filings, material changes, anomalies
- Feeds hosted on GitHub Pages

<a id="run-7-distribution-channels-and-reuse-2-rss-atom-feeds-as-an-insight-delivery-channel-ux"></a>
### UX

- Subscribe in any feed reader; each entry links to Markdown explainers, charts, and data files

<a id="run-7-distribution-channels-and-reuse-2-rss-atom-feeds-as-an-insight-delivery-channel-why-this-is-different"></a>
### Why this is different

- Pushes insights to the user; zero UI learning curve

<a id="run-7-distribution-channels-and-reuse-2-rss-atom-feeds-as-an-insight-delivery-channel-tradeoffs"></a>
### Tradeoffs

- Not exploratory; excellent for monitoring

<a id="run-7-distribution-channels-and-reuse-3-browser-extension-as-the-ux-static-local"></a>
## 3. Browser Extension as the UX (Static + Local)

<a id="run-7-distribution-channels-and-reuse-3-browser-extension-as-the-ux-static-local-core-idea"></a>
### Core idea

- Bring the data to the user instead of sending the user to a site.

<a id="run-7-distribution-channels-and-reuse-3-browser-extension-as-the-ux-static-local-architecture"></a>
### Architecture

- Local browser extension bundles static Clearlane + 990 snapshots and lightweight visualizations
- Updates via GitHub releases (manual install)

<a id="run-7-distribution-channels-and-reuse-3-browser-extension-as-the-ux-static-local-ux"></a>
### UX

- Click extension icon for summaries/charts/comparisons
- Copy for ChatGPT buttons built in

<a id="run-7-distribution-channels-and-reuse-3-browser-extension-as-the-ux-static-local-tradeoffs"></a>
### Tradeoffs

- Installation step required; very fast access once installed

<a id="run-7-distribution-channels-and-reuse-3-browser-extension-as-the-ux-static-local-fastest-free-implementation"></a>
### Fastest free implementation

- Vanilla JS extension
- Static JSON
- Manual release updates

<a id="run-7-distribution-channels-and-reuse-4-json-ld-linked-data-publishing-machine-readable-first"></a>
## 4. JSON-LD / Linked-Data Publishing (Machine-Readable First)

<a id="run-7-distribution-channels-and-reuse-4-json-ld-linked-data-publishing-machine-readable-first-core-idea"></a>
### Core idea

- Publish data so machines and AI tools understand it natively.

<a id="run-7-distribution-channels-and-reuse-4-json-ld-linked-data-publishing-machine-readable-first-architecture"></a>
### Architecture

- Express facts as JSON-LD
- Embed in static HTML pages
- Human-readable view + structured data together

<a id="run-7-distribution-channels-and-reuse-4-json-ld-linked-data-publishing-machine-readable-first-ux"></a>
### UX

- Humans read summaries/charts; AI tools ingest structured context cleanly

<a id="run-7-distribution-channels-and-reuse-4-json-ld-linked-data-publishing-machine-readable-first-chatgpt-usage"></a>
### ChatGPT usage

- Paste JSON-LD blocks for higher-quality reasoning

<a id="run-7-distribution-channels-and-reuse-4-json-ld-linked-data-publishing-machine-readable-first-tradeoffs"></a>
### Tradeoffs

- Requires semantic modeling upfront; long-term interoperability win

<a id="run-7-distribution-channels-and-reuse-5-docs-as-ui-with-search-only-interaction"></a>
## 5. Docs-as-UI with Search-Only Interaction

<a id="run-7-distribution-channels-and-reuse-5-docs-as-ui-with-search-only-interaction-core-idea"></a>
### Core idea

- Treat the system like technical documentation, not an app.

<a id="run-7-distribution-channels-and-reuse-5-docs-as-ui-with-search-only-interaction-architecture"></a>
### Architecture

- Markdown docs: one page per entity and per metric
- Static search index; minimal charts

<a id="run-7-distribution-channels-and-reuse-5-docs-as-ui-with-search-only-interaction-ux"></a>
### UX

- Search -> read -> verify; extremely fast and low cognitive load

<a id="run-7-distribution-channels-and-reuse-5-docs-as-ui-with-search-only-interaction-tradeoffs"></a>
### Tradeoffs

- Minimal visuals; maximum clarity and longevity

<a id="run-7-distribution-channels-and-reuse-6-read-only-codespace-devcontainer-analysis-without-setup"></a>
## 6. Read-Only Codespace / Devcontainer (Analysis Without Setup)

<a id="run-7-distribution-channels-and-reuse-6-read-only-codespace-devcontainer-analysis-without-setup-core-idea"></a>
### Core idea

- Provide a ready-to-run analysis environment without local installs.

<a id="run-7-distribution-channels-and-reuse-6-read-only-codespace-devcontainer-analysis-without-setup-architecture"></a>
### Architecture

- Repo includes notebooks/scripts and data snapshots
- Free ephemeral GitHub Codespaces for exploration

<a id="run-7-distribution-channels-and-reuse-6-read-only-codespace-devcontainer-analysis-without-setup-ux"></a>
### UX

- Open -> explore -> close; no setup; export results to static artifacts

<a id="run-7-distribution-channels-and-reuse-6-read-only-codespace-devcontainer-analysis-without-setup-tradeoffs"></a>
### Tradeoffs

- Not a polished UX; powerful for analysts/auditors

<a id="run-7-distribution-channels-and-reuse-7-snapshot-microsites-per-release-disposable-shareable"></a>
## 7. Snapshot Microsites per Release (Disposable, Shareable)

<a id="run-7-distribution-channels-and-reuse-7-snapshot-microsites-per-release-disposable-shareable-core-idea"></a>
### Core idea

- Each data refresh produces a standalone microsite.

<a id="run-7-distribution-channels-and-reuse-7-snapshot-microsites-per-release-disposable-shareable-architecture"></a>
### Architecture

- Every GitHub release includes /site folder with static HTML/data/charts
- Each release gets its own Pages URL

<a id="run-7-distribution-channels-and-reuse-7-snapshot-microsites-per-release-disposable-shareable-ux"></a>
### UX

- Share snapshot link tied to specific version; ideal for review and audit

<a id="run-7-distribution-channels-and-reuse-7-snapshot-microsites-per-release-disposable-shareable-tradeoffs"></a>
### Tradeoffs

- Multiple URLs over time; strong audit trail

<a id="run-7-distribution-channels-and-reuse-8-manual-semi-automated-refresh-distribution-focused-variant"></a>
## 8. Manual + Semi-Automated Refresh (Distribution-Focused Variant)

<a id="run-7-distribution-channels-and-reuse-8-manual-semi-automated-refresh-distribution-focused-variant-pattern"></a>
### Pattern

- Data added manually or via script
- GitHub Action validates schemas and rebuilds assets
- Humans decide when to publish feeds/snapshots/microsites

<a id="run-7-distribution-channels-and-reuse-8-manual-semi-automated-refresh-distribution-focused-variant-result"></a>
### Result

- Free, controlled, transparent

<a id="run-7-distribution-channels-and-reuse-bottom-line-new-insight"></a>
## Bottom Line (New Insight)

Distribution channels matter as much as dashboards: static API-like endpoints, feeds, extensions, linked data, and snapshot microsites create multiple durable UX paths with AI optional.

<a id="run-8-guided-interaction-and-lowest-operational-risk"></a>
# Run 8 - Guided Interaction and Lowest Operational Risk

Strictly free architectures focusing on guided interaction, constraint-driven clarity, and lowest operational risk using only static assets and browser execution.

<a id="run-8-guided-interaction-and-lowest-operational-risk-1-guided-question-trails-decision-trees-not-chat"></a>
## 1. Guided Question Trails (Decision Trees, Not Chat)

<a id="run-8-guided-interaction-and-lowest-operational-risk-1-guided-question-trails-decision-trees-not-chat-core-idea"></a>
### Core idea

- Replace free-form chat with explicit question paths that mirror oversight workflows.

<a id="run-8-guided-interaction-and-lowest-operational-risk-1-guided-question-trails-decision-trees-not-chat-architecture"></a>
### Architecture

- Static site on GitHub Pages
- Each trail is a JSON decision tree: question -> options -> next question or answer
- Leaves link to charts, tables, and source filings

<a id="run-8-guided-interaction-and-lowest-operational-risk-1-guided-question-trails-decision-trees-not-chat-ux"></a>
### UX

- Click-through, no typing
- Feels conversational but deterministic
- Impossible to ask an unanswerable question

<a id="run-8-guided-interaction-and-lowest-operational-risk-1-guided-question-trails-decision-trees-not-chat-chatgpt-usage-optional"></a>
### ChatGPT usage (optional)

- Terminal node includes fixed prompt: alternative interpretations of documented finding

<a id="run-8-guided-interaction-and-lowest-operational-risk-1-guided-question-trails-decision-trees-not-chat-tradeoffs"></a>
### Tradeoffs

- Requires upfront modeling; extremely safe and repeatable

<a id="run-8-guided-interaction-and-lowest-operational-risk-1-guided-question-trails-decision-trees-not-chat-fastest-free-implementation"></a>
### Fastest free implementation

- JSON decision trees
- Vanilla JS renderer
- Static Markdown answer pages

<a id="run-8-guided-interaction-and-lowest-operational-risk-2-constraint-based-query-builder-natural-language-without-nlp"></a>
## 2. Constraint-Based Query Builder (Natural Language Without NLP)

<a id="run-8-guided-interaction-and-lowest-operational-risk-2-constraint-based-query-builder-natural-language-without-nlp-core-idea"></a>
### Core idea

- Users assemble questions from controlled building blocks.

<a id="run-8-guided-interaction-and-lowest-operational-risk-2-constraint-based-query-builder-natural-language-without-nlp-architecture"></a>
### Architecture

- Dropdowns: subject, time range, comparison mode
- JS maps selections to predefined queries

<a id="run-8-guided-interaction-and-lowest-operational-risk-2-constraint-based-query-builder-natural-language-without-nlp-ux"></a>
### UX

- Reads like a sentence (for example: "Show funding concentration for 2022-2024 compared to prior years")
- Outputs chart + explanation + table

<a id="run-8-guided-interaction-and-lowest-operational-risk-2-constraint-based-query-builder-natural-language-without-nlp-why-this-matters"></a>
### Why this matters

- Avoids NLP; guarantees valid queries

<a id="run-8-guided-interaction-and-lowest-operational-risk-2-constraint-based-query-builder-natural-language-without-nlp-tradeoffs"></a>
### Tradeoffs

- Limited expressiveness; very low error rate

<a id="run-8-guided-interaction-and-lowest-operational-risk-3-explainers-as-the-primary-artifact-system"></a>
## 3. Explainers as the Primary Artifact System

<a id="run-8-guided-interaction-and-lowest-operational-risk-3-explainers-as-the-primary-artifact-system-core-idea"></a>
### Core idea

- Every insight exists first as a standalone explainer, not a chart.

<a id="run-8-guided-interaction-and-lowest-operational-risk-3-explainers-as-the-primary-artifact-system-architecture"></a>
### Architecture

- /explainers Markdown directory; one file per insight; includes claim, evidence, limitations, visuals

<a id="run-8-guided-interaction-and-lowest-operational-risk-3-explainers-as-the-primary-artifact-system-ux"></a>
### UX

- Browse explainers like a library; searchable, linkable, printable

<a id="run-8-guided-interaction-and-lowest-operational-risk-3-explainers-as-the-primary-artifact-system-chatgpt-assist"></a>
### ChatGPT assist

- Consistent prompt on each explainer: summarize for a non-technical audience

<a id="run-8-guided-interaction-and-lowest-operational-risk-3-explainers-as-the-primary-artifact-system-tradeoffs"></a>
### Tradeoffs

- Less exploratory; high clarity and governance value

<a id="run-8-guided-interaction-and-lowest-operational-risk-4-client-side-what-changed-diff-viewer"></a>
## 4. Client-Side What Changed Diff Viewer

<a id="run-8-guided-interaction-and-lowest-operational-risk-4-client-side-what-changed-diff-viewer-core-idea"></a>
### Core idea

- Focus on change: most oversight questions are about deltas.

<a id="run-8-guided-interaction-and-lowest-operational-risk-4-client-side-what-changed-diff-viewer-architecture"></a>
### Architecture

- Static snapshots per year
- Browser-side diff engine highlights increases/decreases and threshold crossings

<a id="run-8-guided-interaction-and-lowest-operational-risk-4-client-side-what-changed-diff-viewer-ux"></a>
### UX

- Select two years; see deltas, percent change, narrative summary

<a id="run-8-guided-interaction-and-lowest-operational-risk-4-client-side-what-changed-diff-viewer-tradeoffs"></a>
### Tradeoffs

- Requires consistent schemas; very high signal

<a id="run-8-guided-interaction-and-lowest-operational-risk-5-single-page-board-view-opinionated-read-only"></a>
## 5. Single-Page Board View (Opinionated, Read-Only)

<a id="run-8-guided-interaction-and-lowest-operational-risk-5-single-page-board-view-opinionated-read-only-core-idea"></a>
### Core idea

- One page answers ~90% of oversight questions.

<a id="run-8-guided-interaction-and-lowest-operational-risk-5-single-page-board-view-opinionated-read-only-architecture"></a>
### Architecture

- Precomputed metrics
- No filters
- Minimal controls (year selection only)

<a id="run-8-guided-interaction-and-lowest-operational-risk-5-single-page-board-view-opinionated-read-only-ux"></a>
### UX

- Load -> read -> done; designed for trust, not exploration

<a id="run-8-guided-interaction-and-lowest-operational-risk-5-single-page-board-view-opinionated-read-only-chatgpt-usage"></a>
### ChatGPT usage

- Optional Explain this page copy block for narrative reframing

<a id="run-8-guided-interaction-and-lowest-operational-risk-5-single-page-board-view-opinionated-read-only-tradeoffs"></a>
### Tradeoffs

- Not flexible; very low cognitive load

<a id="run-8-guided-interaction-and-lowest-operational-risk-6-form-factor-specific-ux-mobile-first-desktop-second"></a>
## 6. Form-Factor-Specific UX (Mobile-First, Desktop-Second)

<a id="run-8-guided-interaction-and-lowest-operational-risk-6-form-factor-specific-ux-mobile-first-desktop-second-core-idea"></a>
### Core idea

- Design explicitly for phone/tablet review.

<a id="run-8-guided-interaction-and-lowest-operational-risk-6-form-factor-specific-ux-mobile-first-desktop-second-architecture"></a>
### Architecture

- Responsive static site
- Cards instead of dense tables
- Charts optimized for narrow screens

<a id="run-8-guided-interaction-and-lowest-operational-risk-6-form-factor-specific-ux-mobile-first-desktop-second-ux"></a>
### UX

- Swipeable sections
- Tap to expand details
- Offline-friendly caching

<a id="run-8-guided-interaction-and-lowest-operational-risk-6-form-factor-specific-ux-mobile-first-desktop-second-tradeoffs"></a>
### Tradeoffs

- Fewer data points per view; higher accessibility

<a id="run-8-guided-interaction-and-lowest-operational-risk-7-zero-js-fallback-mode-graceful-degradation"></a>
## 7. Zero-JS Fallback Mode (Graceful Degradation)

<a id="run-8-guided-interaction-and-lowest-operational-risk-7-zero-js-fallback-mode-graceful-degradation-core-idea"></a>
### Core idea

- Everything works even if JavaScript fails.

<a id="run-8-guided-interaction-and-lowest-operational-risk-7-zero-js-fallback-mode-graceful-degradation-architecture"></a>
### Architecture

- Default: Markdown/HTML tables/SVG charts
- JS only enhances filtering/toggles/comparisons

<a id="run-8-guided-interaction-and-lowest-operational-risk-7-zero-js-fallback-mode-graceful-degradation-ux"></a>
### UX

- Always readable; never blank; resilient long-term

<a id="run-8-guided-interaction-and-lowest-operational-risk-7-zero-js-fallback-mode-graceful-degradation-tradeoffs"></a>
### Tradeoffs

- Less interactivity; maximum durability

<a id="run-8-guided-interaction-and-lowest-operational-risk-8-manual-refresh-with-explicit-effective-date-labels"></a>
## 8. Manual Refresh With Explicit Effective Date Labels

<a id="run-8-guided-interaction-and-lowest-operational-risk-8-manual-refresh-with-explicit-effective-date-labels-core-idea"></a>
### Core idea

- Never hide when data was last updated.

<a id="run-8-guided-interaction-and-lowest-operational-risk-8-manual-refresh-with-explicit-effective-date-labels-architecture"></a>
### Architecture

- Every page includes Data effective as of YYYY-MM-DD
- Updates only via PR; Pages rebuilds

<a id="run-8-guided-interaction-and-lowest-operational-risk-8-manual-refresh-with-explicit-effective-date-labels-ux"></a>
### UX

- Users know freshness immediately; avoids false real-time expectations

<a id="run-8-guided-interaction-and-lowest-operational-risk-8-manual-refresh-with-explicit-effective-date-labels-tradeoffs"></a>
### Tradeoffs

- Manual discipline required; strong trust signal

<a id="run-8-guided-interaction-and-lowest-operational-risk-bottom-line-new-insight"></a>
## Bottom Line (New Insight)

Most reliable zero-cost UX removes ambiguity instead of interpreting it: guided paths, constrained builders, explainer-first content, and deterministic fallbacks with ChatGPT optional.
