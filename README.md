# ccNC Themes

Themes for [**ccNC for Gen5W**](https://github.com/JacobPantuso/ccnc-gen5w), the ccNC-style interface for
Hyundai and Kia Gen5W head units. A theme restyles every ccNC app at once: wallpaper, colours, icons, and
optionally the startup and shutdown videos.

![Themes on ccNC Home](docs/themes.png)

## Install a theme

- **Over Wi-Fi (easiest):** in ccNC, open **Settings > Screen Theme > Theme Store**, tap a theme and
  **Install**. When the car joins Wi-Fi, ccNC tells you about new themes and updates. Nothing installs by itself.
- **From a USB stick:** download the theme's `ccnc.theme.<id>-<version>-nemesis.zip` from the
  [latest release](https://github.com/JacobPantuso/ccnc-themes/releases/latest), unzip it onto the root of a
  stick, and install it from NEMESIS Manager.

Then choose it in **Settings > Screen Theme > ccNC Theme**.

## Catalog

<!-- catalog:start -->
13 themes.

| Preview | Theme |
|---|---|
| <a href="packs/arctic-light"><img src="packs/arctic-light/preview.png" width="420"></a> | **Arctic Light** `arctic-light`<br>Light theme: frosted ice blues with crisp dark text.<br>by ccNC<br>Light · Hyundai + Kia · v1.0<br>Includes: startup video, icons |
| <a href="packs/aurora"><img src="packs/aurora/preview.png" width="420"></a> | **Aurora** `aurora`<br>Northern lights over a dark ridge, mint to violet.<br>by ccNC<br>Dark · Hyundai + Kia · v1.0<br>Includes: startup video, icons |
| <a href="packs/candy-cane-christmas"><img src="packs/candy-cane-christmas/preview.png" width="420"></a> | **Candy Cane Christmas** `candy-cane-christmas`<br>Snowy night, twinkling tree lights and candy-cane icons. Look up!<br>by ccNC<br>Dark · Hyundai + Kia · v1.0<br>Includes: startup video, icons |
| <a href="packs/carbon-orange"><img src="packs/carbon-orange/preview.png" width="420"></a> | **Carbon Orange** `carbon-orange`<br>Carbon-fibre graphite with a hot orange light trail.<br>by ccNC<br>Dark · Hyundai + Kia · v1.0<br>Includes: startup video, icons |
| <a href="packs/deep-ocean"><img src="packs/deep-ocean/preview.png" width="420"></a> | **Deep Ocean** `deep-ocean`<br>Abyssal blues, drifting light rays and teal glow.<br>by ccNC<br>Dark · Hyundai + Kia · v1.0<br>Includes: startup video, icons |
| <a href="packs/evergreen"><img src="packs/evergreen/preview.png" width="420"></a> | **Evergreen** `evergreen`<br>Pine-green topographic contours, calm and organic.<br>by ccNC<br>Dark · Hyundai + Kia · v1.0<br>Includes: startup video, icons |
| <a href="packs/hyundai-parametric"><img src="packs/hyundai-parametric/preview.png" width="420"></a> | **Parametric Blue** `hyundai-parametric`<br>Hyundai: parametric pixel grid in deep blue and cyan.<br>by ccNC<br>Dark · Hyundai · v1.0<br>Includes: startup video, icons |
| <a href="packs/kia-midnight"><img src="packs/kia-midnight/preview.png" width="420"></a> | **Midnight Facets** `kia-midnight`<br>Kia: sharp angular facets in black with coral light.<br>by ccNC<br>Dark · Kia · v1.0<br>Includes: startup video, icons |
| <a href="packs/neon-drive"><img src="packs/neon-drive/preview.png" width="420"></a> | **Neon Drive** `neon-drive`<br>Retro synthwave dusk: striped sun, magenta grid.<br>by ccNC<br>Dark · Hyundai + Kia · v1.0<br>Includes: startup video, icons |
| <a href="packs/rose-gold"><img src="packs/rose-gold/preview.png" width="420"></a> | **Rose Gold** `rose-gold`<br>Silky rose-gold ribbons on deep plum.<br>by ccNC<br>Dark · Hyundai + Kia · v1.0<br>Includes: startup video, icons |
| <a href="packs/sandstone"><img src="packs/sandstone/preview.png" width="420"></a> | **Sandstone** `sandstone`<br>Light theme: warm desert dunes, terracotta accent.<br>by ccNC<br>Light · Hyundai + Kia · v1.0<br>Includes: startup video, icons |
| <a href="packs/swamp-master"><img src="packs/swamp-master/preview.png" width="420"></a> | **Swamp Master** `swamp-master`<br>Misty jungle swamp, ancient roots and a glowing green accent.<br>by ccNC<br>Dark · Hyundai + Kia · v1.0<br>Includes: startup video, icons |
| <a href="packs/swamp-ogre"><img src="packs/swamp-ogre/preview.png" width="420"></a> | **Swamp Ogre** `swamp-ogre`<br>Murky swamp at dusk: moss greens, mud browns, firefly glow.<br>by ccNC<br>Dark · Hyundai + Kia · v1.0<br>Includes: startup video, icons |
<!-- catalog:end -->

## Make your own

Anyone can make a theme and send it in: see [CONTRIBUTING.md](CONTRIBUTING.md). Short version: copy
`tools/template` to `packs/<your-id>/`, edit `theme.json` (put your name in `author` and your GitHub username
in `github`, that's how you're credited in the store), add a 1920 x 720 wallpaper and any icons, check it with
`python3 -I tools/validate.py packs/<your-id>`, and open a pull request. An automatic check validates every
pull request.

## How the store works

Each release holds the theme list (`themes.json`), its signature, a preview and a zip for every theme. ccNC
only uses a list signed with the store's key, checks every download against it, and only unpacks a theme's own
files (theme.json, wallpaper, icons, videos), so nothing else can reach the car through a theme.

## Licence

Tools: MIT ([LICENSE](LICENSE)). Themes: CC BY 4.0, credit the theme's author; see
[packs/LICENSE.md](packs/LICENSE.md) (the starter packs' icons are recoloured ccNC artwork and not covered).
