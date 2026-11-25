# Submitting a theme

1. **Fork** this repo and copy `tools/template` to `packs/<your-theme-id>/` (id: 2-32 characters of `a-z 0-9 _ -`,
   the folder name must equal `"id"` in theme.json).
2. **Edit `theme.json`:**

   | Field | What |
   |---|---|
   | `id` | same as the folder name |
   | `name` | shown in the store (max 32 characters) |
   | `author` | your name, shown as the theme's author |
   | `github` | your GitHub username (shown as `@you`) |
   | `version` | dotted numbers, e.g. `1.0`. Raise it for every update so cars offer the update |
   | `description` | one line, max 80 characters |
   | `brands` | `["hyundai"]`, `["kia"]` or both |
   | `light` | `true` for a light theme (dark text) |
   | `colors` | `background` (4 gradient colours), `glow1`, `glow2`, `shade`, `card`, `subtext`, `accent` as `#rrggbb` or `#aarrggbb` |
   | `wallpaper` | `wallpaper.jpg`: **1920 x 720 JPEG**, max 2 MB |
   | `icons` | folder of **90 x 90 PNG** icons, names from `tools/icon-names.txt`; leave any out to keep ccNC's |
   | `boot_video`, `shutdown_video` | optional `.mp4` (H.264 baseline, 1920 x 720, max 30 MB) or `null` |

   Optional: `preview.png` (1920 x 720 or 960 x 360) for the store; otherwise the wallpaper is used.
3. **Check it:** `python3 -I tools/validate.py packs/<id>` must print `OK`. `tools/mktheme.sh packs/<id>` builds
   the zip so you can try it on your car from a USB stick.
4. **Open a pull request.** The automatic check runs the same validation on every pack.

## Rules

- **Original work only.** Your own artwork, or art you have the right to share. No copyrighted characters,
  movie / game / brand logos or imagery you didn't make.
- Keep text readable: cards sit over the wallpaper, so keep the lower half calm or raise `card` / `shade` opacity.
- One theme per pull request. Updates: raise `version`.
- Packs contain files only (no scripts). Pull requests that change `tools/` or `.github/` are reviewed separately.

Accepted themes go out in the next store release.
