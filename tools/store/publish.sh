#!/bin/bash
# Maintainer only: publishes the ccNC Theme Store from this repo's packs/ as a new GitHub release (marked latest).
# ccNC Home reads https://github.com/JacobPantuso/ccnc-themes/releases/latest/download/themes.json
#   tools/store/publish.sh <tag>        e.g. tools/store/publish.sh 2026.11.24
# Needs gh (logged in) and the store signing key ($CCNC_STORE_KEY, default ~/Documents/GEN5W/keys/ccnc-themes-store.pem).
set -euo pipefail
cd "$(dirname "$0")/../.."
TAG=${1:?usage: tools/store/publish.sh <tag>}
git pull --ff-only
for p in packs/*/; do [ -f "$p/theme.json" ] && tools/mktheme.sh "$p" >/dev/null; done
python3 -I tools/catalog.py
if ! git diff --quiet README.md docs/CATALOG.md || [ -n "$(git status --porcelain docs/CATALOG.md)" ]; then  # new / changed themes: keep the README catalog current
    git add README.md docs/CATALOG.md && git commit -q -m "Update theme catalog" && git push -q
fi
python3 -I tools/store/mkstore.py
gh release create "$TAG" store-out/* --repo JacobPantuso/ccnc-themes --title "ccNC themes $TAG" \
    --notes "ccNC Theme Store: $(python3 -I -c "import json;print(len(json.load(open('store-out/themes.json'))['themes']))") themes." --latest
echo "published: https://github.com/JacobPantuso/ccnc-themes/releases/latest/download/themes.json"
