"""Compare a cross-compiled Linux console interpreter with native transcripts."""

import argparse
import json
import subprocess
import sys

from run import PROTOTYPE, format_transcript


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--distro", required=True, help="Name of an existing WSL distribution")
    args = parser.parse_args()
    wsl = ["wsl", "-d", args.distro, "--exec"]

    def linux_path(path):
        return subprocess.check_output(
            wsl + ["wslpath", "-a", path.resolve().as_posix()],
            text=True, timeout=15).strip()

    interpreter = linux_path(PROTOTYPE / "build/console-glulxe-linux")
    for example in json.loads((PROTOTYPE / "examples.json").read_text()):
        folder = PROTOTYPE / "build" / example["id"]
        result = subprocess.run(
            wsl + [interpreter, "-q", "-u", linux_path(folder / "story.ulx")],
            input=("\n".join(example["commands"]) + "\n").encode("utf-8"),
            capture_output=True, timeout=60)
        if result.returncode or result.stderr:
            raise RuntimeError(result.stderr.decode(errors="replace"))
        actual = format_transcript(result.stdout.decode("utf-8"), example["commands"])
        expected = (folder / "transcript.txt").read_text(encoding="utf-8")
        if actual != expected:
            raise RuntimeError(f'Linux transcript differs: {example["id"]}')
        print(f'PASS native/Linux output matches: {example["id"]}')


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, OSError, subprocess.SubprocessError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
