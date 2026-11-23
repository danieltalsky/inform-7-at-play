# Publishing the website

This directory turns the Markdown in `book/` into the public website. It reads the
transcripts already in the chapters; it does not install Inform, compile stories,
or regenerate gameplay. Those tasks live in [the example pipeline](../prototype/README.md).

Run commands from the repository root with [uv](https://docs.astral.sh/uv/):

```powershell
uv run --project . --group publishing python -m publishing.build
uv run --project . --group publishing python -m unittest publishing.test_builder
```

The build writes `dist/` and checks every internal link and fragment. Open
`dist/index.html` directly, or serve it:

```powershell
uv run --project . python -m http.server 8000 --directory dist --bind 127.0.0.1
```

The `publishing` dependency group adds the Markdown and HTML parsers. The optional
`build` group belongs to the Inform interpreter compiler and is not needed here.
Both pipelines share one root Python environment and lockfile.

`book/README.md` becomes `dist/index.html`, and `book/things/README.md` becomes
`dist/things/index.html`. The source directory does not appear in public URLs.

## Where things belong

- [build.py](build.py): Markdown export, highlighting, navigation, and link validation.
- [themes/](themes/README.md): Jinja templates, CSS, fonts, and checked-in favicons.
- [generate_favicons.ps1](generate_favicons.ps1): Windows favicon asset generator.
- [deploy/](deploy/README.md): FTPS scripts, mirror tests, and hosting configuration instructions.
- [test_builder.py](test_builder.py): site export tests.

The [Verify and publish workflow](../.github/workflows/verify-and-publish.yml)
runs site checks and Inform-example checks in independent jobs. Deployment waits
for both, then publishes the exact `static-site` artifact produced by the site job.
Pull requests run checks; eligible `maestra` runs deploy when enabled.
