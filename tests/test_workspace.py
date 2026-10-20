"""Workspace isolation, portability and report ownership, using temporary files only."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from test_portfolio import p


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name).resolve()
        self.core = self.base / "core"
        self.core.mkdir()
        self.workspace = self.base / "private"
        self.workspace.mkdir()

    def config(self, **values):
        (self.core / "ideations.local.json").write_text(json.dumps(values))

    def test_missing_configuration_never_defaults_to_core(self):
        with self.assertRaisesRegex(p.Blocked, "Choose a workspace"):
            p.settings(core=self.core, environ={})
        self.assertEqual(list(self.core.iterdir()), [])

    def test_relative_config_and_override_precedence(self):
        self.config(workspace="../private", research={"model": "inexpensive-worker", "reasoning_effort": "low"})
        resolved = p.settings(core=self.core, environ={})
        self.assertEqual(resolved["workspace"], str(self.workspace))
        self.assertEqual(resolved["research"]["model"], "inexpensive-worker")
        alternate = self.base / "alternate"
        alternate.mkdir()
        env = {"IDEATIONS_WORKSPACE": str(alternate)}
        self.assertEqual(p.settings(core=self.core, environ=env)["workspace"], str(alternate))
        self.assertEqual(p.settings(self.workspace, core=self.core, environ=env)["workspace"], str(self.workspace))

    def test_bad_config_fails_closed(self):
        for raw in ("not json", "[]", '{"workspace": 12}', '{"research": {"model": []}}',
                    '{"research": {"reasoning_effort": "unbounded"}}', '{"workspcae": "../private"}'):
            (self.core / "ideations.local.json").write_text(raw)
            with self.assertRaises(p.Blocked):
                p.settings(self.workspace, core=self.core, environ={})

    def test_core_examples_and_symlink_alias_cannot_be_workspace(self):
        nested = self.core / "examples"
        nested.mkdir()
        alias = self.base / "alias"
        alias.symlink_to(nested, target_is_directory=True)
        for candidate in (self.core, nested, alias):
            with self.assertRaisesRegex(p.Blocked, "outside the core"):
                p.settings(candidate, core=self.core, environ={})

    def test_nonexistent_workspace_is_not_created(self):
        missing = self.base / "missing"
        with self.assertRaisesRegex(p.Blocked, "does not exist"):
            p.settings(missing, core=self.core, environ={})
        self.assertFalse(missing.exists())

    def test_cli_from_another_directory_uses_config_and_keeps_core_clean(self):
        scripts = self.core / "scripts"
        scripts.mkdir()
        helper = scripts / "portfolio.py"
        shutil.copy2(p.__file__, helper)
        self.config(workspace="../private")
        draft = self.base / "draft.md"
        draft.write_text("# Fictional idea\nHuman annotation: preserve exactly.\n")
        env = {k: v for k, v in os.environ.items() if k != "IDEATIONS_WORKSPACE"}
        result = subprocess.run([sys.executable, str(helper), "capture", "alpha", "--content", str(draft)],
                                cwd=self.base, env=env, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Human annotation", (self.workspace / "alpha/CONTEXT.md").read_text())
        self.assertFalse((self.core / "alpha").exists())
        self.assertEqual(p.inventory(self.workspace), {"alpha": "SEED"})

    def test_moved_workspace_retains_history_and_ignores_supporting_trees(self):
        idea = p.save_capture(self.workspace, "alpha", "Original bytes and human note")
        original = (idea / "CONTEXT.md").read_bytes()
        nested = self.workspace / "projects/not-an-idea"
        nested.mkdir(parents=True)
        (nested / "CONTEXT.md").write_text("Nested project fixture")
        (self.workspace / "old-name").symlink_to("alpha", target_is_directory=True)
        moved = self.base / "relocated"
        self.workspace.rename(moved)
        self.config(workspace="../relocated")
        resolved = Path(p.settings(core=self.core, environ={})["workspace"])
        self.assertEqual(p.inventory(resolved), {"alpha": "SEED"})
        self.assertEqual((resolved / "alpha/CONTEXT.md").read_bytes(), original)

    def test_offer_is_append_only_and_never_opens_an_active_slot(self):
        idea = p.save_capture(self.workspace, "alpha", "Original proposal")
        offer = p.append_report(self.workspace, "offer-design", "## O1\nPrice is a hypothesis.", "alpha")
        with offer.open("a") as output:
            output.write("\nHuman annotation: do not promise an outcome.\n")
        original = offer.read_bytes()
        p.append_report(self.workspace, "offer-design", "## O2\nRevised scoped pilot.", "alpha")
        self.assertTrue(offer.read_bytes().startswith(original))
        self.assertEqual({f.name for f in idea.iterdir()}, {"CONTEXT.md", "OFFER.md"})
        self.assertEqual(p.state(idea), "SEED")
        with self.assertRaises(p.Blocked):
            p.append_report(self.workspace, "offer-design", "Wrong scope")
        with self.assertRaises(p.Blocked):
            p.append_report(self.workspace, "offer-design", "Missing context", "absent")


if __name__ == "__main__":
    unittest.main()
