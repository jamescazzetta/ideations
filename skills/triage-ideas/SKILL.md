---
name: triage-ideas
description: Rank and prune ideas across the repository, recommending PROMOTE, VALIDATE, PARK, MERGE or KILL with explicit opportunity cost and portfolio limits.
---

# Triage the portfolio

Read [the shared contract](../../docs/CONTRACT.md) and [lifecycle](../../README.md). Trigger when the user wants to compare ideas or decide what deserves scarce attention.

## Inputs and ownership

Enumerate immediate workspace idea folders using `python3 scripts/portfolio.py status`; never include skills or test fixtures. Read their CONTEXT.md, canonical states, and available OFFER, MARKET, CHALLENGE, ASSUMPTIONS, VALIDATION, EVIDENCE, NEXT and retrospective records. Read existing PORTFOLIO.md, including manual commitments and annotations. Own only workspace PORTFOLIO.md; append a dated ranked assessment rather than replacing its history.

Missing optional artifacts lower confidence; no state means SEED, not researched. If state is malformed, flag the conflict and stop recommendations that would increase commitment until repaired. With zero ideas write a brief empty-portfolio assessment; with one, compare against doing nothing and existing commitments, not fictional alternatives.

## Decision procedure

Use five qualitative dimensions: pain strength, founder fit/unfair advantage, credible differentiation, distribution accessibility, and cheap testability. Label unknowns. Consider bootstrap compatibility, external-signal latency, operating/dependency burden and durable personal interest where decisive. Include acquisition time, delivery capacity, onboarding/integration effort and recurring support when comparing service and product options. Count ongoing customer commitments for shipped work as opportunity cost even though SHIPPED does not consume an active lifecycle slot. Do not turn these into a scoring engine.

Rank ideas explicitly against one another and the option of starting nothing. Assign exactly one recommendation per idea:
- PROMOTE: meaningful external evidence appears sufficient; request promotion-gate review, never bypass lifecycle steps.
- VALIDATE: one cheap test could change the decision, so allocate attention to that test.
- PARK: insufficient priority or a worthwhile reference without a current product case; specify a revisit trigger.
- MERGE: substantially the same mechanism/job; name the destination and what would be retained.
- KILL: strong negative evidence or an unacceptable dependency; explain what failed.

For terminal ideas, mark “no active candidacy”; retain the disposition (MERGE for MERGED, KILL for REJECTED, PARK for SHIPPED as a recommendation of no new work, not a state change). Do not automatically resurrect them. An existing BUILDING idea should be compared with finishing its current scope; VALIDATE can mean its next external test and PROMOTE can mean continue a justified commitment, without resetting state. Explain this explicitly.

Each ranked row includes recommendation, concise comparative rationale, evidence confidence, and what would change it. Summarize capacity from canonical state: ACTIVE <=3 including VALIDATING/PROMOTED/BUILDING; BUILDING <=1. Each proposed entrant names what work loses attention even if capacity is free. When full, name exactly which current idea must leave and its proposed disposition. Do not propose more than three combined active ideas or a second builder. User annotations expressing an active commitment with no matching STATE are a conflict to resolve, not free capacity.

## Non-goals and handoff

No state changes, silent promotion, research, implementation or automatic gate calls. Recommend fewer projects; an all-PARK/KILL result is valid. Link gate checks or a cheap test as optional follow-up and stop.
