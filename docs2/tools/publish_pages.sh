#!/usr/bin/env bash
# Publish a folder to the gh-pages branch, safe when several workflow runs push at once.
# Usage: publish_pages.sh <source_dir> <destination_dir> "<commit message>"
# Existing files on gh-pages are kept. When the push is rejected because another run
# pushed first, it fetches the new tip, redoes the copy on top of it and tries again.
set -euo pipefail
src="$1"; dest="$2"; msg="$3"
repo="https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"
work="$(mktemp -d)"
src="$(cd "$src" && pwd)"
trap 'rm -rf "$work"' EXIT

git init -q "$work"
cd "$work"
git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git remote add origin "$repo"

for attempt in 1 2 3 4 5 6 7 8; do
  if git fetch -q --depth=1 origin gh-pages 2>/dev/null; then
    git checkout -q -B gh-pages FETCH_HEAD
  else
    git checkout -q --orphan gh-pages   # first ever publish
  fi
  mkdir -p "$dest"
  cp -a "$src"/. "$dest"/
  touch .nojekyll
  git add -A
  if git diff --cached --quiet; then echo "Nothing new to publish to $dest"; exit 0; fi
  git commit -q -m "$msg"
  if git push -q origin gh-pages; then echo "Published to gh-pages/$dest (attempt $attempt)"; exit 0; fi
  echo "Push rejected (attempt $attempt), another run pushed first. Retrying..."
  sleep $(( (RANDOM % 6) + attempt * 2 ))
done
echo "::error::Could not push to gh-pages after several tries"
exit 1
