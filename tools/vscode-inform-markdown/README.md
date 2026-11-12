# Inform Markdown

Colors Inform 7 code fences in the Markdown source editor using the installed
[Inform Ecosystem](https://marketplace.visualstudio.com/items?itemName=jeffnyman.inform-ecosystem-vscode)
grammar. Supports `inform7` and `i7` labels, backtick and tilde fences, and
case-insensitive language labels. Colors follow your VS Code theme.

This is a declarative grammar extension: no runtime JavaScript, commands,
network access, or copied Inform grammar. Inform Ecosystem is a required dependency.
It does not change Markdown preview, GitHub, or the published website.

## Install

Build from the repository root:

```powershell
uv run --project . python tools/vscode-inform-markdown/package_extension.py
```

In VS Code, choose **Extensions → ⋯ → Install from VSIX**, then select
`prototype/build/inform-markdown-0.1.0.vsix`. If the editor was already open,
run **Developer: Reload Window** afterward.

Open `places/README.md` in the text editor. Quoted descriptions and comments inside
the `inform7` fences should use the same colors as standalone Inform source.
Prose, other languages, and gameplay transcripts retain their usual highlighting.

## Test

The tests tokenize real Markdown with VS Code's TextMate and Oniguruma libraries,
using the actual installed Markdown and Inform Ecosystem grammars. With Node.js
and npm installed, run `npm ci` in this directory, then:

```powershell
node test/highlighting.cjs PATH_TO_VSCODE_RESOURCES_APP PATH_TO_INFORM_ECOSYSTEM_EXTENSION
```

An optional third argument points at a directory containing unpacked npm packages
at `vscode-textmate/package` and `vscode-oniguruma/package`, for environments
without npm. No development dependencies are included in the VSIX.
