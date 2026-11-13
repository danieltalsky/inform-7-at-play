# Static site themes

Build the complete site from the repository root:

```powershell
uv run --project . python site_builder.py
```

Open `dist/index.html` directly, or serve it locally:

```powershell
uv run --project . python -m http.server 8000 --directory dist --bind 127.0.0.1
```

Upload the contents of `dist` to the subdomain's document root. No Python or
Jinja installation is needed on the web server. Links also work in a subfolder.
The body copy and examples come from the chapter Markdown, in their original
order. Existing handwritten transcripts are preserved; this export does not
compile or regenerate gameplay. The wordmark currently loads Literata from
Google Fonts, with Cambria/serif fallbacks.

To create another theme, copy `themes/at-play` to another named directory and edit
its templates and assets. Select it with:

```powershell
uv run --project . python site_builder.py --theme my-theme --output dist-my-theme
```

`page.html` controls the shell and chapter navigation; `code.html` and
`transcript.html` control the paired examples. `assets/style.css` contains the
palette and typography. Jinja autoescaping is enabled; only generated markup
is marked safe. Chapter Markdown supports trusted inline HTML.

Every build checks internal file links and fragment targets. The exporter
overwrites its own files and copies theme assets; it does not delete the output
directory. Use a new output directory when changing theme asset names to avoid
carrying old, unused files into a deployment.

## Editorial TODOs

Use the exact marker `@TODO` followed by a note, in its own paragraph:

```markdown
@TODO Add an example of an enterable supporter.
```

The exporter removes that paragraph. If a heading's section contains only TODOs
(including nested TODO-only sections), it removes the heading and section too.
Sections end at the next heading of the same or a higher level. A heading with
`@TODO` explicitly hides its entire section, including prose, code, and subheadings:

```markdown
## @TODO Conversation examples

Draft content stays in the Markdown but is omitted from the export.
```

Put page-bottom planning lists under an `## @TODO ...` heading. Literal markers
inside inline code or fenced code are preserved. Completed prose next to a TODO
paragraph stays visible. This happens during export, so draft content is absent
from the generated HTML rather than merely hidden with CSS.
