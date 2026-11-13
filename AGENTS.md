# Working in this repository

## Main branch

`maestra` is this repository's main/default branch. References to "main" mean
`maestra`; do not create or rename a branch to `main`.

## Change workflow

The initial deployment setup may be committed directly to `maestra`. Once
deployment is in place, use feature branches and pull requests targeting
`maestra` for subsequent changes; do not push directly unless explicitly asked.

## Inform 7 reference

Before answering Inform questions or editing Inform examples, read
[the compact reference](references/inform7/README.md). Read only the additional
file relevant to the task:

- [Language scope](references/inform7/scope.md): independent capability map;
  use for “what is missing?” reviews, without assuming every feature belongs in
  an introductory explanation.
- [Troubleshooting](references/inform7/troubleshooting.md): symptoms, causes,
  fixes, and exact documentation sections.
- [Source map](references/inform7/sources.md): installed official manuals,
  official website, community guides, extensions, and selected game sources.

Use these notes first, then the relevant official section. The installed
documentation and Standard Rules may be read directly; their paths are in the
source map. Check subtle claims against the version actually compiled:
[prototype/toolchain.json](prototype/toolchain.json) currently pins Inform
10.1.2 / Inform 6 6.41. Historical books, forum posts, extensions, and games
are not automatically compatible. Do not upgrade the toolchain to fit an example.

Aaron Reed's local book, if present, has navigation at
`references/aaron-reed/topics.md` and `index.md`. Read targeted pages only.
That directory is gitignored private research material; do not commit or publish
the book or its extraction. Write original explanations and examples.

For executable chapter examples, follow [prototype/README.md](prototype/README.md):
preserve sample IDs, update catalog recipes when needed, compile/play the changed
example, and regenerate affected transcripts rather than inventing output.
Distinguish verified behavior from an untested suggestion. Keep reference updates
compressed, source-linked, and specific to reusable language knowledge.

## Python execution

- Run Python only through `uv` in the current project's `.venv`.
- Use `uv run --project . python ...` from the project root.
- Never invoke `python`, `python3`, `py`, or a `.venv` interpreter directly.
- If the project has no `pyproject.toml` or `.venv`, set up the environment with
  `uv` before running Python.
- If uv's default cache is inaccessible, set
  `$env:UV_CACHE_DIR = "$PWD/.uv-cache"` in PowerShell.
