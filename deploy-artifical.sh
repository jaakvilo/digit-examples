#!/bin/sh

# Deploy this static examples site to https://artifical.eu/digit/.
#
# Examples:
#   ./deploy-artifical.sh
#   ./deploy-artifical.sh --dry-run
#   ./deploy-artifical.sh artifical:domeenid/www.artifical.eu/htdocs/test-digit/

set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
TARGET=${DEPLOY_TARGET:-artifical:domeenid/www.artifical.eu/htdocs/digit/}
DRY_RUN=0

usage() {
  cat <<'EOF'
Usage: ./deploy-artifical.sh [--dry-run] [target]

Syncs this repository as a static website to:
  artifical:domeenid/www.artifical.eu/htdocs/digit/

Options:
  --dry-run   Show what would be uploaded without changing the server.
  target      Optional rsync target, overriding the default.

Environment:
  DEPLOY_TARGET  Optional default rsync target.
EOF
}

while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run)
      DRY_RUN=1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    -*)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 1
      ;;
    *)
      TARGET=$1
      ;;
  esac
  shift
done

if [ ! -f "$ROOT_DIR/index.html" ]; then
  echo "index.html not found in $ROOT_DIR" >&2
  exit 1
fi

set -- rsync -av --delete \
  --exclude .git/ \
  --exclude .DS_Store \
  --exclude deploy-artifical.sh \
  --exclude README.md \
  "$ROOT_DIR/" "$TARGET"

if [ "$DRY_RUN" -eq 1 ]; then
  set -- "$@" --dry-run
fi

printf 'Deploying %s to %s\n' "$ROOT_DIR/" "$TARGET"
exec "$@"
