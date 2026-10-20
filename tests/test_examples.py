"""Replay invented examples structurally; these tests do not judge evidence truth."""
from pathlib import Path
import re
import shutil
import tempfile
import unittest
from urllib.parse import unquote

from test_portfolio import p

CORE = Path(__file__).resolve().parents[1]


class ExampleTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def copy(self, slug):
        destination = self.root / slug
        shutil.copytree(CORE / "examples" / slug, destination)
        return destination

    def test_histories_replay_through_structural_gates(self):
        for slug, final in (("booking-recovery", "SHIPPED"), ("invoice-reminder", "PARKED")):
            idea = self.copy(slug)
            events = p.records(idea / "STATE.md", "ideations-state")
            (idea / "STATE.md").unlink()  # Reset only a temporary fictional fixture.
            for event in events:
                p.transition(self.root, slug, event["to"], event["reason"], event["evidence"],
                             event["decision"], event["opportunity_cost"], event["merge_target"], apply=True)
            self.assertEqual(p.state(idea), final)
        self.assertFalse(any(s in p.ACTIVE for s in p.inventory(self.root).values()))

    def test_failed_offer_cannot_be_promoted(self):
        idea = self.copy("invoice-reminder")
        events = p.records(idea / "STATE.md", "ideations-state")
        (idea / "STATE.md").unlink()
        for event in events[:2]:
            p.transition(self.root, idea.name, event["to"], event["reason"], event["evidence"],
                         event["decision"], event["opportunity_cost"], apply=True)
        before = (idea / "STATE.md").read_bytes()
        with self.assertRaisesRegex(p.Blocked, "does not support"):
            p.transition(self.root, idea.name, "PROMOTED", "Try the failed fixture", "E1")
        self.assertEqual((idea / "STATE.md").read_bytes(), before)

    def test_shipped_customer_plan_never_reopens_state_or_creates_evidence(self):
        idea = self.copy("booking-recovery")
        originals = {name: (idea / name).read_bytes() for name in ("STATE.md", "EVIDENCE.md")}
        p.append_report(self.root, "execution-bridge", "## FICTIONAL proposal\nOne outcome conversation; NOT RUN.", idea.name)
        for name, original in originals.items():
            self.assertEqual((idea / name).read_bytes(), original)
        with self.assertRaises(p.Blocked):
            p.transition(self.root, idea.name, "BUILDING", "New features disguised as retention")

    def test_core_markdown_file_links_resolve(self):
        files = [CORE / "README.md", CORE / "AGENTS.md", CORE / "CONTRIBUTING.md"]
        for directory in ("docs", "skills", "examples", "templates"):
            files.extend((CORE / directory).rglob("*.md"))
        for path in files:
            for raw in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                target = unquote(raw.split("#", 1)[0])
                if not target or "://" in target or target.startswith("mailto:"):
                    continue
                with self.subTest(file=str(path.relative_to(CORE)), target=target):
                    self.assertTrue((path.parent / target).exists(), "Broken local Markdown link")


if __name__ == "__main__":
    unittest.main()
