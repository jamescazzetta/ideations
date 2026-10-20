---
name: market-check
description: Run a small sourced scan of competitors and substitutes for a captured product or service idea.
---

# Check what already exists

Compare the idea with relevant alternatives and identify what remains uncertain.

Follow the [shared rules](../../docs/CONTRACT.md). Require CONTEXT.md and read any existing MARKET.md. Save only MARKET.md. The coordinator must read [worker setup and review](references/delegation.md) before dispatching; an assigned worker performs the research below directly.

**Worker budget:** at most 6 search queries, 8 opened source pages, and approximately 800 report words. These are work limits, not a billing guarantee. Report actual usage only when supplied by the environment.

## Research the problem

1. Extract the user's problem, mechanism, audience and constraints, separating assistant suggestions. If audience/geography is unspecified, label the work an initial English-language scan with geography unspecified.
2. Search by problem and mechanism as well as the idea's wording. Include direct competitors, general tools and manual substitutes; consider official app-store listings for apps. Search generic descriptions rather than private details.
3. Aim for 3–5 relevant alternatives, fewer when evidence is limited. Open primary sources: official product pages, documentation, pricing or developer-controlled listings. Snippets and inaccessible pages remain unverified leads.
4. Compare concrete behavior. Label features **documented**, **explicitly unsupported**, or **not verified**. Marketing claims are advertised behavior, not independent tests. A missing mention does not prove a missing feature.
5. Describe possible differentiation as a hypothesis tied to evidence. Use “not found among the alternatives reviewed” when appropriate. Competitor presence or an apparent gap does not establish demand. No useful gap is a valid finding.
6. Suggest one small validation step and the most important remaining uncertainty. Leave market-size guesses, unsupported revenue claims, novelty scores and build verdicts out.

## Save the scan

Append to **MARKET.md** using `append-report market-check`. Include:

- Date, input idea link, model/effort actually used or unknown, scope and complete/partial status.
- Short assessment and a comparison table: alternative, direct/substitute, overlap, difference/unknown and sources.
- Possible differentiators, their evidence and how to challenge them.
- Actual queries, URLs, search/page counts and coverage limits, with citations beside supported claims.
- One suggested next validation step.

Use current web evidence. If browsing fails, save verified partial findings and label the scan incomplete; do not reconstruct competitors from memory. Preserve the original thesis and earlier assessments.

Refresh only on request or materially changed circumstances. Report unavailable research as pending once. Finish with a report link; this is a single foreground scan, not recurring monitoring or an analysis pipeline.
