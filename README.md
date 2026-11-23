# Inform 7 at Play

An illustrated guide to Inform 7, with examples of source code and actual play.

**[Read the book online](https://informatplay.danieltalsky.com/)** or browse
[the book source](book/README.md).

## Working on the book

- [book/](book/README.md) contains the homepage and chapters, including Inform
  source examples, capture recipes, and generated gameplay transcripts.
- [publishing/](publishing/README.md) builds the website and contains its themes,
  assets, and deployment scripts.
- [prototype/](prototype/README.md) compiles and plays the Inform examples and
  regenerates transcripts.
- [CONTRIBUTING.md](CONTRIBUTING.md) explains the repository layout and workflows.

Build the website from the repository root with [uv](https://docs.astral.sh/uv/):

```powershell
uv run --project . --group publishing python -m publishing.build
```

Open `dist/index.html` to preview the result. The website build uses the existing
chapter transcripts; see the example pipeline guide when changing Inform source.
