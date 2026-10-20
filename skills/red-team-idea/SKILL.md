---
name: red-team-idea
description: Attempt to disprove a captured idea's commercial case when asked to challenge it, identify failure modes, or decide why it may not be worth building.
---

# Red-team an idea

Read [the shared contract](../../docs/CONTRACT.md). Trigger on a request to challenge one captured idea; do not automatically run after market-check.

## Inputs and ownership

Require the selected idea's CONTEXT.md. Read MARKET.md if present, any existing CHALLENGE.md, and relevant supplied external evidence. Own only that idea's CHALLENGE.md. Append a dated assessment, preserving all earlier analysis and user annotations. Missing market evidence means a provisional challenge with explicit unknowns, not invented competitors or an automatic research run.

## Procedure and output

Take the stance: “Why is this probably not worth building?” Attack the product case rather than the elegance of the mechanism. Identify the target person, painful job and frequency, actual evidence of payment or costly workarounds, and whether the mechanism changes an outcome that person cares about.

Consider substitutes and inertia, switching costs, accessible distribution, incumbent advantages, operational and dependency burden, data/regulatory exposure, AI commoditization, defensibility and timing. Use only relevant factors; mark unresearched claims as hypotheses. Consider founder-specific disadvantages and whether this is a feature, a personal tool, or an interesting technical puzzle with no demonstrated demand. Do not invent domain expertise, customer access, or legal conclusions.

Keep the output focused (usually 500–800 words) with:
- Strongest case against the idea, grounded in the most consequential observations.
- Strongest case still remaining for it; do not manufacture balance if evidence is weak.
- Fatal assumptions (a short candidate list for assumption-map).
- Observations that would materially weaken the idea.
- Observations that would materially strengthen it.
- Most likely failure mode, explicitly labeled inference.
- A section titled exactly **What would make us abandon this idea?** with falsifiable observations or proposed thresholds, not “if it fails.”

Distinguish missing evidence from negative evidence and hard constraints from untested worries. Do not give a simplistic yes/no verdict. Conceptual notes without a commercial thesis may receive “commercial case not specified; no build case established” rather than a fictional business plan.

## Non-goals and handoff

No new market summary, browsing, implementation, state change, or automatic downstream invocation. Suggest assumption-map only if narrowing uncertainty would help; then stop. The challenge may recommend parking or rejection but only promotion-gate applies decisions.
