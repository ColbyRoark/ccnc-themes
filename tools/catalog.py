"""Writes the theme catalog into README.md (between the catalog markers) from packs/*/theme.json.

    python3 -I tools/catalog.py
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
START, END = '<!-- catalog:start -->', '<!-- catalog:end -->'


def main():
    packs = []
    for d in sorted(os.listdir(os.path.join(ROOT, 'packs'))):
        j = os.path.join(ROOT, 'packs', d, 'theme.json')
        if os.path.isfile(j):
            packs.append((d, json.load(open(j, encoding='utf-8'))))
    rows = ['| Preview | Theme |', '|---|---|']
    for d, t in packs:
        img = 'preview.png' if os.path.isfile(os.path.join(ROOT, 'packs', d, 'preview.png')) else t.get('wallpaper') or 'wallpaper.jpg'
        who = t.get('author', '')
        if t.get('github'):
            who = '[%s](https://github.com/%s)' % (who or '@' + t['github'], t['github'])
        brands = ' + '.join(b.capitalize() for b in t.get('brands', [])) or 'Hyundai + Kia'
        extras = []
        if t.get('boot_video'):
            extras.append('startup video')
        if t.get('icons'):
            extras.append('icons')
        info = '**%s** `%s`<br>%s<br>by %s<br>%s · %s · v%s%s' % (
            t['name'], d, t.get('description', ''), who, 'Light' if t.get('light') else 'Dark', brands, t.get('version', '1.0'),
            ('<br>Includes: ' + ', '.join(extras)) if extras else '')
        rows.append('| <a href="packs/%s"><img src="packs/%s/%s" width="420"></a> | %s |' % (d, d, img, info))
    table = '\n'.join(rows)
    p = os.path.join(ROOT, 'README.md')
    s = open(p, encoding='utf-8').read()
    block = '%s\n%d themes.\n\n%s\n%s' % (START, len(packs), table, END)
    s = re.sub(re.escape(START) + '.*?' + re.escape(END), block, s, flags=re.S) if START in s else s + '\n' + block + '\n'
    open(p, 'w', encoding='utf-8').write(s)
    print('catalog: %d themes' % len(packs))


if __name__ == '__main__':
    main()
