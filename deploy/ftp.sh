#!/usr/bin/env bash
# Run from the repository root. The FTP login directory is the entire site.
set -euo pipefail

: "${FTP_HOST:?Missing FTP_HOST}"
: "${FTP_USERNAME:?Missing FTP_USERNAME}"
: "${FTP_PASSWORD:?Missing FTP_PASSWORD}"
if [[ ! "$FTP_HOST" =~ ^[a-zA-Z0-9][a-zA-Z0-9.-]*$ ]]; then
  printf 'FTP_HOST must be a hostname or IPv4 address, without a URL or path.\n' >&2
  exit 1
fi
port=${FTP_PORT:-21}
if [[ ! "$port" =~ ^[0-9]{1,5}$ ]] || (( 10#$port < 1 || 10#$port > 65535 )); then
  printf 'FTP_PORT must be between 1 and 65535.\n' >&2
  exit 1
fi
if [[ ! -s dist/index.html || ! -s dist/assets/style.css ]]; then
  printf 'Refusing to deploy an incomplete or empty dist directory.\n' >&2
  exit 1
fi
if [[ -L dist || -n "$(find dist -type l -print -quit)" ]]; then
  printf 'Refusing to deploy symbolic links.\n' >&2
  exit 1
fi

command -v lftp >/dev/null
export LFTP_PASSWORD="$FTP_PASSWORD"
unset FTP_PASSWORD

# Credentials are passed as data, never interpolated into lftp commands.
lftp --norc --env-password --user "$FTP_USERNAME" --port "$port" \
  "ftp://$FTP_HOST" -e "$(cat deploy/mirror.lftp)"
