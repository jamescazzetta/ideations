#!/usr/bin/env python3
"""Local structural guards. Evidence truth and human intent require agent/human review."""
import argparse
from contextlib import contextmanager
from datetime import date, datetime, timezone
import fcntl
import json
import os
from pathlib import Path
import re
import sys

STATES = {"SEED", "RESEARCHED", "VALIDATING", "PROMOTED", "BUILDING",
          "SHIPPED", "PARKED", "MERGED", "REJECTED"}
ACTIVE = {"VALIDATING", "PROMOTED", "BUILDING"}
TERMINAL = {"SHIPPED", "MERGED", "REJECTED"}
FORWARD = dict(zip(["SEED", "RESEARCHED", "VALIDATING", "PROMOTED", "BUILDING"],
                   ["RESEARCHED", "VALIDATING", "PROMOTED", "BUILDING", "SHIPPED"]))
IDEA_REPORTS = {"market-check": "MARKET.md", "red-team-idea": "CHALLENGE.md",
                "offer-design": "OFFER.md",
                "assumption-map": "ASSUMPTIONS.md", "validation-designer": "VALIDATION.md",
                "promotion-gate": "GATE.md", "execution-bridge": "NEXT.md",
                "idea-retrospective": "RETROSPECTIVE.md"}
ROOT_REPORTS = {"triage-ideas": "PORTFOLIO.md", "portfolio-review": "REVIEWS.md",
                "cross-pollinate": "CROSS_POLLINATIONS.md", "idea-retrospective": "CALIBRATION.md"}
CORE = Path(__file__).resolve().parents[1]
DEFAULT_RESEARCH = {"model": None, "reasoning_effort": "low"}


class Blocked(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise Blocked(message)


def settings(root_override=None, core=CORE, environ=None):
    """Resolve private data independently of the checkout or current directory."""
    environ = os.environ if environ is None else environ
    config_path = core / "ideations.local.json"
    config = {}
    if config_path.exists():
        try:
            config = json.loads(config_path.read_text())
        except (ValueError, UnicodeError) as exc:
            raise Blocked("Invalid local configuration: " + str(config_path)) from exc
        require(isinstance(config, dict), "Local configuration must be an object")
        require(not (set(config) - {"workspace", "research"}), "Unknown local configuration key")
    research = config.get("research", {})
    require(isinstance(research, dict), "research must be an object")
    require(not (set(research) - set(DEFAULT_RESEARCH)), "Unknown research configuration key")
    research = {**DEFAULT_RESEARCH, **research}
    require(research["model"] is None or
            (isinstance(research["model"], str) and bool(research["model"].strip())),
            "research.model must be a model name or null")
    require(research["reasoning_effort"] in ("low", "medium", "high"),
            "research.reasoning_effort must be low, medium, or high")
    configured = config.get("workspace")
    if configured is not None:
        require(isinstance(configured, str) and bool(configured.strip()), "workspace must be a path")
    chosen = root_override or environ.get("IDEATIONS_WORKSPACE")
    if chosen:
        root = Path(chosen).expanduser().resolve()
    elif configured:
        root = Path(configured).expanduser()
        root = (root if root.is_absolute() else core / root).resolve()
    else:
        raise Blocked("Choose a workspace with --root, IDEATIONS_WORKSPACE, or ideations.local.json; see docs/quickstart.md")
    require(root.is_dir(), "Workspace does not exist: " + str(root))
    require(root != core.resolve() and core.resolve() not in root.parents,
            "Keep workspace data outside the core repository (including examples and fixtures)")
    return {"workspace": str(root), "research": research}


def ideas(root):
    """Only immediate, real directories with CONTEXT.md are ideas, never skills."""
    return sorted(p for p in root.iterdir() if p.is_dir() and not p.is_symlink()
                  and (p / "CONTEXT.md").is_file() and not (p / "SKILL.md").exists())


def idea_path(root, slug):
    require(bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug)), "Invalid idea slug")
    path = root / slug
    require(path in ideas(root), "Idea not found (requires CONTEXT.md, not SKILL.md)")
    return path


def records(path, tag):
    if not path.exists():
        return []
    require(not path.is_symlink(), "Refusing symlink: " + str(path))
    text = path.read_text()
    pattern = r"^```" + re.escape(tag) + r"\n(.*?)\n```[ \t]*$"
    blocks = re.findall(pattern, text, re.M | re.S)
    require(text.count("```" + tag) == len(blocks), "Malformed record fence: " + str(path))
    result = []
    for block in blocks:
        try:
            item = json.loads(block)
        except ValueError as exc:
            raise Blocked("Invalid JSON record in " + str(path)) from exc
        require(isinstance(item, dict), "Record must be an object")
        result.append(item)
    return result


