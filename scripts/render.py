"""Renderiza uma pagina quadro a quadro em 1920x1080, 30 fps.
Quadros:  render.py anim.html pasta inicio fim
Teste:    render.py anim.html pasta --times 1.5,5,9.92
Pula quadros que ja existem, entao da para retomar."""
import os, pathlib, sys
from playwright.sync_api import sync_playwright

args = sys.argv[1:]
times = None
if '--times' in args:
    i = args.index('--times')
    times = [float(x) for x in args[i + 1].split(',')]
    del args[i:i + 2]
page, out = pathlib.Path(args[0]).resolve(), pathlib.Path(args[1])
out.mkdir(parents=True, exist_ok=True)
start, end = (int(args[2]), int(args[3])) if len(args) >= 4 else (0, 0)
FLAGS = ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--hide-scrollbars']

with sync_playwright() as p:
    b = p.chromium.launch(channel='chrome', headless=True, args=FLAGS)
    pg = b.new_page(viewport={'width': 1920, 'height': 1080}, device_scale_factor=1)
    erros = []
    pg.on('pageerror', lambda e: erros.append(str(e)))
    pg.goto(page.as_uri(), wait_until='networkidle')
    pg.evaluate('window.__ready')
    if erros:
        sys.exit('ERRO NA PAGINA: ' + erros[0])
    if times:
        for t in times:
            pg.evaluate(f'window.__setTime({t})')
            pg.screenshot(path=str(out / f't_{t:06.2f}.png'))
    else:
        for f in range(start, end):
            dst = out / f'f_{f:05d}.png'
            if dst.exists() and dst.stat().st_size > 0:
                continue
            pg.evaluate(f'window.__setTime({f / 30})')
            tmp = str(dst) + '.tmp.png'
            pg.screenshot(path=tmp)
            os.replace(tmp, dst)
    b.close()
    if erros:
        sys.exit('ERRO NA PAGINA: ' + erros[0])
print('fim')
