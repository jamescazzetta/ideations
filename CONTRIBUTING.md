# Contributing

Read README.md and docs/CONTRACT.md first. Keep the core small and filesystem-based. Skills belong in `skills/`; portfolio data belongs in a separate workspace. Each report has one owner. Preserve append-only history and the distinction between hypotheses, external observations and human decisions.

Run the standard-library suite from the core:

```sh
python3 -m unittest discover -s tests -v
```

Tests use temporary workspaces and fictional observations. Never run fixtures against a personal portfolio or create real external actions from tests. For skill changes, also review the relevant semantic cases in tests/SCENARIOS.md; structural tests cannot establish whether an agent judges evidence correctly.

Explain the changed behavior, why it matters and what was verified. Avoid new dependencies, services or lifecycle states unless they solve a concrete problem. Changes to layout, record formats or ownership need matching docs and meaningful behavioral tests. Preserve state limits and explicit authorization boundaries.

CI runs on Linux and macOS. The directory lock uses POSIX flock; native Windows is not currently supported. No credentials or network access are required for tests.

The CI setup follows GitHub's [Python workflow guidance](https://docs.github.com/en/actions/tutorials/build-and-test-code/python).
