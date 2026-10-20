# Ideations

**Agent skills for capturing ideas, testing their promise, and deciding what to pursue.**

Save a thought, see what already exists, work out what someone might buy, and choose a small real-world test. Ideations keeps your research, evidence, and decisions in Markdown so you can return to an idea without starting over.

Use it for products, services, or thoughts worth keeping. You choose which skill to run and what to act on.

## Why Ideations?

AI assistants help us generate ideas, explore possibilities, and build prototypes. Choosing what deserves our time still takes judgment: whose problem matters, what evidence would change our minds, and what we would give up to pursue it. Ideations gives that thinking a durable home, so each decision can draw on what we have already learned.

Your idea collection is meant to grow over time. Preserve promising thoughts, failed experiments, useful discoveries, and ideas you have set aside. When requested, [cross-pollinate](skills/cross-pollinate/SKILL.md) revisits the collection to suggest connections: a shared customer problem, a reusable component, or an approach from one idea that could strengthen another. An idea can contribute something valuable even if it never becomes a project. You decide which connections to pursue.

The aim is to accumulate knowledge while keeping active commitments small. The skills should evolve with real use too: refine what helps, and add a procedure when a recurring need earns it a place.

## How it fits together

There are two folders: this repository holds the reusable tools; a separate workspace holds your ideas.

```text
ideations/                    # This repository
├── skills/                   # Instructions your agent follows
├── scripts/portfolio.py      # Saves reports and checks lifecycle rules
├── templates/                # Optional starting points for your own notes
├── examples/                 # Fictional worked examples
├── docs/                     # Setup and reference
└── tests/

ideations-workspace/          # Your data, outside this repository
├── FOUNDER.md                # Optional: your time, experience, and goals
├── my-idea/
│   └── CONTEXT.md            # Created when you capture an idea
└── PORTFOLIO.md              # Created when you request a comparison
```

The skills do the thinking through your agent. The Python helper handles file writes and structural checks. Keep the repository together: individual skill files refer to shared instructions and the helper.

## Choose a skill

Ask your agent in ordinary language. Each skill saves a focused result you can revisit.

| I want to… | Skill | Result |
|---|---|---|
| Save this idea | [capture-ideas](skills/capture-ideas/SKILL.md) | Original context |
| See what already exists | [market-check](skills/market-check/SKILL.md) | Competitors and substitutes |
| Find reasons it might fail | [red-team-idea](skills/red-team-idea/SKILL.md) | Case against the idea |
| Define what someone would buy | [offer-design](skills/offer-design/SKILL.md) | Buyer, outcome, scope, and price hypothesis |
| Choose what to learn first | [assumption-map](skills/assumption-map/SKILL.md) | The few assumptions that matter |
| Design a small test | [validation-designer](skills/validation-designer/SKILL.md) | One experiment with success and stop criteria |
| Decide which ideas deserve attention | [triage-ideas](skills/triage-ideas/SKILL.md) | Ranked recommendations |
| Record results or check readiness | [promotion-gate](skills/promotion-gate/SKILL.md) | Evidence review and lifecycle decision |
| Choose the next customer action | [execution-bridge](skills/execution-bridge/SKILL.md) | 1–3 actions suited to the current state |
| Review where my time is going | [portfolio-review](skills/portfolio-review/SKILL.md) | Commitments, stalls, and tradeoffs |
| Find connections between ideas | [cross-pollinate](skills/cross-pollinate/SKILL.md) | Connections for you to consider |
| Learn from what happened | [idea-retrospective](skills/idea-retrospective/SKILL.md) | Predictions compared with outcomes |

Start with capture, then choose the question that matters now. You can request a sequence such as “Challenge this idea, then map its assumptions.” Customer learning can cover acquisition, sales, onboarding, delivery, and retention.

## Get started

You need **Python 3.10+ on macOS or Linux** and an agent that can read and write local files. The helper uses only Python's standard library.

Clone or download this repository, then run these commands from its root:

```sh
mkdir -p ../ideations-workspace
test -e ideations.local.json || cp ideations.example.json ideations.local.json
python3 scripts/portfolio.py settings
python3 scripts/portfolio.py status
```

This creates an empty workspace and a local configuration pointing to it, keeping any existing configuration. Check that `settings` shows the workspace you intend to use; a fresh one reports `ACTIVE 0/3; BUILDING 0/1`.

Optionally copy your founder-context template and fill it in:

```sh
test -e ../ideations-workspace/FOUNDER.md || cp templates/FOUNDER.md ../ideations-workspace/FOUNDER.md
```

Edit the **workspace copy**, adding the time you have, relevant experience, customer access, and constraints. It is fine to leave unknowns blank. If you use another workspace path, copy it there instead.

Open this repository in your agent, allow access to the workspace, and ask:

> Read AGENTS.md. Capture this idea in my configured workspace: [your idea]. Skip market research for now.

The agent creates the idea folder and CONTEXT.md. Other reports appear when you request their skills; you do not create them in advance.

See the [setup walkthrough](docs/quickstart.md) for a different workspace location, optional research, existing ideas, and troubleshooting.

## How we work

- **Capture freely, commit carefully.** Keep interesting thoughts without turning each one into a project.
- **Test before investing.** Prefer a small real-world test over a bigger argument or architecture.
- **Protect your attention.** At most three active ideas, with one being built. Name what loses attention when taking something on.
- **Keep the evidence and the decision separate.** Preserve earlier notes, learn from actual outcomes, and choose commitments yourself.

A new product or service capture normally gets one small market scan when the tools are available; ask to skip it when you prefer. Further procedures run when requested. Plans remain proposals; building, contacting people, publishing, and spending require your applicable authorization.

## Go deeper

[Worked examples](examples/README.md) · [Lifecycle and commitment](docs/lifecycle.md) · [Customer learning](docs/commercial-practice.md) · [Files and reports](docs/artifacts.md) · [Migration](docs/migration.md) · [Contributing](CONTRIBUTING.md)

[Release 0.9.0](https://github.com/jamescazzetta/ideations/releases/tag/v0.9.0) · [MIT licensed](LICENSE). Your workspace and local configuration stay outside the shared repository history.
