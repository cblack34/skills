from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from bump_plugin_version import SemVer, update_plugin_version  # noqa: E402


class BumpPluginVersionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.plugins_root = Path(self.temporary_directory.name) / "plugins"
        self.plugin = "example-plugin"
        self.plugin_root = self.plugins_root / self.plugin
        self.paths = (
            self.plugin_root / ".claude-plugin" / "plugin.json",
            self.plugin_root / ".codex-plugin" / "plugin.json",
        )
        for path in self.paths:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                json.dumps(
                    {
                        "name": self.plugin,
                        "version": "1.2.3",
                        "description": "Example",
                    },
                    indent=2,
                )
                + "\n",
                encoding="utf-8",
            )

    def versions(self) -> list[str]:
        return [
            json.loads(path.read_text(encoding="utf-8"))["version"]
            for path in self.paths
        ]

    def test_minor_bump_updates_both_manifests(self) -> None:
        current, target, _ = update_plugin_version(
            self.plugins_root, self.plugin, "minor"
        )

        self.assertEqual((current, target), ("1.2.3", "1.3.0"))
        self.assertEqual(self.versions(), ["1.3.0", "1.3.0"])

    def test_explicit_prerelease_is_supported(self) -> None:
        update_plugin_version(self.plugins_root, self.plugin, "2.0.0-beta.1")

        self.assertEqual(self.versions(), ["2.0.0-beta.1", "2.0.0-beta.1"])

    def test_dry_run_does_not_write(self) -> None:
        current, target, _ = update_plugin_version(
            self.plugins_root, self.plugin, "patch", dry_run=True
        )

        self.assertEqual((current, target), ("1.2.3", "1.2.4"))
        self.assertEqual(self.versions(), ["1.2.3", "1.2.3"])

    def test_mismatched_versions_are_rejected_without_writing(self) -> None:
        manifest = json.loads(self.paths[1].read_text(encoding="utf-8"))
        manifest["version"] = "1.2.4"
        self.paths[1].write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "manifest versions disagree"):
            update_plugin_version(self.plugins_root, self.plugin, "minor")

        self.assertEqual(self.versions(), ["1.2.3", "1.2.4"])

    def test_same_version_and_downgrade_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "already at version"):
            update_plugin_version(self.plugins_root, self.plugin, "1.2.3")
        with self.assertRaisesRegex(ValueError, "refusing to downgrade"):
            update_plugin_version(self.plugins_root, self.plugin, "1.2.2")

        self.assertEqual(self.versions(), ["1.2.3", "1.2.3"])

    def test_semver_prerelease_precedence(self) -> None:
        beta_2 = SemVer.parse("1.0.0-beta.2")
        beta_11 = SemVer.parse("1.0.0-beta.11")
        release = SemVer.parse("1.0.0")

        self.assertLess(beta_2.compare_precedence(beta_11), 0)
        self.assertLess(beta_11.compare_precedence(release), 0)


if __name__ == "__main__":
    unittest.main()
