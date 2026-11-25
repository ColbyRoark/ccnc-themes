# Theme format

[← Back to README](../README.md)

A theme is a folder in `packs/<id>/`. It holds files only, never scripts.

```
packs/my-theme/
├── theme.json       required
├── wallpaper.jpg    1920 x 720 JPEG, max 2 MB
├── preview.png      optional store preview (1920 x 720 or 960 x 360)
├── icons/           optional 90 x 90 PNGs
└── boot.mp4         optional startup video
```

## theme.json

```json
{
  "id": "my-theme",
  "name": "My Theme",
  "author": "Your Name",
  "github": "your-github-username",
  "version": "1.0",
  "description": "One line about your theme.",
  "brands": ["hyundai", "kia"],
  "light": false,
  "colors": {
    "background": ["#05070A", "#0B1118", "#101922", "#06090C"],
    "glow1": "#00000000",
    "glow2": "#00000000",
    "shade": "#99000000",
    "card": "#5C2A343D",
    "subtext": "#B4BEC6",
    "accent": "#4FB3E8"
  },
  "wallpaper": "wallpaper.jpg",
  "icons": "icons",
  "boot_video": null,
  "shutdown_video": null
}
```

## Fields

| Field | Required | Rules |
|---|---|---|
| `id` | yes | 2–32 characters of `a-z 0-9 _ -`; same as the folder name |
| `name` | yes | Max 32 characters |
| `author` | yes | Max 32 characters; shown as the theme's author |
| `github` | no | Your GitHub username; shown as `@you` in the store |
| `version` | yes | Dotted numbers, e.g. `1.0`. Raise it for every update |
| `description` | yes | One line, max 80 characters |
| `brands` | yes | `["hyundai"]`, `["kia"]` or both |
| `light` | yes | `true` for a light theme (dark text) |
| `colors.background` | yes | 4 colours of the diagonal background gradient |
| `colors.glow1`, `glow2` | yes | Soft glows over the gradient (`#00000000` for none) |
| `colors.shade` | yes | Darkening at the bottom of the screen, over the wallpaper |
| `colors.card` | yes | Card fill; keep it translucent |
| `colors.subtext` | yes | Secondary text |
| `colors.accent` | yes | Selections, progress and toggles (owners can override it) |
| `wallpaper` | no | 1920 x 720 JPEG, max 2 MB |
| `icons` | no | Folder of 90 x 90 PNGs named from [`tools/icon-names.txt`](../tools/icon-names.txt); leave any out to keep ccNC's |
| `boot_video`, `shutdown_video` | no | `.mp4`, H.264 baseline, 1920 x 720, max 30 MB, or `null` |

Colours are `#rrggbb` or `#aarrggbb` (alpha first).

## Design tips

- Cards sit over the lower part of the wallpaper: keep that area calm, or raise `card` and `shade` opacity.
- Check text contrast on both the welcome page and the app pages.
- Light themes need `"light": true` so text turns dark.

## Tools

| Command | What |
|---|---|
| `python3 -I tools/validate.py packs/<id>` | Checks every rule above; must print `OK` |
| `tools/mktheme.sh packs/<id>` | Builds the NEMESIS zips (store and USB) into `dist/` |
| `python3 -I tools/catalog.py` | Regenerates the README gallery and `docs/CATALOG.md` |
