"""SFX da v22: so gravacoes reais (Freesound CC0), no motion e nas cenas.

Motion: whooshes de trailer (EpicSoundEffects e outros), impacto "Michael Bay", boom com sub, kick grande, risers, prato
reverso, BWAAAM, cliques de interface, digitacao de iPhone, brilhos.
Cenas: os sons reais da v21 (vento, rugido, asas, fogo, brasas, passos, gritos) + armadura dos cavaleiros + risada da moca.

Uso: python sfx_v22.py times.json pasta_gravacoes_motion pasta_gravacoes_cenas pasta_sfx saida.json
(os real_* da v21 precisam ja estar em pasta_sfx: rodar sons_reais_v21.py antes)
"""
import json, sys
import numpy as np, soundfile as sf
from scipy.signal import resample_poly

T, G2, G1, PASTA, SAIDA = sys.argv[1:6]
SR = 48000


def rec(nome, a=0, b=None, fi=.005, fo=.08, vel=1.0, pasta=None):
    x, sr = sf.read(f'{pasta or G2}/{nome}.flac', always_2d=True); x = x.mean(1)
    if sr != SR: x = resample_poly(x, SR, sr)
    x = x[int(a * SR):(int(b * SR) if b else None)]
    if vel != 1.0: x = resample_poly(x, 100, int(100 * vel))
    n = len(x); e = np.ones(n); fi_n = max(1, int(fi * SR)); fo_n = max(1, int(fo * SR))
    e[:fi_n] = np.linspace(0, 1, fi_n); e[n - fo_n:] = np.linspace(1, 0, fo_n)
    return x * e


def save(nome, x):
    sf.write(f'{PASTA}/{nome}.wav', (x / (np.abs(x).max() + 1e-9) * .9).astype(np.float32), SR)


# ---------- motion ----------
save('m_wh1', rec('wh_tennis', 0, .48))
save('m_wh2', rec('wh_movC', 0, .39))
save('m_wh3', rec('wh_transB', 0, 1.0, fo=.3))
save('m_wh4', rec('wh_simple11', 1.15, 2.6, fo=.3))
save('m_wh_grave', rec('wh_weighted', 0, 2.2, fo=.6))
save('m_kick', rec('im_bigkick', .06, 1.4, fo=.4))
save('m_bay', rec('im_bay', .3, 5.0, fo=1.5))
save('m_boom', rec('im_tgnboom', 0, 4.0, fo=1.2))
save('m_impact', rec('im_crazy15', 0, 1.6, fo=.5))
save('m_metal', rec('im_metal', 0, 2.0, fo=.8))
save('m_sub', rec('sub_lofreq', 0, 5.5, fo=1.5))
save('m_riser', rec('ri_riser2', 3.2, 6.95, fi=.4, fo=.02))
save('m_revcymb', rec('ri_revcymb', 4.0, 5.96, fi=.3, fo=.01))
save('m_swell', rec('ri_swell', 1.2, 3.25, fi=.3, fo=.05))
save('m_energy', rec('ri_energy', 0, .72, fo=.02))
save('m_bwaam', rec('br_bwaam', 0, 4.5, fo=1.5))
save('m_braam', rec('br_braam4', .2, 4.5, fo=1.5))
save('m_click', rec('ui_click02', .08, .5, fo=.1))
save('m_click2', rec('ui_click213', 0, .3, fo=.08))
save('m_typing', rec('ty_iphone', .3, 2.1, fo=.1))
save('m_glitter', rec('sh_glitter', .25, 2.5, fo=.8))
save('m_chimes', rec('sh_chimes', .95, 3.6, fo=1.0))
# personagens
save('p_armadura_anda', rec('ar_walk', 35.9, 40.8, fo=.3))
save('p_armadura_corre', rec('ar_walk', 35.9, 40.8, fo=.3, vel=1.6))
save('p_armadura_tranco', rec('ar_mov', .1, 2.0, fo=.4))
save('p_risada', rec('ri_ooh', .1, 2.1, fo=.3))
save('p_risada2', rec('ri_laugh2', .05, .77, fo=.15))

# ---------- eventos ----------
J = json.load(open(T)); INS = J['ins']
E = []
def ev(nome, t, db, az=(0, 0), el=(0, 0), rev=.1, al='pico'):
    if t >= 0: E.append({"nome": nome, "t": round(t, 3), "db": round(db, 1), "az": list(az), "el": list(el), "rev": rev, "alinhar": al})
def kw(w, n=0):
    L = [t for t, x in J['kw'] if x.lower().strip('“') == w.strip('“')]
    return L[min(n, len(L) - 1)]

WH = ['m_wh1', 'm_wh2', 'm_wh3', 'm_wh4']
# cortes de cena: whoosh de trailer passando no corte + kick grande + impacto
for i, c in enumerate(J['cuts']):
    side = -1 if i % 2 == 0 else 1
    ev(WH[i % 4], c, -8, (side * 90, -side * 30), rev=.08)
    ev('m_kick', c, -7, al='inicio', rev=.05)
    ev('m_impact', c, -15, al='inicio', rev=.15)