def allowed(before, after):
    if before in TERMINAL:
        return False
    if before == "PARKED":
        return after in {"SEED", "REJECTED", "MERGED"}
    return after == FORWARD.get(before) or after in {"PARKED", "REJECTED", "MERGED"}


def state(path):
    entries = records(path / "STATE.md", "ideations-state")
    require(not (path / "STATE.md").exists() or bool(entries),
            "STATE.md exists without valid history: " + path.name)
    current = "SEED"
    for entry in entries:
        require(entry.get("from") == current and entry.get("to") in STATES
                and allowed(current, entry["to"]), "Invalid state history: " + path.name)
        require(all(isinstance(entry.get(k), str) and entry[k].strip()
                    for k in ("at", "reason", "decision")), "Incomplete state history: " + path.name)
        current = entry["to"]
    return current


def inventory(root):
    return {p.name: state(p) for p in ideas(root)}


def local_reference(path, reference):
    require(isinstance(reference, str) and reference.strip(), "Missing artifact reference")
    relative = reference.split("#", 1)[0]
    require(relative and not Path(relative).is_absolute(), "Use an idea-relative artifact reference")
    target = (path / relative).resolve()
    require(path.resolve() in target.parents and target.is_file(),
            "Missing or out-of-folder artifact: " + reference)
    require(bool(target.read_text().strip()), "Empty artifact: " + reference)
    return target


def evidence(path, identity, kind):
    matches = [r for r in records(path / "EVIDENCE.md", "ideations-evidence")
               if r.get("id") == identity]
    require(len(matches) == 1, "Evidence ID must exist exactly once: " + str(identity))
    item = matches[0]
    require(item.get("kind") == kind, "Expected evidence kind: " + kind)
    for key in ("id", "date", "summary", "source", "limitations"):
        require(isinstance(item.get(key), str) and item[key].strip(), "Evidence missing " + key)
    try:
        date.fromisoformat(item["date"])
    except ValueError as exc:
        raise Blocked("Evidence date must be YYYY-MM-DD") from exc
    source = item["source"]
    if not source.startswith(("https://", "http://", "conversation:")):
        local_reference(path, source)
    if kind in {"market", "external", "release"}:
        require(item.get("result") == "supports", "Evidence does not support this transition")
    if kind == "market":
        require(not source.startswith("conversation:"), "Market evidence needs a source page or local source notes")
        local_reference(path, "MARKET.md")
    if kind == "external":
        local_reference(path, item.get("assumption"))
        local_reference(path, item.get("experiment"))
        require(isinstance(item.get("threshold_result"), str) and item["threshold_result"].strip(),
                "External evidence needs observed results against the predeclared threshold")
    if kind == "release":
        require(isinstance(item.get("access"), str) and item["access"].strip(),
                "Release evidence needs an externally usable access location")
    return item


@contextmanager
def locked(root):
    # A directory lock avoids persistent lockfiles and serializes cooperating writers.
    import os
    descriptor = os.open(str(root), os.O_RDONLY)
    try:
        fcntl.flock(descriptor, fcntl.LOCK_EX)
        yield
    finally:
        fcntl.flock(descriptor, fcntl.LOCK_UN)
        os.close(descriptor)


def append(path, text, heading):
    require(not path.is_symlink(), "Refusing symlink: " + str(path))
    with path.open("a") as out:
        if path.stat().st_size == 0:
            out.write(heading + "\n")
        out.write("\n" + text.rstrip() + "\n")


