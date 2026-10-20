# Working with Ideations

Use [README.md](README.md) for orientation. Before running a skill, read [the shared rules](docs/CONTRACT.md) and its complete SKILL.md. These rules refine parent workspace capture instructions: work on Ideations, reports, examples and tests never triggers capture or research.

Choose the skill that matches the user's request:

| Request | Skill |
|---|---|
| Save an idea | [capture-ideas](skills/capture-ideas/SKILL.md) |
| Find competitors or substitutes | [market-check](skills/market-check/SKILL.md) |
| Challenge an idea | [red-team-idea](skills/red-team-idea/SKILL.md) |
| Define a commercial offer | [offer-design](skills/offer-design/SKILL.md) |
| Identify critical assumptions | [assumption-map](skills/assumption-map/SKILL.md) |
| Design a test | [validation-designer](skills/validation-designer/SKILL.md) |
| Compare and prioritize ideas | [triage-ideas](skills/triage-ideas/SKILL.md) |
| Record results or check/change state | [promotion-gate](skills/promotion-gate/SKILL.md) |
| Choose the next customer action | [execution-bridge](skills/execution-bridge/SKILL.md) |
| Review attention and stalled work | [portfolio-review](skills/portfolio-review/SKILL.md) |
| Find connections between ideas | [cross-pollinate](skills/cross-pollinate/SKILL.md) |
| Compare predictions with outcomes | [idea-retrospective](skills/idea-retrospective/SKILL.md) |

Resolve the separate workspace with `python3 scripts/portfolio.py settings`; never infer it from the current directory. Use the helper for inventory and state checks. For state-dependent work, read [lifecycle and commitment](docs/lifecycle.md). Only promotion-gate may write STATE.md through the helper.
