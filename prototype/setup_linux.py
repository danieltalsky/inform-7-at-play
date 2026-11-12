"""Extract pinned Linux compilers and resources without installing the Inform IDE."""

import hashlib
import io
import json
from pathlib import Path
import sys
import tarfile
import urllib.request

PROTOTYPE = Path(__file__).resolve().parent
BUILD = PROTOTYPE / "build"


def debian_payload(data):
    """Read the data tar member of a Debian package's ar container."""
    if not data.startswith(b"!<arch>\n"):
        raise ValueError("Not a Debian ar archive")
    offset = 8
    while offset + 60 <= len(data):
        header = data[offset:offset + 60]
        if header[58:] != b"`\n":
            raise ValueError("Invalid ar member header")
        name = header[:16].decode("ascii").strip().rstrip("/")
        length = int(header[48:58])
        start = offset + 60
        if length < 0 or start + length > len(data):
            raise ValueError("Truncated ar member")
        if name.startswith("data.tar."):
            return data[start:start + length]
        offset = start + length + length % 2
    raise ValueError("Debian package has no data tar archive")


def main():
    if not sys.platform.startswith("linux"):
        raise RuntimeError("This setup command targets Linux; use the installed Inform tools on Windows")
    BUILD.mkdir(exist_ok=True)
    pin = json.loads((PROTOTYPE / "toolchain.json").read_text())["linux_package"]
    package = BUILD / "inform-linux.deb"
    if not package.exists():
        print("Downloading pinned Linux Inform package", flush=True)
        with urllib.request.urlopen(pin["url"], timeout=60) as response:
            package.write_bytes(response.read())
    data = package.read_bytes()
    if hashlib.sha256(data).hexdigest() != pin["sha256"]:
        raise RuntimeError(f"Checksum mismatch: {package}; remove it and retry")
    destination = (BUILD / "inform-linux").resolve()
    compilers = {"usr/lib/x86_64-linux-gnu/inform7-ide/inform7",
                 "usr/lib/x86_64-linux-gnu/inform7-ide/inform6"}
    with tarfile.open(fileobj=io.BytesIO(debian_payload(data))) as bundle:
        for member in bundle.getmembers():
            name = member.name.removeprefix("./")
            if name not in compilers and not name.startswith("usr/share/inform7-ide/"):
                continue
            target = (destination / name).resolve()
            if not target.is_relative_to(destination):
                raise RuntimeError(f"Unexpected archive path: {name}")
            if member.isdir():
                target.mkdir(parents=True, exist_ok=True)
            elif member.isfile():
                target.parent.mkdir(parents=True, exist_ok=True)
                with bundle.extractfile(member) as source:
                    target.write_bytes(source.read())
                target.chmod(member.mode & 0o777)
            else:
                raise RuntimeError(f"Unsupported archive entry: {name}")
    for name in compilers:
        if not (destination / name).is_file():
            raise RuntimeError(f"Package is missing {name}")
    print(f"Extracted Linux Inform tools to {destination}")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, OSError, ValueError, tarfile.TarError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
