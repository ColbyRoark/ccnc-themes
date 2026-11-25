# ccNC Themes

Theme packs for **ccNC**, the ccNC-style interface for Hyundai / Kia Gen5W head units. A theme changes the
wallpaper, colours and icons of every ccNC app (Home, Settings, Climate, Media, EV and the rest), and can carry
boot / shutdown videos.

## Installing themes on the car

- **Over Wi-Fi:** Settings > Screen Theme > **Theme Store** in ccNC lists every theme published here, with
  previews. Tap a theme, then Install. When the head unit joins Wi-Fi, ccNC tells you about new themes and
  updates; nothing installs by itself.
- **From a USB stick:** each release also has `*-nemesis.zip` files for NEMESIS: unzip onto a stick and
  install from NEMESIS Manager.

Then pick the theme in Settings > Screen Theme > ccNC Theme.

## Making your own

See [CONTRIBUTING.md](CONTRIBUTING.md): copy `tools/template`, edit `theme.json`, add your wallpaper and icons,
check it with `tools/validate.py`, and open a pull request. Your name (and GitHub username) is shown as the
theme's author in the Theme Store.

## How the store works

Every release holds `themes.json` (the list of themes), its signature `themes.json.sig`, a preview and a zip per
theme. ccNC only uses a list signed with the store key, checks every download against it, and only unpacks a
theme's own files (theme.json, wallpaper, icons, videos).
