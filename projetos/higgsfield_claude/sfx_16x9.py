"""Gera sfx_16x9.json: SFX do Katana (CC0) + pacote Pires, no tempo das palavras e da animacao 16:9."""
import json, random
r = random.Random(4)
E = []
def e(nome, t, db, az=(0, 0), el=(0, 0), rev=.25, al='pico'):
    E.append({"nome": nome, "t": round(t, 3), "db": db, "az": list(az), "el": list(el), "rev": rev, "alinhar": al})
def digita(t0, t1, db=-12, az=20):
    t = t0
    while t < t1:
        e(f"kt_key{r.randint(1,5)}", t, db + r.uniform(-2, 1), (az, az), rev=.05, al='inicio'); t += .055 + r.random() * .05
# 1 OLHA SO
e("kt_power", .0, -12, al='inicio'); e("kt_hit", .02, -9, (-15, -15)); e("kt_hit", .24, -8, (15, 15))
e("pv_impact", .88, -4, rev=.45); e("kt_boom", .88, -6, rev=.3); e("sub_drop", .88, -9, al='inicio')
# 2 nos
e("kt_data", 1.5, -10, (-90, 0)); e("kt_blip", 1.86, -9, (-30, -30)); e("kt_scan", 2.2, -13, (-20, 20))
e("kt_blip", 2.58, -9, (30, 30)); e("kt_sel", 2.8, -10, (30, 30))
e("kt_long2", 2.98, -7, (-90, 90), (-.4, .6)); e("kt_crack", 2.98, -6, rev=.4); e("kt_hitm", 3.0, -8)
# 3 CARALHO MUITO FODA
e("kt_riser", 3.58, -10, (-90, 270), (-1, 1), al='pico'); e("pv_impact", 3.58, -3, rev=.5); e("kt_boom", 3.58, -6)
e("kt_glitch", 3.6, -10); e("braam", 3.58, -9, al='inicio', rev=.6)
e("kt_hit", 4.20, -8, (-35, -35)); e("kt_hitm", 4.66, -6, (30, 30)); e("kt_boom2", 4.66, -5); e("kt_crack", 4.68, -9, (30, 30))
e("kt_wh2", 5.75, -9, (0, 90))
# 4 prompt
e("kt_wh1", 6.1, -10, (-60, 0)); e("kt_sel", 6.18, -11); digita(6.4, 7.35)
# 5 pipeline
for t, az in [(7.68, -50), (8.56, 0), (9.30, 25), (10.48, 55)]:
    e("kt_data2", t - .17, -14, (az - 40, az)); e("kt_blip", t, -8, (az, az))
e("kt_scan", 8.5, -15); e("pv_impact", 10.48, -6); e("kt_flash", 10.6, -8)
e("kt_long", 10.7, -9, (60, 180), (0, .8))
# 6 sem After
e("kt_err", 11.52, -7, (-30, -30)); e("kt_glitch2", 11.53, -9)
for t, az in [(12.24, -20), (12.5, -10), (12.78, 0), (13.1, 10)]:
    e("kt_err2", t, -11, (az, az)); e("kt_hitm", t, -15, (az, az))
e("kt_long2", 13.5, -7, (-90, 90), (.6, -.4)); e("kt_crack", 13.52, -5, rev=.4); e("kt_boom", 13.52, -6); e("kt_glitch", 13.55, -9)
# 7 e o melhor
e("kt_sel", 14.2, -10); e("kt_data", 14.6, -12, (0, 90))
# 8 3 dias gratis
e("kt_flash", 15.22, -6); e("pv_impact", 15.22, -6); e("kt_boom2", 15.22, -7)
e("kt_wh3", 16.25, -9, (-60, 0)); e("kt_hit", 16.30, -6); e("kt_wh3", 17.0, -9, (60, 0)); e("kt_hit", 17.06, -5); e("kt_boom", 17.06, -7); e("kt_crack", 17.08, -10)
# 9 cartao
e("kt_long", 17.64, -8, (-90, 30)); e("kt_hit", 18.36, -9, (10, 10)); e("kt_wh2", 19.3, -8, (0, 120))
# 10 comenta aqui
e("kt_sel", 19.56, -9); e("kt_scan", 19.6, -14); digita(20.46, 21.0, -11, 0); e("kt_blip", 21.15, -7, (35, 35))
e("kt_wh1", 21.92, -9); e("pv_impact", 21.98, -5); e("kt_hit", 21.98, -6, (-25, -25)); e("kt_hitm", 22.16, -7, (25, 25))
# 11 assinatura
e("pv_metallic_riser", 23.23, -9, (0, 720), (-1, 1), rev=.35); e("kt_long2", 23.2, -8, (-90, 90))
e("kt_crack", 23.22, -5, rev=.5); e("pv_impact", 23.25, -2, rev=.55); e("kt_boom", 23.25, -5); e("braam", 23.25, -6, al='inicio', rev=.7)
e("sub_queda", 23.25, -8, al='inicio'); e("pv_shine", 23.6, -10, (-20, 20), (.2, 1), rev=.6)
json.dump(E, open(__file__.replace('.py', '.json'), 'w'), indent=0)
print(len(E), 'eventos')
