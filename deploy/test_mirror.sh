#!/usr/bin/env bash
# Exercise the actual mirror commands against an isolated local destination.
set -euo pipefail
repo=$PWD
scratch=$(mktemp -d)
trap 'rm -rf -- "$scratch"' EXIT
mkdir -p "$scratch/remote/stale-directory" "$scratch/remote/assets"
printf 'obsolete\n' > "$scratch/remote/stale-directory/page.html"
printf 'obsolete\n' > "$scratch/remote/.stale-hidden-file"
# A changed file with the same size and timestamp must still be replaced.
cp dist/index.html "$scratch/remote/index.html"
printf 'X' | dd of="$scratch/remote/index.html" bs=1 count=1 conv=notrunc status=none
touch -r dist/index.html "$scratch/remote/index.html"
lftp --norc "file://$scratch/remote" -e "$(cat deploy/mirror.lftp)"
diff -r dist "$scratch/remote"
# Local preflight must fail before connecting if the artifact is missing or linked.
cd "$scratch"
export FTP_HOST=localhost FTP_USERNAME=test FTP_PASSWORD=test
if bash "$repo/deploy/ftp.sh" >preflight.log 2>&1; then
  printf 'An absent artifact was accepted.\n' >&2
  exit 1
fi
grep -q 'incomplete or empty' preflight.log
ln -s "$repo/dist" dist
if bash "$repo/deploy/ftp.sh" >preflight.log 2>&1; then
  printf 'A linked artifact was accepted.\n' >&2
  exit 1
fi
grep -q 'symbolic links' preflight.log
cd "$repo"
# Repeating a deployment must leave exactly the same tree.
lftp --norc "file://$scratch/remote" -e "$(cat deploy/mirror.lftp)"
diff -r dist "$scratch/remote"
