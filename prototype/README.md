# Executable documentation prototype

This prototype compiles examples from the documentation and generates transcripts
from actual gameplay. Read [the generated page](generated.md) for the result.

## Setup

Install [uv](https://docs.astral.sh/uv/) and
[Inform for Windows](https://github.com/DavidKinder/Windows-Inform7/releases).
The recipe currently requires Inform 7 **10.1.2** and Inform 6 **6.41**, matching
the installed February 2026.2 Windows package. The runner checks both versions.

From the repository root, build the console interpreter once:

```powershell
uv run --project . --group build python prototype/build_interpreter.py
```

This downloads pinned [Glulxe](https://github.com/erkyrath/glulxe) and
[CheapGlk](https://github.com/erkyrath/cheapglk) source archives, verifies their
SHA-256 checksums, and builds a local executable. The optional build dependency
is Zig 0.15.2, installed inside the project environment by uv; no system-wide C
compiler is needed. See [toolchain.json](toolchain.json) and the uv lockfile for
the pins. The archives retain the upstream MIT license files.

The first setup downloads roughly 90 MB for the compiler. Subsequent interpreter
builds reuse the downloaded archives and compiler cache. Normal transcript runs
use only the Python standard library and the already-built executables.

## Generate and check

```powershell
uv run --project . python prototype/run.py
uv run --project . python prototype/run.py --check
uv run --project . python -m unittest discover -s prototype -p test_runner.py
```

The first command updates [generated.md](generated.md) and the selected transcript
region in the opening section of [Making Places](../places/README.md). The second
independently compiles and plays all examples, checks expected response fragments,
and fails if either output differs, without editing files. Review generated diffs
before accepting intentional changes.

Compiler errors, interpreter errors, timeouts, missing responses, and unexpected
input boundaries fail the run. Compiler logs, instrumented source, compiled stories,
raw console output, and formatted transcripts remain under ignored `prototype/build/`.

Inform defaults to `C:\Program Files\Inform`. Use `--inform 'D:\Apps\Inform'`
or set `INFORM_HOME` for another installation location.

## How examples are selected

An invisible HTML comment immediately before an Inform source fence supplies a
stable ID:

````markdown
<!-- inform-example: breezeway -->
```inform7
The Beautiful Breezeway is a room.
```
````

[examples.json](examples.json) maps each ID to a document, story title, command
sequence, and expected response fragments. The runner rejects missing or repeated
tags for a selected ID. Inserting or moving unrelated code blocks doesn't change
the selection.

The opening room example in Making Places also sets `"chapter_transcript": true`.
Its output lives between `<!-- inform-transcript: featureless-room -->` and
`<!-- /inform-transcript: featureless-room -->` comments. The runner replaces only
the content between those markers, keeping the surrounding prose and source.
Chapter output omits the compiler banner and uses a plain-text fence so prompts
and story text display literally. The full banner remains in `generated.md`.

To edit this example, change its Inform source in the chapter or its commands in
`examples.json`, run the generator, and review both the chapter and proof-page
diffs. Don't hand-edit the generated region: CI detects changes to it. The rest
of the chapters still have their original handwritten transcripts.

## Capture contract

Glulxe is linked to CheapGlk, which reads commands from standard input and writes
UTF-8 text to standard output. The runner uses no IDE protocol or GUI automation.
CheapGlk supports a single text buffer; status bars, graphics, and typography are
outside this prototype.

The compiled story receives a small harness rule that emits a unique marker before
each command read. The displayed code is the original documentation block with
trailing whitespace removed for presentation; the compiled source retains it. Markers
let the runner verify that every submitted command returned to an input boundary,
rather than guessing from a `>` in story text.

CheapGlk doesn't echo piped input, so the runner inserts the submitted commands
into the transcript. It removes only harness markers, prompts used for framing,
the console EOF trailer, and surrounding whitespace. Story responses come from the
interpreter. The compiler banner remains visible.

Commands must be nonempty single lines of at most 250 UTF-8 bytes. Examples must
use the standard Inform prompt and return to command input after their final
command. Game endings, file dialogs, and keyboard-only interaction aren't supported.
The runner fails on unexpected boundaries or trailers; it is not a general game
automation framework.

## Portability and reproducibility

The same build recipe supports native Windows, Linux, and macOS paths; the small
[Windows adapter](windows_compat.c) supplies missing POSIX temporary-file support.
The full pipeline has been verified on native Windows and in an isolated Linux
project environment: all three examples compile, play, and produce identical
generated Markdown. macOS execution has not yet been verified.

To use a Linux compiler distribution with a different directory layout, provide
explicit paths (all paths are resolved before the runner changes directories):

```sh
uv run --project . --group build python prototype/build_interpreter.py
uv run --project . python prototype/run.py \
  --inform7 /path/to/inform7 \
  --inform6 /path/to/inform6 \
  --internal /path/to/Internal \
  --check
```

`--interpreter` overrides the locally built console executable. It must be Glulxe
linked to CheapGlk and support `-q -u`; the IDE's bundled interpreter cannot be used.

A fixed compiler date and random seed make these examples reproducible. Compiler
versions are checked against the recipe. Interpreter sources and the build compiler
are pinned in the build recipe; a custom `--interpreter` is the caller's responsibility.
When changing versions, update the pins deliberately, rebuild, regenerate, and
review the resulting transcript changes.

For an optional Windows-to-Linux comparison using an existing WSL distribution:

```powershell
uv run --project . --group build python prototype/build_interpreter.py --linux-x86-64
uv run --project . python prototype/compare_linux.py --distro YOUR_EXISTING_DISTRO
```

This cross-compiles a static Linux console interpreter, then compares its output
with the native transcripts from the most recent successful generation. It does
not install or modify the WSL distribution.

## Linux CI

[The GitHub Actions workflow](../.github/workflows/executable-documentation.yml)
runs on pushes, pull requests, and manual dispatches using Ubuntu 24.04 and Python
3.13. It installs locked dependencies, extracts the checksum-pinned official Linux
Inform package, builds the console interpreter, runs the contract tests, and
compiles and plays every example with `--check`. It never updates the generated
page automatically. Compiler logs and transcripts are retained as diagnostic
artifacts for seven days, including when a later step fails.

The Linux setup script extracts only the two compilers and their resources into
`prototype/build/inform-linux`; it does not install the IDE or system packages.
To reproduce the CI commands on x86-64 Linux from the repository root:

```sh
uv sync --locked --python 3.13 --group build
uv run --locked --project . python prototype/setup_linux.py
uv run --locked --project . --group build python prototype/build_interpreter.py
uv run --locked --project . python -m unittest discover -s prototype -p test_runner.py
uv run --locked --project . python prototype/run.py \
  --inform7 prototype/build/inform-linux/usr/lib/x86_64-linux-gnu/inform7-ide/inform7 \
  --inform6 prototype/build/inform-linux/usr/lib/x86_64-linux-gnu/inform7-ide/inform6 \
  --internal prototype/build/inform-linux/usr/share/inform7-ide \
  --check
```

The opening Making Places example is the first chapter integration. Evaluate that
editing workflow before selecting additional transcript regions for conversion.
