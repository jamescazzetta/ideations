"""Real filesystem tests; every observation/decision here is fictional test data."""
import importlib.util
import json
from pathlib import Path
import tempfile
import subprocess
import sys
import unittest

SPEC = importlib.util.spec_from_file_location("portfolio", Path(__file__).parents[1] / "scripts/portfolio.py")
p = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(p)


class PortfolioTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.idea = self.make("alpha")

    def make(self, slug):
        path = self.root / slug
        path.mkdir()
        (path / "CONTEXT.md").write_text("# Original user idea\nUser annotation: KEEP EXACTLY.\n")
        return path

    def record(self, idea, identity, kind, **extra):
        item = {"id": identity, "kind": kind, "date": "2026-09-09",
                "summary": "FICTIONAL test observation", "source": "conversation:fictional test",
                "limitations": "Synthetic fixture, not real evidence"}
        item.update(extra)
        p.append(idea / "EVIDENCE.md", "```ideations-evidence\n" + json.dumps(item) + "\n```", "# Evidence")

    def prepare(self, idea, target):
        before = p.state(idea)
        decision = before + "-" + target
        self.record(idea, decision, "human-decision", **{
            "from": before, "to": target,
            "intent": "start-building" if target == "BUILDING" else "change-state"})
        identity = None
        if target == "RESEARCHED":
            (idea / "MARKET.md").write_text("# Market\nFictional source notes.")
            identity = "M1"
            self.record(idea, identity, "market", source="MARKET.md", result="supports")
        if target == "VALIDATING":
            (idea / "ASSUMPTIONS.md").write_text("# Assumptions\n## A1\nA falsifiable test claim.")
            (idea / "VALIDATION.md").write_text("# Plan\n## V1\nPredeclared threshold.")
        if target == "PROMOTED":
            identity = "E1"
            self.record(idea, identity, "external", result="supports", assumption="ASSUMPTIONS.md#a1",
                        experiment="VALIDATION.md#v1", threshold_result="FICTIONAL threshold met")
        if target == "SHIPPED":
            identity = "R1"
            self.record(idea, identity, "release", result="supports", access="https://example.invalid/release")
        return decision, identity

    def move(self, idea, target, **kwargs):
        decision, identity = self.prepare(idea, target)
        return p.transition(self.root, idea.name, target, "Fictional test decision", identity,
                            decision, apply=True, **kwargs)

    def advance(self, idea, target):
        while p.state(idea) != target:
            self.move(idea, p.FORWARD[p.state(idea)], tradeoff="Forego another fictional test")

    def test_legacy_defaults_ignore_documentation_volume(self):
        (self.idea / "MARKET.md").write_text("Validated! " * 500)
        self.assertEqual(p.state(self.idea), "SEED")
        self.assertEqual(p.inventory(self.root), {"alpha": "SEED"})

    def test_skills_and_nested_fixtures_are_not_ideas(self):
        skill = self.make("skill")
        (skill / "SKILL.md").write_text("Skill")
        nested = self.root / "tests" / "fixture"
        nested.mkdir(parents=True)
        (nested / "CONTEXT.md").write_text("Fake")
        self.assertEqual(list(p.inventory(self.root)), ["alpha"])

    def test_matched_capture_preserves_original_and_no_new_folder(self):
        before = (self.idea / "CONTEXT.md").read_bytes()
        p.save_capture(self.root, "different-title", "Dated development", existing="alpha")
        self.assertFalse((self.root / "different-title").exists())
        self.assertTrue((self.idea / "CONTEXT.md").read_bytes().startswith(before))

    def test_colliding_slug_cannot_overwrite(self):
        with self.assertRaises(p.Blocked):
            p.save_capture(self.root, "alpha", "Replacement")
        self.assertIn("KEEP EXACTLY", (self.idea / "CONTEXT.md").read_text())

    def test_market_failure_cannot_roll_back_capture(self):
        saved = p.save_capture(self.root, "beta", "Original captured thought")
        try:
            raise RuntimeError("Simulated unavailable research service")
        except RuntimeError:
            pass
        self.assertTrue((saved / "CONTEXT.md").exists())
        self.assertEqual(p.state(saved), "SEED")

    def test_missing_market_evidence_blocks_and_does_not_write_state(self):
        with self.assertRaises(p.Blocked):
            p.transition(self.root, "alpha", "RESEARCHED", "Try")
        self.assertFalse((self.idea / "STATE.md").exists())

    def test_no_skipping_forward_gates(self):
        for target in ("VALIDATING", "PROMOTED", "BUILDING", "SHIPPED"):
            with self.assertRaises(p.Blocked):
                p.transition(self.root, "alpha", target, "Skip")

    def test_missing_plan_blocks_validation(self):
        self.advance(self.idea, "RESEARCHED")
        with self.assertRaises(p.Blocked):
            p.transition(self.root, "alpha", "VALIDATING", "Try", tradeoff="Other work")

    def test_promotion_requires_external_support_not_market_or_enthusiasm(self):
        self.advance(self.idea, "VALIDATING")
        for identity in (None, "M1"):
            with self.assertRaises(p.Blocked):
                p.transition(self.root, "alpha", "PROMOTED", "Try", identity)
        self.record(self.idea, "bad", "external", result="inconclusive")
        with self.assertRaises(p.Blocked):
            p.transition(self.root, "alpha", "PROMOTED", "Try", "bad")
        self.assertEqual(p.state(self.idea), "VALIDATING")

    def test_building_needs_specific_human_intent(self):
        self.advance(self.idea, "PROMOTED")
        with self.assertRaises(p.Blocked):
            p.transition(self.root, "alpha", "BUILDING", "Try", apply=True)
        self.record(self.idea, "wrong", "human-decision", **{
            "from": "PROMOTED", "to": "BUILDING", "intent": "change-state"})
        with self.assertRaises(p.Blocked):
            p.transition(self.root, "alpha", "BUILDING", "Try", decision_id="wrong", apply=True)
        self.assertEqual(p.state(self.idea), "PROMOTED")

    def test_readiness_check_is_read_only_and_build_gate_never_implements(self):
        self.advance(self.idea, "PROMOTED")
        before = (self.idea / "STATE.md").read_bytes()
        p.transition(self.root, "alpha", "BUILDING", "Check")
        self.assertEqual(before, (self.idea / "STATE.md").read_bytes())
        files = set(self.idea.iterdir())
        self.move(self.idea, "BUILDING")
        self.assertEqual(files, set(self.idea.iterdir()))

    def test_capacity_and_explicit_exit(self):
        self.advance(self.idea, "VALIDATING")
        for slug in ("beta", "gamma"):
            self.advance(self.make(slug), "VALIDATING")
        fourth = self.make("delta")
        self.advance(fourth, "RESEARCHED")
        with self.assertRaisesRegex(p.Blocked, "ACTIVE limit"):
            self.move(fourth, "VALIDATING", tradeoff="alpha")
        self.move(self.idea, "PARKED")
        # Reuse the unchanged real decision rather than creating a duplicate record.
        p.transition(self.root, "delta", "VALIDATING", "Slot freed", decision_id="RESEARCHED-VALIDATING",
                     tradeoff="alpha is now parked", apply=True)
        self.assertEqual(sum(s in p.ACTIVE for s in p.inventory(self.root).values()), 3)

    def test_single_building_limit(self):
        self.advance(self.idea, "BUILDING")
        second = self.make("beta")
        self.advance(second, "PROMOTED")
        with self.assertRaisesRegex(p.Blocked, "BUILDING limit"):
            self.move(second, "BUILDING")

    def test_free_capacity_still_requires_opportunity_cost(self):
        self.advance(self.idea, "RESEARCHED")
        with self.assertRaisesRegex(p.Blocked, "displaced"):
            self.move(self.idea, "VALIDATING")

    def test_annotations_survive_state_and_evidence_updates(self):
        self.advance(self.idea, "RESEARCHED")
        for filename in ("STATE.md", "EVIDENCE.md"):
            with (self.idea / filename).open("a") as out:
                out.write("\nHuman annotation: KEEP EXACTLY.\n")
        before = {f: (self.idea / f).read_bytes() for f in ("STATE.md", "EVIDENCE.md")}
        self.move(self.idea, "VALIDATING", tradeoff="Other work")
        for filename, text in before.items():
            self.assertTrue((self.idea / filename).read_bytes().startswith(text))

    def test_terminal_states_and_reactivation(self):
        self.move(self.idea, "PARKED")
        with self.assertRaises(p.Blocked):
            p.transition(self.root, "alpha", "PROMOTED", "Cannot jump")
        self.move(self.idea, "SEED")
        self.move(self.idea, "REJECTED")
        with self.assertRaises(p.Blocked):
            p.transition(self.root, "alpha", "SEED", "No automatic resurrection")

    def test_merge_requires_distinct_nonterminal_target_and_preserves_both(self):
        other = self.make("beta")
        for destination in (None, "alpha", "missing"):
            with self.assertRaises(p.Blocked):
                p.transition(self.root, "alpha", "MERGED", "Try", merge_target=destination)
        before = (self.idea / "CONTEXT.md").read_bytes()
        self.move(self.idea, "MERGED", merge_target="beta")
        self.assertEqual(before, (self.idea / "CONTEXT.md").read_bytes())
        self.assertTrue((other / "CONTEXT.md").exists())
        with self.assertRaises(p.Blocked):
            p.transition(self.root, "beta", "MERGED", "Terminal target", merge_target="alpha")

    def test_shipped_requires_release_evidence_and_releases_slot(self):
        self.advance(self.idea, "BUILDING")
        with self.assertRaises(p.Blocked):
            p.transition(self.root, "alpha", "SHIPPED", "Architecture completed")
        self.move(self.idea, "SHIPPED")
        self.assertNotIn(p.state(self.idea), p.ACTIVE)
        with self.assertRaises(p.Blocked):
            p.transition(self.root, "alpha", "BUILDING", "Restart")

    def test_malformed_state_fails_closed(self):
        for text in ("", "State: PROMOTED", "```ideations-state\n{broken}\n```",
                     '```ideations-state\n{"from":"SEED","to":"BUILDING"}\n```'):
            (self.idea / "STATE.md").write_text(text)
            with self.assertRaises(p.Blocked):
                p.inventory(self.root)

    def test_duplicate_evidence_and_outside_refs_fail_closed(self):
        self.prepare(self.idea, "RESEARCHED")
        self.record(self.idea, "M1", "market", source="MARKET.md", result="supports")
        with self.assertRaises(p.Blocked):
            p.evidence(self.idea, "M1", "market")
        outside = self.root / "outside.md"
        outside.write_text("Not this idea's evidence")
        with self.assertRaises(p.Blocked):
            p.local_reference(self.idea, "../outside.md")

    def test_missing_idea_does_not_create_artifacts(self):
        with self.assertRaises(p.Blocked):
            p.transition(self.root, "absent", "RESEARCHED", "Try")
        self.assertFalse((self.root / "absent").exists())

    def test_concurrent_admission_cannot_take_same_last_slot(self):
        self.advance(self.idea, "VALIDATING")
        self.advance(self.make("beta"), "VALIDATING")
        processes = []
        for slug in ("gamma", "delta"):
            candidate = self.make(slug)
            self.advance(candidate, "RESEARCHED")
            self.prepare(candidate, "VALIDATING")
        for slug in ("gamma", "delta"):
            command = [sys.executable, str(Path(p.__file__)), "--root", str(self.root),
                       "transition", slug, "VALIDATING", "--reason", "Fictional admission",
                       "--decision", "RESEARCHED-VALIDATING", "--tradeoff", "Other work", "--apply"]
            processes.append(subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
        outputs = [proc.communicate(timeout=10) for proc in processes]
        self.assertEqual(sorted(proc.returncode for proc in processes), [0, 1], outputs)
        self.assertEqual(sum(s in p.ACTIVE for s in p.inventory(self.root).values()), 3)

    def test_symlink_output_cannot_overwrite_another_artifact(self):
        target = self.root / "protected.md"
        target.write_text("Human content")
        (self.idea / "EVIDENCE.md").symlink_to(target)
        with self.assertRaises(p.Blocked):
            p.append(self.idea / "EVIDENCE.md", "Overwrite", "# Evidence")
        self.assertEqual(target.read_text(), "Human content")

    def test_cross_pollination_can_only_append_root_report(self):
        before = set(self.root.iterdir())
        p.append_report(self.root, "cross-pollinate", "## Candidate\nFICTIONAL connection; human review required.")
        self.assertEqual(set(self.root.iterdir()) - before, {self.root / "CROSS_POLLINATIONS.md"})
        with self.assertRaises(p.Blocked):
            p.append_report(self.root, "cross-pollinate", "Forbidden idea output", "alpha")
        self.assertEqual(p.inventory(self.root), {"alpha": "SEED"})

    def test_report_refresh_preserves_human_annotations_and_history(self):
        path = p.append_report(self.root, "validation-designer", "## V1\nOriginal threshold.", "alpha")
        with path.open("a") as out:
            out.write("\nHuman annotation: do not redefine success.\n")
        before = path.read_bytes()
        p.append_report(self.root, "validation-designer", "## V2\nSupersedes V1 after failed trial.", "alpha")
        self.assertTrue(path.read_bytes().startswith(before))
        with self.assertRaises(p.Blocked):
            p.append_report(self.root, "red-team-idea", "No context", "missing")
        self.assertFalse((self.root / "missing").exists())

    def test_reports_do_not_launch_downstream_work(self):
        p.append_report(self.root, "market-check", "Partial scan", "alpha")
        self.assertEqual({f.name for f in self.idea.iterdir()}, {"CONTEXT.md", "MARKET.md"})
        p.append_report(self.root, "red-team-idea", "Provisional challenge", "alpha")
        self.assertEqual({f.name for f in self.idea.iterdir()}, {"CONTEXT.md", "MARKET.md", "CHALLENGE.md"})


if __name__ == "__main__":
    unittest.main()
