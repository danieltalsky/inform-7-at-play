"""Compile named documentation examples and capture play using console Glulxe."""

import argparse
import difflib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
PROTOTYPE = ROOT / "prototype"
MARKER = "__I7_AT_PLAY_INPUT_READY__"
HARNESS = ("\n\nBefore reading a command:\n"
           f'    say "[line break]{MARKER}[line break]".\n')
EXAMPLE_PATTERN = re.compile(
    r"<!-- inform-example: ([a-z0-9-]+) -->\s*\n```inform7[^\n]*\n(.*?)```", re.DOTALL)


def extract_source(document, example_id):
    matches = [source.strip() for name, source in EXAMPLE_PATTERN.findall(document)
               if name == example_id]
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one source block tagged {example_id!r}; found {len(matches)}")
    return matches[0]


def compiler_version(executable, option, pattern):
    result = subprocess.run([str(executable), option], capture_output=True, timeout=15)
    text = (result.stdout + result.stderr).decode("utf-8", errors="replace")
    match = re.search(pattern, text)
    if result.returncode or not match:
        raise RuntimeError(f"Cannot identify compiler {executable}:\n{text}")
    return match[1]


def verify_compilers(inform7, inform6):
    pins = json.loads((PROTOTYPE / "toolchain.json").read_text())
    for executable, option, pattern, expected in (
        (inform7, "-version", r"inform7 version ([\d.]+)", pins["inform_version"]),
        (inform6, "-h", r"Inform ([\d.]+)", pins["inform6_version"]),
    ):
        actual = compiler_version(executable, option, pattern)
        if actual != expected:
            raise RuntimeError(f"{executable}: expected {expected}, found {actual}; "
                               "compiler upgrades require an explicit toolchain.json update")


def compile_story(inform7, inform6, internal, work, source):
    work.mkdir(parents=True, exist_ok=True)
    (work / "external").mkdir(exist_ok=True)
    story = work / "story.ni"
    story.write_text(source + HARNESS, encoding="utf-8")
    intermediate = work / "auto.inf"
    output = work / "story.ulx"
    commands = [
        [inform7, "-source", story, "-internal", internal,
         "-external", work / "external", "-transient", work,
         "-format=Inform6/32", "-rng", "-fixtime", "-no-index", "-no-progress",
         "-o", intermediate],
        [inform6, "-G", "-w", intermediate, output],
    ]
    for index, command in enumerate(commands):
        result = subprocess.run([str(arg) for arg in command], cwd=work,
                                capture_output=True, timeout=90)
        log = (result.stdout + result.stderr).decode("utf-8", errors="replace")
        (work / f"compiler-{index + 1}.log").write_text(log, encoding="utf-8")
        if result.returncode:
            raise RuntimeError(f"Compilation failed in {work}:\n{log}")
    return output


def format_transcript(raw, commands):
    """Remove explicit harness boundaries and echo piped commands.

    CheapGlk does not echo stdin. A small Inform rule emits a boundary before
    each read, so story text containing ">" never determines command delivery.
    The final boundary and EOF trailer prove all commands reached another read.
    """
    raw = raw.replace("\r\n", "\n")
    chunks = raw.split("\n" + MARKER + "\n")
    if len(chunks) != len(commands) + 2:
        raise RuntimeError("Unexpected input boundaries: story ended early or requested extra input")
    if not re.fullmatch(r"\s*>\s*<end of input>\s*", chunks[-1]):
        raise RuntimeError("Unexpected console EOF trailer; unsupported interaction or interpreter version")
    transcript = chunks[0].strip()
    for command, chunk in zip(commands, chunks[1:-1]):
        chunk = chunk.lstrip("\n")
        if not chunk.startswith(">"):
            raise RuntimeError("Expected the standard Inform command prompt after a harness boundary")
        transcript += f"\n\n>{command}\n" + chunk[1:].strip()
    if "*** Run-time problem" in transcript or "Glulxe fatal error" in raw:
        raise RuntimeError("Interpreter reported a runtime error")
    return transcript.rstrip() + "\n"


def play(interpreter, story, commands):
    if any(not command or "\n" in command or "\r" in command
           or len(command.encode("utf-8")) > 250 for command in commands):
        raise ValueError("Commands must be nonempty single lines of at most 250 UTF-8 bytes")
    result = subprocess.run(
        [str(interpreter), "-q", "-u", str(story)],
        input=("\n".join(commands) + "\n").encode("utf-8"),
        cwd=story.parent, capture_output=True, timeout=60,
    )
    raw = result.stdout.decode("utf-8")
    (story.parent / "console-output.txt").write_bytes(result.stdout)
    stderr = result.stderr.decode("utf-8", errors="replace")
    if result.returncode or stderr:
        raise RuntimeError(f"Console interpreter failed ({result.returncode}):\n{stderr}\n{raw}")
    return format_transcript(raw, commands)


