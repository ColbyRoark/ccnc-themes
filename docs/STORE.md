# How the store works

[← Back to README](../README.md)

## For owners

Each [release](https://github.com/JacobPantuso/ccnc-themes/releases/latest) of this repository is the store.
It holds:

| File | What |
|---|---|
| `themes.json` | The list of themes, versions, sizes and SHA-256 hashes |
| `themes.json.sig` | The list's RSA-SHA256 signature |
| `preview-<id>.png` | Store previews |
| `ccnc.theme.<id>-<version>.zip` | Each theme, as a NEMESIS package |

ccNC Home:

1. Downloads `themes.json` and only uses it if the signature matches the store key built into ccNC.
2. Checks every theme download against the size and SHA-256 in the signed list.
3. Unpacks only a theme's own files (`theme.json`, wallpaper, icons, videos). Nothing else from a theme can
   reach the car.
4. Checks for new themes and updates when the head unit joins Wi-Fi (at most every 6 hours) and only shows a
   notification. Nothing installs without a tap.

## For maintainers

```sh
tools/store/publish.sh <tag>     # e.g. tools/store/publish.sh 2026.11.24
```

Builds every pack, regenerates the catalog, signs the index with the key in `$CCNC_STORE_KEY` and publishes the
release. The signing key never goes in this repository.