def transition(root, slug, target, reason, evidence_id=None, decision_id=None,
               tradeoff=None, merge_target=None, apply=False):
    with locked(root):
        path = idea_path(root, slug)
        current = state(path)
        require(target in STATES and allowed(current, target),
                "Transition blocked: %s -> %s" % (current, target))
        require(bool(reason and reason.strip()), "A decision reason is required")
        for name in {
            "RESEARCHED": ["MARKET.md"],
            "VALIDATING": ["ASSUMPTIONS.md", "VALIDATION.md"],
            "PROMOTED": ["ASSUMPTIONS.md", "VALIDATION.md"],
        }.get(target, []):
            local_reference(path, name)
        kind = {"RESEARCHED": "market", "PROMOTED": "external", "SHIPPED": "release"}.get(target)
        if kind:
            evidence(path, evidence_id, kind)
        snapshot = inventory(root)
        if target in ACTIVE:
            others = {k: v for k, v in snapshot.items() if k != slug}
            require(sum(s in ACTIVE for s in others.values()) < 3,
                    "ACTIVE limit: explicitly park/reject/merge an active idea first: " +
                    ", ".join(k for k, v in others.items() if v in ACTIVE))
            require(sum(s == "BUILDING" for s in others.values()) + (target == "BUILDING") <= 1,
                    "BUILDING limit: finish or explicitly remove the current building idea first")
            if current not in ACTIVE:
                require(bool(tradeoff and tradeoff.strip()), "Name the work or idea displaced, even with free capacity")
        if target == "MERGED":
            require(merge_target != slug, "Cannot merge an idea into itself")
            destination = idea_path(root, merge_target or "")
            require(state(destination) not in TERMINAL, "Merge destination must not be terminal")
        if apply:
            decision = evidence(path, decision_id, "human-decision")
            require(decision.get("from") == current and decision.get("to") == target,
                    "Human decision must name this exact transition")
            intent = "start-building" if target == "BUILDING" else "change-state"
            require(decision.get("intent") == intent,
                    "Explicit human intent required: " + intent)
            event = {"at": datetime.now(timezone.utc).isoformat(), "from": current,
                     "to": target, "reason": reason, "decision": decision_id,
                     "evidence": evidence_id, "opportunity_cost": tradeoff,
                     "merge_target": merge_target}
            append(path / "STATE.md", "```ideations-state\n" +
                   json.dumps(event, indent=2) + "\n```", "# State history\n\nInitial state: SEED")
        return "%s -> %s: %s" % (current, target, "recorded" if apply else
                "structural checks passed; evidence review and human decision still required to apply")


def save_capture(root, slug, content, existing=None):
    """Semantic matching is the capture skill's job; an explicit match never creates a folder."""
    require(bool(content.strip()), "Capture is empty")
    with locked(root):
        if existing:
            path = idea_path(root, existing)
        else:
            require(bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug)), "Invalid slug")
            path = root / slug
            require(not path.exists(), "Folder already exists; inspect for duplicate mechanism")
            path.mkdir()
        append(path / "CONTEXT.md", content, "# " + path.name)
        return path


def append_report(root, skill, content, slug=None):
    """Append only the skill's declared report; never create idea folders or launch work."""
    require(bool(content.strip()), "Report is empty")
    with locked(root):
        if slug is not None:
            require(skill in IDEA_REPORTS, "This skill does not own an idea-level report")
            target = idea_path(root, slug) / IDEA_REPORTS[skill]
        else:
            require(skill in ROOT_REPORTS, "This skill requires an existing idea")
            target = root / ROOT_REPORTS[skill]
        append(target, content, "# " + target.stem.replace("_", " ").title())
        return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, help="Private workspace; overrides environment and local config")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("status")
    commands.add_parser("audit")
    commands.add_parser("settings", help="Show resolved workspace and research routing")
    capture = commands.add_parser("capture")
    capture.add_argument("slug")
    capture.add_argument("--content", type=Path, required=True)
    capture.add_argument("--existing", help="Use the mechanism match selected by the capture skill")
    report = commands.add_parser("append-report")
    report.add_argument("skill", choices=sorted(set(IDEA_REPORTS) | set(ROOT_REPORTS)))
    report.add_argument("--content", type=Path, required=True)
    report.add_argument("--idea", help="Existing idea slug for an idea-level report")
    gate = commands.add_parser("transition")
    gate.add_argument("slug")
    gate.add_argument("target", choices=sorted(STATES))
    gate.add_argument("--reason", required=True)
    gate.add_argument("--evidence")
    gate.add_argument("--decision")
    gate.add_argument("--tradeoff")
    gate.add_argument("--merge-target")
    gate.add_argument("--apply", action="store_true", help="Record a transition authorized by a human decision")
    args = parser.parse_args()
    try:
        resolved = settings(args.root)
        root = Path(resolved["workspace"])
        if args.command == "settings":
            print(json.dumps(resolved, indent=2))
        elif args.command in {"status", "audit"}:
            snapshot = inventory(root)
            for slug, current in snapshot.items():
                print("%s\t%s" % (slug, current))
            active = sum(s in ACTIVE for s in snapshot.values())
            building = sum(s == "BUILDING" for s in snapshot.values())
            print("ACTIVE %d/3; BUILDING %d/1" % (active, building))
            require(active <= 3 and building <= 1, "Portfolio limits exceeded")
        elif args.command == "capture":
            print(save_capture(root, args.slug, args.content.read_text(), args.existing))
        elif args.command == "append-report":
            print(append_report(root, args.skill, args.content.read_text(), args.idea))
        else:
            print(transition(root, args.slug, args.target, args.reason, args.evidence,
                             args.decision, args.tradeoff, args.merge_target, args.apply))
    except (Blocked, OSError) as exc:
        print("BLOCKED: " + str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
