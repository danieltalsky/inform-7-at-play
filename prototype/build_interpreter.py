"""Build pinned Glulxe + CheapGlk locally with the optional Zig toolchain."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tarfile
import urllib.request

PROTOTYPE = Path(__file__).resolve().parent
BUILD = PROTOTYPE / "build"
EXECUTABLE = BUILD / ("console-glulxe.exe" if os.name == "nt" else "console-glulxe")


def fetch_source(name, pin):
    archive = BUILD / f"{name}.tar.gz"
    if not archive.exists():
        url = f'https://codeload.github.com/erkyrath/{name}/tar.gz/{pin["commit"]}'
        print(f"Downloading {name} at {pin['commit']}", flush=True)
        with urllib.request.urlopen(url, timeout=60) as response:
            archive.write_bytes(response.read())
    if hashlib.sha256(archive.read_bytes()).hexdigest() != pin["sha256"]:
        raise RuntimeError(f"Checksum mismatch: {archive}; remove it and retry")
    # Extract only regular files and directories below the expected archive root.
    directory = BUILD / f'{name}-{pin["commit"]}'
    with tarfile.open(archive) as bundle:
        for member in bundle.getmembers():
            target = (BUILD / member.name).resolve()
            if not target.is_relative_to(directory.resolve()):
                raise RuntimeError(f"Unexpected archive path: {member.name}")
            if member.isdir():
                target.mkdir(parents=True, exist_ok=True)
            elif member.isfile():
                target.parent.mkdir(parents=True, exist_ok=True)
                with bundle.extractfile(member) as source:
                    target.write_bytes(source.read())
            else:
                raise RuntimeError(f"Unexpected archive entry: {member.name}")
    return directory


def main():
    import ziglang

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--linux-x86-64", action="store_true",
                        help="Cross-compile a Linux executable for portability checks")
    args = parser.parse_args()
    output = BUILD / "console-glulxe-linux" if args.linux_x86_64 else EXECUTABLE
    BUILD.mkdir(exist_ok=True)
    pins = json.loads((PROTOTYPE / "toolchain.json").read_text())
    sources = {name: fetch_source(name, pin) for name, pin in pins["sources"].items()}
    glulxe = sources["glulxe"]
    cheapglk = sources["cheapglk"]
    vm_files = ("main files vm exec funcs operand string glkop heap serial search accel "
                "float gestalt osdepend profile debugger unixstrt unixautosave").split()
    glk_files = ("cgfref cggestal cgmisc cgstream cgstyle cgwindow cgschan cgdate cgunicod "
                 "main gi_dispa gi_blorb gi_debug cgblorb").split()
    zig = Path(ziglang.__file__).parent / ("zig.exe" if os.name == "nt" else "zig")
    command = [str(zig), "cc", "-O2", "-DOS_STDC", "-I", str(cheapglk),
               "-o", str(output)]
    if args.linux_x86_64:
        command += ["-target", "x86_64-linux-musl"]
    elif os.name == "nt":
        command += ["-include", str(PROTOTYPE / "windows_compat.h"),
                    str(PROTOTYPE / "windows_compat.c")]
    command += [str(glulxe / f"{name}.c") for name in vm_files]
    command += [str(cheapglk / f"{name}.c") for name in glk_files]
    command += ["-lm"]
    print("Building console Glulxe (first build can take a few minutes)", flush=True)
    result = subprocess.run(command, capture_output=True, timeout=300)
    log = (result.stdout + result.stderr).decode("utf-8", errors="replace")
    (BUILD / "interpreter-build.log").write_text(log, encoding="utf-8")
    if result.returncode:
        raise RuntimeError(log)
    print(f"Built {output}")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, OSError, subprocess.TimeoutExpired, ImportError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
