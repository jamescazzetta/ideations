# Migrating an existing portfolio

The core and workspace are separate roots. The core contains skills and tooling; the workspace contains immediate idea directories and root reports. Keep the workspace outside the core, ideally as a sibling when existing notes link to sibling development repositories.

1. Inventory immediate real directories with CONTEXT.md and no SKILL.md. Do not recursively collect examples, research or application fixtures.
2. Record original file hashes, state history and paths. Preserve original notes, human annotations, nested repositories, untracked files, symlinks and archives.
3. Move each idea directory intact. Move PORTFOLIO.md, REVIEWS.md, CROSS_POLLINATIONS.md, CALIBRATION.md and private FOUNDER.md when present. Classify unrelated application trees and backups explicitly; do not turn them into ideas or delete duplicates by assumption.
4. Prefer same-filesystem renames. Verify the moved entries and original document hashes, keeping a private journal of old/new paths and any adjusted symlinks. Stop on collisions or failed verification.
5. Configure the core's ignored local workspace setting. Update host/parent instruction references to `skills/<name>/SKILL.md` and the new workspace. Preserve historical prose; document path mappings and use private compatibility aliases where needed.
6. Run status/audit against the new workspace and compare inventories. An absent STATE.md remains SEED even if the folder contains a released app. Migration never creates evidence or transitions.

Moving folders is not a Git history migration: preserve each nested .git directory with its project. Do not initialize the public core around private data. Before the first commit, explicitly review the staged file list; .gitignore is not a substitute for selecting the intended files.

The helper has no shadow index to rebuild. To relocate an existing workspace again, move it intact and update the local path, then check relative links and host instructions. Keep migration journals private because they contain local paths and project inventories.
