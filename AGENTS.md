# Ideations operating instructions

Read [README.md](README.md) for doctrine and lifecycle and [docs/CONTRACT.md](docs/CONTRACT.md) before running a skill. This is a filesystem decision-support system, not an autonomous project generator.

Use the skill matching the user's intent; read its complete `SKILL.md`. Skills are immediate directories under `skills/` containing `SKILL.md`. Resolve the separate private workspace using `python3 scripts/portfolio.py settings`; its immediate directories containing `CONTEXT.md` and no `SKILL.md` are ideas. Never infer the workspace from the current directory or scan the core as a portfolio. Do not scan test fixtures as portfolio ideas.

| Intent | Skill |
|---|---|
| Preserve a promising thought from available context | `skills/capture-ideas/SKILL.md` |
| Bounded competitor/substitute research | `skills/market-check/SKILL.md` |
| Attempt to disprove the product case | `skills/red-team-idea/SKILL.md` |
| Define a buyer, outcome, scope and price hypothesis | `skills/offer-design/SKILL.md` |
| Identify the few load-bearing unknowns | `skills/assumption-map/SKILL.md` |
| Compare, rank, prune across ideas | `skills/triage-ideas/SKILL.md` |
| Design one cheap falsification experiment | `skills/validation-designer/SKILL.md` |
| Check or explicitly change lifecycle state | `skills/promotion-gate/SKILL.md` |
| Pick 1–3 customer-learning/delivery actions | `skills/execution-bridge/SKILL.md` |
| Review attention allocation and stalled work | `skills/portfolio-review/SKILL.md` |
| Suggest structural connections for human review | `skills/cross-pollinate/SKILL.md` |
| Compare prior predictions with observed outcomes | `skills/idea-retrospective/SKILL.md` |

Capture first. Preserve the existing optional, bounded capture-to-market handoff for new product/service ideas. Everything after it is an explicit procedure requested by the user, never an automatic cascade. A request for a named sequence authorizes that finite sequence, not transitions, implementation, outreach, publishing, or spending unless separately included in the user's intent. Existing authorization in the conversation remains valid; do not ask again unnecessarily.

These local instructions refine the parent workspace's capture rules: work on this system, its reports, examples, skill outputs, and test fixtures must not itself trigger captures or market scans. Workers never recurse into capture or additional workers. Cross-pollination writes candidates only.

Only promotion-gate may append `STATE.md`, using `scripts/portfolio.py`. Other skills recommend; they never change states. No state file means SEED, regardless of existing prose. Active means VALIDATING, PROMOTED, or BUILDING: at most 3 combined and at most 1 BUILDING. Use the helper for counts; portfolio prose is not authoritative state.

Append dated assessments; preserve originals and human annotations. Missing evidence blocks a transition, not capture. Do not treat fictional test records as real evidence. No implementation of a captured idea starts from a skill recommendation.

Commercial work covers acquisition, sales, onboarding, delivery and retention. Plans never count as outcomes. SHIPPED remains terminal; ongoing customer commitments count as opportunity cost. Read workspace FOUNDER.md if present; do not assume a particular founder profile.
