// node render.js anim.html pasta_saida t1,t2,...
const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
(async () => {
  const [, , html, out, times] = process.argv;
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await pg.goto('file://' + path.resolve(html));
  await pg.evaluate(() => document.fonts.ready);
  for (const t of times.split(',').map(Number)) {
    await pg.evaluate(t => window.__setTime(t), t);
    await pg.waitForTimeout(60);
    await pg.screenshot({ path: `${out}/t_${t.toFixed(2).padStart(6, '0')}.png` });
  }
  await b.close();
})();
