# Set up your own workspace

Setup is a one-time choice of where your ideas live. You create the workspace and point Ideations at it; the skills create idea folders and reports as you use them.

## What you set up

| Item | Required? | What you do |
|---|---|---|
| This repository | Yes | Clone or download it, keeping skills, docs and scripts together. |
| Python and an agent | Yes | Use Python 3.10+ on macOS/Linux and an agent with local file access. |
| Private workspace | Yes | Create or choose a folder outside this repository. |
| Workspace setting | Yes | Set its path in local configuration, an environment variable, or `--root`. |
| Workspace FOUNDER.md | Optional | Copy the template and describe your constraints and experience. |
| Research tools/model | For market scans | Use a host with browsing and an inexpensive worker; optionally pin the model. |

There are no Python packages, database or background service to install. The workspace is separate from the core's Git history. Ideations does not back it up or sync it; choose your own backup or private repository if needed.

## 1. Get the repository

Clone it using an account with access, or download a copy. In a terminal:

```sh
git clone https://github.com/jamescazzetta/ideations.git
cd ideations
```

Open this directory in your agent. Run the following commands from this repository's root. If you already have the repository, use your existing checkout.

## 2. Create and connect the workspace

For the default sibling layout:

```sh
mkdir -p ../ideations-workspace
test -e ideations.local.json || cp ideations.example.json ideations.local.json
python3 scripts/portfolio.py settings
python3 scripts/portfolio.py status
```

`mkdir` creates the private workspace. The copy creates an ignored, machine-local configuration only if one does not already exist. The helper reports settings and inventory but does not create the workspace for you.

The configuration looks like this:

```json
{
  "workspace": "../ideations-workspace",
  "research": {
    "model": null,
    "reasoning_effort": "low"
  }
}
```

The workspace path is relative to the repository, so the helper can find it even when invoked from elsewhere. You can instead put an absolute path in this field. Create that directory first, then check that `settings` reports the intended location. Keep credentials out of this file.

A fresh workspace reports:

```text
ACTIVE 0/3; BUILDING 0/1
```

An existing workspace lists its ideas. It does not need to be empty. Only immediate real folders containing CONTEXT.md and no SKILL.md count as ideas. For moving an existing portfolio, follow [migration guidance](migration.md).

### Other ways to select a workspace

Configuration precedence is: `--root`, then `IDEATIONS_WORKSPACE`, then `ideations.local.json`. For a single command:

```sh
python3 scripts/portfolio.py --root /absolute/path/to/my-ideas status
```

The directory must already exist. Explicit and environment paths resolve from the calling directory; relative JSON configuration paths resolve from the core. Use the same workspace override for every command in a procedure. If no workspace is selected, the helper stops with setup guidance; it never defaults to writing into the core.

## 3. Add founder context, if useful

For the default layout:

```sh
test -e ../ideations-workspace/FOUNDER.md || cp templates/FOUNDER.md ../ideations-workspace/FOUNDER.md
```

If your workspace is elsewhere, copy to that location instead. Edit **FOUNDER.md in your workspace**, leaving the repository template reusable. The command preserves an existing founder file.

A few honest bullets are enough:

- How much time you have and what commitments already consume it.
- Relevant experience, skills and actual access to potential customers.
- Financial or operational constraints you want decisions to respect.
- Preferred business formats, interests and noncommercial ideas worth keeping.

Leave unknowns blank. The skills use this context when assessing fit, priorities and commitments; it is not proof of customer demand. Skipping this file is fine—the agent should state missing context rather than invent it. The [template](../templates/FOUNDER.md) contains no personal profile until you fill in your private copy.

## 4. Capture your first idea

Allow your agent to read this repository and read/write the chosen workspace. Ask it:

> Read AGENTS.md in this repository. Capture this idea in my configured workspace: [your idea]. Skip market research for now.

The agent reads the capture skill, checks for a related existing idea, and creates or updates `<idea-slug>/CONTEXT.md` in the workspace. It returns a link to the note. This happens in the current conversation; it does not monitor other chats. These instructions work without a global skill installation.

Verify the result with:

```sh
python3 scripts/portfolio.py status
```

Your new idea is SEED. You do **not** create empty STATE.md, EVIDENCE.md, or analysis files. Later skills create their own outputs when requested. For example, “Define an offer for my-idea” creates OFFER.md, and “Compare my ideas” creates workspace PORTFOLIO.md. The [files reference](artifacts.md) lists all outputs.

## Optional: enable market research

A new product/service capture normally hands off to one small market scan unless you ask to skip it. Conceptual notes and routine edits do not trigger scans.

Your agent host needs browsing and a way to select an inexpensive worker. The default `model: null` lets it choose when it can identify a suitable inexpensive model. To pin one, replace null with a model name your host actually supports. Configuration does not install models, authenticate a provider, or enable delegation.

If browsing or the worker is unavailable, the idea stays saved and the scan is reported pending. Other skills still work with explicit evidence limitations. You can request a scan later when the tools are available.

## If setup does not work

| Message or symptom | What to check |
|---|---|
| “Choose a workspace” | Create local configuration or supply `--root`. |
| “Workspace does not exist” | Create the configured folder, or correct its path. |
| “Keep workspace data outside the core” | Choose a sibling or another external directory, including for example runs. |
| Invalid configuration | Check JSON syntax and the supported fields shown above. |
| Agent cannot write the workspace | Allow that directory in your host's file-access settings. |
| Agent cannot find a skill | Ask it to read the full path to this repository's AGENTS.md or the selected SKILL.md. |

Next, choose one question from the [skill menu](../README.md#choose-a-skill), or read a [fictional worked example](../examples/README.md). Lifecycle changes follow the [evidence and commitment rules](lifecycle.md); drafting a report alone never changes state.