# insercoes Seedance: prato reverso + riser -> BWAAAM + impacto Michael Bay + sub
for k, I in enumerate(INS):
    a = I['t']; side = -1 if k % 2 == 0 else 1
    ev('m_riser', a, -14, (side * 60, 0), (.3, .6), rev=.15)
    ev('m_revcymb', a, -13, rev=.1)
    ev('m_bay', a, -6, al='inicio', rev=.3)
    ev('m_bwaam', a, -10, al='inicio', rev=.35)
    ev('m_sub', a, -9, al='inicio', rev=.1)
    ev('m_glitter', a + .45, -16, (side * 40, -side * 40), (.5, .5), rev=.3, al='inicio')
    h = a + I['half']  # tela cheia -> card
    ev('m_wh_grave', h, -8, (side * 120, 0), rev=.1)
    ev('m_wh3', h, -12, (-side * 60, 0), rev=.1)
    ev('m_kick', h, -6, al='inicio', rev=.05)
    ev('m_impact', h, -11, al='inicio', rev=.2)
    q = a + I['q']  # corte dentro do card
    ev('m_wh1', q, -10, (-side * 100, 0), rev=.08)
    ev('m_kick', q, -10, al='inicio', rev=.05)

# batidas de destaque que nao sao corte
cortes = J['cuts'] + [I['t'] + d for I in INS for d in (0, I['half'], I['q'])]
for t, k in J['hits']:
    if min(abs(t - c) for c in cortes) < .08: continue
    ev('m_kick', t, -12 + 4 * k, al='inicio', rev=.05)
    if k >= .85: ev('m_impact', t, -14, al='inicio', rev=.2)

# palavras-chave: clique real bem baixo
for i, (t, w) in enumerate(J['kw']):
    ev('m_click' if i % 2 else 'm_click2', t, -21, ((-1) ** i * 35, 0), rev=.05, al='inicio')

# abertura: swell e drop com boom
ev('m_energy', .88, -12); ev('m_kick', .88, -5, al='inicio'); ev('m_boom', .88, -10, al='inicio', rev=.2)

# "Caralho, é muito FODA": impacto metalico + boom
foda = kw('foda')
ev('m_metal', foda, -14, al='inicio', rev=.3); ev('m_boom', foda, -12, al='inicio', rev=.2)

# digitacao (prompt e comentario) e envio
ev('m_typing', kw('falo') - .02, -15, (10, 10), rev=.05, al='inicio')
ev('m_typing', kw('higgsfield”', 1), -15, (10, 10), rev=.05, al='inicio')
ev('m_click', kw('higgsfield”', 1) + .69, -14, al='inicio')

# "sem After": cada item riscado
for t in [kw('after,') + d for d in (.72, .98, 1.26, 1.58)]:
    ev('m_click2', t, -15, ((-1) ** int(t * 10) * 50, 0), al='inicio')

# "3 dias gratis": brilho + swell
g = kw('grátis')
ev('m_swell', g, -13); ev('m_chimes', g, -13, (0, 0), (.6, .6), rev=.35, al='inicio')

# final KATANA
e = J['end']
ev('m_revcymb', e + .05, -11); ev('m_riser', e + .05, -14, rev=.15)
ev('m_kick', e + .05, -4, al='inicio'); ev('m_bay', e + .05, -5, al='inicio', rev=.35)
ev('m_braam', e + .05, -10, al='inicio', rev=.4); ev('m_sub', e + .05, -9, al='inicio')
ev('m_chimes', e + .45, -15, rev=.4, al='inicio')

# ---------- cenas e personagens (sons reais) ----------
a, b = INS[0]['t'], INS[1]['t']; I1, I2 = INS
def evc(nome, t, db, az=(0, 0), el=(0, 0), rev=.3): ev(nome, t, db, az, el, rev, 'inicio')
evc('real_vento', a - .1, -19, (-60, 60), (.2, .4), rev=.15)
evc('real_vento_grave', a, -23, rev=.1)
evc('real_rugido', a + 1.0, -10, rev=.35)
evc('real_asas', a + 3.0, -13, (-30, 30), rev=.25)
evc('p_risada', a + I1['half'] + .5, -17, (25, 15), rev=.2)          # a moca rindo no dragao
evc('p_risada2', a + I1['half'] + 2.6, -19, (30, 20), rev=.2)
evc('real_passagem', a + I1['q'] - .25, -10, (-90, 90), (.3, 0), rev=.3)
evc('real_andando', b + .02, -12, (-15, 15), rev=.15)
evc('p_armadura_anda', b + .02, -16, (-15, 15), rev=.15)              # armadura do cavaleiro
evc('real_ponte', b + .1, -21, rev=.15)
evc('real_rugido_janela', b + .55, -18, (60, 40), (.4, .4), rev=.45)
evc('real_fogo', b + .95, -8, (70, -30), (.3, 0), rev=.3)
evc('p_armadura_tranco', b + 1.6, -15, (-20, 0), rev=.2)              # leva o susto
evc('real_grito', b + 1.95, -15, (-25, -25), rev=.25)
evc('real_grito2', b + 2.15, -18, (30, 30), rev=.25)
evc('real_brasa', b + 2.3, -16, (-10, 10), rev=.15)
evc('real_correndo', b + 2.55, -9, (0, -40), rev=.15)
evc('p_armadura_corre', b + 2.55, -14, (0, -40), rev=.15)
evc('real_correndo', b + I2['half'] + .05, -8, rev=.15)
evc('p_armadura_corre', b + I2['half'] + .05, -13, rev=.15)
evc('real_ponte', b + I2['half'] + .3, -19, rev=.15)
evc('real_brasa', b + I2['q'], -15, rev=.15)
evc('real_correndo', b + I2['q'] + .02, -9, (10, -20), rev=.15)
evc('p_armadura_corre', b + I2['q'] + .02, -14, (10, -20), rev=.15)

E.sort(key=lambda x: x['t'])
json.dump(E, open(SAIDA, 'w'), indent=0)
print(len(E), 'eventos')