def update_chapter_transcript(document, example_id, transcript):
    """Replace one explicitly delimited chapter region, preserving its surroundings."""
    start = f"<!-- inform-transcript: {example_id} -->"
    end = f"<!-- /inform-transcript: {example_id} -->"
    if document.count(start) != 1 or document.count(end) != 1:
        raise ValueError(f"Expected exactly one pair of transcript markers for {example_id}")
    before, _, remaining = document.partition(start)
    _, separator, after = remaining.partition(end)
    if not separator or end in before:
        raise ValueError(f"Transcript markers are out of order for {example_id}")
    # Keep the teaching example focused on play; the full banner remains in generated.md.
    banner = (r"\A[^\n]+\nAn Interactive Fiction\n"
              r"Release [^\n]+ / Inform 7 v[^\n]+\n\n")
    gameplay, count = re.subn(banner, "", transcript, count=1)
    if count != 1:
        raise ValueError(f"Unrecognized story banner for {example_id}; refusing to trim it")
    region = f"\n\n```text\n{gameplay.rstrip()}\n```\n\n"
    return before + start + region + end + after


def write_or_check(target, rendered, check):
    previous = target.read_text(encoding="utf-8") if target.exists() else ""
    if check:
        if previous == rendered:
            return True
        name = target.relative_to(ROOT).as_posix()
        print("".join(difflib.unified_diff(previous.splitlines(True), rendered.splitlines(True),
                                          fromfile=f"checked-in/{name}", tofile=f"generated/{name}")))
        return False
    if previous != rendered:
        target.write_text(rendered, encoding="utf-8", newline="\n")
        print(f"Wrote {target}")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inform", type=Path,
                        default=Path(os.environ.get("INFORM_HOME", "C:/Program Files/Inform")))
    parser.add_argument("--inform7", type=Path, help="Override the Inform 7 compiler path")
    parser.add_argument("--inform6", type=Path, help="Override the Inform 6 compiler path")
    parser.add_argument("--internal", type=Path, help="Override Inform resources")
    parser.add_argument("--interpreter", type=Path,
                        default=PROTOTYPE / "build" / ("console-glulxe.exe" if os.name == "nt" else "console-glulxe"))
    parser.add_argument("--check", action="store_true",
                        help="Fail if regenerated Markdown differs from the checked-in page")
    args = parser.parse_args()
    install = args.inform.resolve()
    suffix = ".exe" if os.name == "nt" else ""
    inform7 = (args.inform7 or install / f"Compilers/inform7{suffix}").resolve()
    inform6 = (args.inform6 or install / f"Compilers/inform6{suffix}").resolve()
    internal = (args.internal or install / "Internal").resolve()
    interpreter = args.interpreter.resolve()
    for executable in (inform7, inform6, interpreter):
        if not executable.is_file():
            raise RuntimeError(f"Missing {executable}; see prototype/README.md for setup and path overrides")
    if not internal.is_dir():
        raise RuntimeError(f"Missing Inform resources: {internal}")
    verify_compilers(inform7, inform6)
    examples = json.loads((PROTOTYPE / "examples.json").read_text(encoding="utf-8"))
    ids = [example["id"] for example in examples]
    if len(ids) != len(set(ids)) or any(not re.fullmatch(r"[a-z0-9-]+", name) for name in ids):
        raise ValueError("Example IDs must be unique lowercase letters, digits, and hyphens")
    sections = ["# Executable documentation: proof of concept\n\n"
                "Generated by `uv run --project . python prototype/run.py`. "
                "Named source blocks come directly from the existing documentation; "
                "responses come from compiled stories running in console Glulxe with CheapGlk. "
                "The runner echoes submitted commands and removes its input-boundary markers. "
                "Compiler versions, random seed, and build date are fixed.\n"]
    chapters = {}
    for example in examples:
        path = ROOT / example["document"]
        document = chapters.get(path)
        if document is None:
            document = path.read_text(encoding="utf-8")
        source = extract_source(document, example["id"])
        display_source = "\n".join(line.rstrip() for line in source.splitlines())
        work = PROTOTYPE / "build" / example["id"]
        story = compile_story(inform7, inform6, internal, work, f'"{example["title"]}"\n\n{source}\n')
        transcript = play(interpreter, story, example["commands"])
        (work / "transcript.txt").write_text(transcript, encoding="utf-8")
        for expected in example["expect"]:
            if expected not in transcript:
                raise RuntimeError(f'{example["id"]}: missing expected output {expected!r}')
        if example.get("chapter_transcript", False):
            chapters[path] = update_chapter_transcript(document, example["id"], transcript)
        sections.append(f'\n## {example["title"]}\n\n'
                        f'Source: [{example["document"]}](../{example["document"]})\n\n'
                        f'```inform7\n{display_source}\n```\n\n'
                        f'```text\n{transcript}```\n')
        print(f'PASS {example["id"]}: compiled and played {len(example["commands"])} commands')
    rendered = "".join(sections)
    outputs = {PROTOTYPE / "generated.md": rendered, **chapters}
    # Finish every compile and render before writing any documentation.
    matches = [write_or_check(target, content, args.check) for target, content in outputs.items()]
    if args.check:
        if not all(matches):
            raise RuntimeError("Generated documentation differs; run without --check to update")
        print("Generated documentation is up to date")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, subprocess.TimeoutExpired, OSError, ValueError, IndexError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
