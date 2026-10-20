# Quickstart

## Set up the core and your workspace

Use Python 3.10+ on macOS/Linux. Clone or download the core, open a terminal in it, then:

```sh
mkdir -p ../ideations-workspace
cp ideations.example.json ideations.local.json
python3 scripts/portfolio.py settings
python3 scripts/portfolio.py status
```

The workspace is private data, outside the repository. `ideations.local.json` is ignored by Git. Its relative workspace path is resolved from the core, so invoking the helper from another directory still works. Choose another existing directory with `--root /path/to/my-ideas` before the subcommand, or set `IDEATIONS_WORKSPACE`.

The default research model is null: a host may select an available inexpensive worker when it can identify one. Set `research.model` to an inexpensive model supported by your host to pin it; `research.reasoning_effort` is low by default. If the configured worker or browsing is unavailable, capture is still saved and research is pending. This configuration does not install models or provide API credentials.

Optionally copy `templates/FOUNDER.md` into the workspace and fill in relevant constraints. Use an agent with filesystem access and ask it to read this core's `AGENTS.md`. Automatic discovery and delegation differ between hosts; directly reading a skill works without a global installation.

## First idea

Ask: “Read skills/capture-ideas/SKILL.md and capture this idea in my configured workspace: [your thought]. Skip market research for now.”

The skill checks for an existing mechanism match and writes or appends CONTEXT.md. No STATE.md means SEED. The helper can also save a draft you have prepared:

```sh
python3 scripts/portfolio.py capture my-idea --content /path/to/context-draft.md
python3 scripts/portfolio.py status
```

The helper only writes the supplied text. Semantic duplicate checking and optional research are skill responsibilities.

## Choose the procedure you need

- “Challenge my-idea, then map its assumptions.”
- “Define one offer for my-idea, including buyer, scoped pilot and price hypothesis.”
- “Design one cheap test of its most important uncertainty.”
- “Record these actual trial results and check whether promotion is justified.”
- “What is the smallest next customer-learning action within its current state?”
- “Review delivery/support obligations alongside the rest of the portfolio.”

A requested finite sequence is supported; there is no automatic pipeline. Offer design can inform validation before a build. Conceptual notes do not need an offer. Review the [lifecycle](../README.md#lifecycle) before changing commitment.

## Reports and gates

Reports are appended through their owning skill. A draft contains only the new dated section:

```sh
python3 scripts/portfolio.py append-report offer-design --idea my-idea --content /path/to/offer-draft.md
python3 scripts/portfolio.py audit
```

Only promotion-gate may apply lifecycle changes, using actual evidence and the user's recorded decision. `transition` without `--apply` is a structural check, not a semantic verdict. An ALLOWED IN PRINCIPLE assessment does not authorize building.

See the [fictional examples](../examples/README.md) before trying the record format. Never copy their invented evidence or decisions into a real idea.
