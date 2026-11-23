# Working on Inform 7 at Play

The `book/` directory contains the book. The public site is
https://informatplay.danieltalsky.com/.

## Repository layout

| Location | Purpose |
| --- | --- |
| `README.md` | Project overview and links for readers and authors |
| `book/` | Book homepage, chapters, Inform source, example recipes, and generated chapter transcripts |
| `publishing/` | Website exporter, themes, assets, tests, and FTPS deployment |
| `prototype/` | Inform compilation, gameplay capture, transcript rendering, and sample gallery |
| `references/` | Inform language reference notes for authors |
| `tools/` | Authoring utilities, including the VS Code extension |
| `.github/workflows/` | Automated verification and publishing orchestration |
| `pyproject.toml`, `uv.lock` | Shared Python environment and pinned dependencies |

## Choose the task

For prose, edit the chapter Markdown in `book/`. For source examples, also edit the adjacent
recipe and follow the [example pipeline guide](prototype/README.md) to compile,
play, and regenerate affected transcripts. Preserve sample IDs and review generated
diffs. Generated transcript regions should not be edited by hand.

For website layout, styling, navigation, or HTML export, follow the
[publishing guide](publishing/README.md). A site build uses the existing chapter
transcripts and needs no Inform installation. Theme instructions are in
[publishing/themes](publishing/themes/README.md); hosting instructions are in
[publishing/deploy](publishing/deploy/README.md).

Use `uv run --project . python ...` from the repository root for Python commands,
adding `--group publishing` for website commands or `--group build` when building
the console interpreter. The generated website goes to ignored `dist/`; compiler
downloads, captures, logs, and the sample gallery go to ignored `prototype/build/`.

Use feature branches and pull requests targeting `maestra`. CI verifies the site
and examples independently; deployment requires both jobs to pass. See
[AGENTS.md](AGENTS.md) for repository instructions used by coding agents.
