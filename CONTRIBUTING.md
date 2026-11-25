# Contributing a theme

[← Back to README](README.md)

Thanks for making a theme! Accepted themes appear in every car's Theme Store, credited to you.

## Steps

1. **Fork** this repository.
2. **Copy the template:** `cp -R tools/template packs/<your-theme-id>`
3. **Edit `theme.json`:** name, your `author` name and `github` username, colours and description.
   Every field is explained in [Theme format](docs/THEME-FORMAT.md).
4. **Add artwork:** a 1920 x 720 `wallpaper.jpg`, and optionally icons, a `preview.png` and a startup video.
5. **Validate:** `python3 -I tools/validate.py packs/<your-theme-id>` must print `OK`.
6. **Try it (optional):** `tools/mktheme.sh packs/<your-theme-id>` builds a zip you can install from a USB stick.
7. **Open a pull request.** An automatic check validates every pack.

Accepted themes go out in the next store release.

## Rules

- **Original work only.** Your own artwork, or art you have the right to share. No copyrighted characters,
  movie, game or brand logos, or imagery you didn't make.
- **Readable text.** Cards sit over the wallpaper: keep the lower half calm, or raise `card` / `shade` opacity.
- **One theme per pull request.** For updates, raise `version`.
- **Files only.** Packs never contain scripts. Pull requests that change `tools/` or `.github/` are reviewed
  separately.
- **License.** By submitting, you license your theme under [CC BY 4.0](packs/LICENSE.md).
