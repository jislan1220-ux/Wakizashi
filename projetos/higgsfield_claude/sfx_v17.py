"""SFX da v17 (igual a v16, com duracao por insercao e tempos tirados da animacao):

SFX da v16: som de motion "gostoso", seco e no corte.

- Sintetiza one-shots limpos (swoosh de ar que termina no corte, kick de sub, pop, tick, swell reverso)
  e salva em <pasta_sfx>/v16_*.wav.
- Monta o mapa de eventos do zero a partir dos tempos reais da animacao (times16.json, exportado do anim.html):
  cada corte = swoosh chegando + kick no quadro do corte; palavras-chave = pop; insercoes Seedance =
  riser -> braam/sub -> brilho no titulo; final com riser metalico.
- Sai sem os sons sci-fi de interface (erro, bip, scan, data, glitch, teclas), que deixavam o som barato.

Uso: python sfx_v16.py times16.json pasta_sfx saida.json
"""
import json, sys
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

SR = 48000
T, PASTA, SAIDA = sys.argv[1], sys.argv[2], sys.argv[3]
rng = np.random.RandomState(16)


def bp(x, lo, hi, o=2):
    return sosfilt(butter(o, [lo, hi], 'band', fs=SR, output='sos'), x)


def save(nome, x):
    x = x / (np.abs(x).max() + 1e-9) * 0.9
    wavfile.write(f'{PASTA}/{nome}.wav', SR, x.astype(np.float32))


def sweep_noise(dur, f0, f1, curve):
    """ruido rosa passando por um filtro que varre de f0 a f1 (em blocos), com envelope curve."""
    n = int(dur * SR); w = rng.randn(n)
    pink = np.cumsum(w); pink = pink - np.convolve(pink, np.ones(400) / 400, 'same'); pink /= np.abs(pink).max()
    out = np.zeros(n); B = 960
    for i in range(0, n, B):
        u = i / n; f = f0 * (f1 / f0) ** u
        seg = bp(pink[max(0, i - 2000):i + B], f * 0.6, min(f * 1.8, 20000))[-min(B, n - i):]
        out[i:i + len(seg)] = seg
    return out * curve(np.linspace(0, 1, n))


# --- swoosh de ar: cresce e PARA seco no corte (pico no fim) ---
for k, (dur, f0, f1) in enumerate([(.34, 350, 4200), (.42, 250, 3200), (.28, 500, 6000)]):
    x = sweep_noise(dur, f0, f1, lambda u: u ** 2.6)
    x[-int(.004 * SR):] *= np.linspace(1, 0, int(.004 * SR))
    save(f'v16_swoosh{k + 1}', x)

# --- swoosh que sai depois do corte (cauda curta descendo) ---
x = sweep_noise(.32, 5000, 300, lambda u: np.exp(-u * 5) * np.clip(u * 40, 0, 1))
save('v16_tail', x)

# --- kick de sub: corpo grave com queda de pitch + clique de ataque ---
n = int(.55 * SR); tt = np.arange(n) / SR
f = 42 + 110 * np.exp(-tt * 38); ph = 2 * np.pi * np.cumsum(f) / SR
body = np.sin(ph) * np.exp(-tt * 6.5)
click = bp(rng.randn(n), 1800, 6000) * np.exp(-tt * 260) * 0.5
save('v16_kick', np.tanh(2.2 * (body + click)))

# --- kick leve (para as batidas menores) ---
n = int(.3 * SR); tt = np.arange(n) / SR
f = 55 + 90 * np.exp(-tt * 45); ph = 2 * np.pi * np.cumsum(f) / SR
save('v16_kick_leve', np.tanh(1.6 * (np.sin(ph) * np.exp(-tt * 11) + bp(rng.randn(n), 2500, 7000) * np.exp(-tt * 400) * .35)))

# --- pop: bolha suave para palavra-chave ---
n = int(.12 * SR); tt = np.arange(n) / SR
f = 380 + 1100 * np.exp(-tt * 70); ph = 2 * np.pi * np.cumsum(f) / SR
env = np.clip(tt / .002, 0, 1) * np.exp(-tt * 38)
save('v16_pop', (np.sin(ph) + .25 * np.sin(2 * ph)) * env)

# --- tick: madeira/vidro curto, para elementos de interface ---
n = int(.08 * SR); tt = np.arange(n) / SR
save('v16_tick', (np.sin(2 * np.pi * 2300 * tt) * np.exp(-tt * 90) + bp(rng.randn(n), 3000, 8000) * np.exp(-tt * 300) * .4))

# --- swell reverso: sobe para dentro do corte grande ---
n = int(1.1 * SR); tt = np.arange(n) / SR
tone = sum(np.sin(2 * np.pi * fr * tt + rng.rand() * 6) for fr in (110, 165, 220, 330))
noise = bp(rng.randn(n), 300, 5000)
x = (tone * .5 + noise * .6) * (tt / tt[-1]) ** 3.2
x[-int(.003 * SR):] *= np.linspace(1, 0, int(.003 * SR))
save('v16_swell', x)

# ---------- mapa de eventos ----------
J = json.load(open(T))
E = []
def ev(nome, t, db, az=(0, 0), el=(0, 0), rev=.12, al='pico'):
    if t >= 0: E.append({"nome": nome, "t": round(t, 3), "db": round(db, 1), "az": list(az), "el": list(el), "rev": rev, "alinhar": al})

INS = J['ins']  # [{t, len, half, q}]

# cortes de cena: swoosh chegando + kick no quadro do corte + cauda saindo
for i, c in enumerate(J['cuts']):
    side = -1 if i % 2 == 0 else 1
    ev(f'v16_swoosh{i % 3 + 1}', c - .004, -9, (side * 100, 0), rev=.08)
    ev('v16_kick', c, -6, al='inicio', rev=.05)
    ev('v16_tail', c + .01, -15, (0, -side * 90), rev=.15, al='inicio')
    ev('pv_impact', c, -14, rev=.15)

# insercoes Seedance
for k, I in enumerate(INS):
    a = I['t']; side = -1 if k % 2 == 0 else 1
    ev('pv_suspense_riser', a - .01, -13, (side * 60, 0), (.3, .6), rev=.2)
    ev('v16_swell', a - .003, -11, rev=.1)
    ev('v16_kick', a, -4, al='inicio', rev=.05)
    ev('braam', a, -10, rev=.35)
    ev('sub_drop', a, -10, rev=.2)
    ev('pv_impact', a, -8, rev=.25)
    ev('pv_shine', a + .45, -13, (side * 40, -side * 40), (.5, .5), rev=.3)
    h = a + I['half']  # tela cheia -> card
    ev('v16_swoosh2', h - .004, -8, (side * 120, 0), rev=.08)
    ev('v16_kick', h, -5, al='inicio', rev=.05)
    ev('pv_impact', h, -9, rev=.2)
    ev('pv_echo_snap', h + .02, -14, rev=.25)
    q = a + I['q']  # corte dentro do card
    ev('v16_swoosh3', q - .004, -10, (-side * 100, 0), rev=.08)
    ev('v16_kick_leve', q, -7, al='inicio', rev=.05)
    ev('v16_tail', a + I['len'] - .2, -12, (0, side * 90), rev=.15, al='inicio')

# batidas de destaque (as que nao sao corte): kick leve
cortes = J['cuts'] + [I['t'] + d for I in INS for d in (0, I['half'], I['q'])]
for t, k in J['hits']:
    if min(abs(t - c) for c in cortes) < .08: continue
    ev('v16_kick_leve' if k < .85 else 'v16_kick', t, -9 + 3 * k, al='inicio', rev=.05)
    if k >= .85: ev('pv_impact', t, -10, rev=.2)

# palavras-chave: pop suave, passeando de um lado para o outro
for i, (t, w) in enumerate(J['kw']):
    ev('v16_pop', t, -17, ((-1) ** i * 35, (-1) ** i * 35), (.2, .2), rev=.1, al='inicio')

def kw(w, n=0):
    """tempo da n-esima ocorrencia de uma palavra-chave (comparando sem aspas e em minusculas)"""
    L = [t for t, x in J['kw'] if x.lower().strip('“') == w.strip('“')]
    return L[min(n, len(L) - 1)]

# abertura: celular liga e o drop
ev('pv_digital_camera_power_on', 0.0, -13, rev=.1, al='inicio')
ev('v16_swell', 0.88, -12); ev('v16_kick', 0.88, -4, al='inicio'); ev('sub_drop', 0.88, -10)

# "Caralho, é muito FODA": brilho e cauda grave
foda = [t for t, w in J['kw'] if w.lower().startswith('foda')][0]
ev('pv_shine', foda + .05, -12, rev=.3); ev('boom_cauda', foda, -12, rev=.3)

# digitacao do prompt e do comentario: teclado de celular, sem metralhadora de teclas
ev('pv_phone_typing', kw('falo') - .02, -14, (10, 10), rev=.05, al='inicio')
ev('pv_phone_typing', kw('higgsfield”', 1), -14, (10, 10), rev=.05, al='inicio')
ev('v16_tick', J['phr'][9], -14, al='inicio'); ev('pv_digital_camera_click', kw('higgsfield”', 1) + .69, -15, al='inicio')

# "sem After": cada item riscado leva um snap
for t in [kw('after,') + d for d in (.72, .98, 1.26, 1.58)]:
    ev('pv_echo_snap', t, -15, ((-1) ** int(t * 10) * 50, 0), rev=.15)

# oferta "3 dias gratis": brilho
g = [t for t, w in J['kw'] if w.lower().startswith('grátis')][0]
ev('pv_shine', g, -10, (0, 0), (.6, .6), rev=.35)

# final KATANA
e = J['end']
ev('pv_metallic_riser', e + .03, -11, rev=.2)
ev('v16_swell', e + .045, -9)
ev('v16_kick', e + .05, -3, al='inicio'); ev('pv_impact', e + .05, -5, rev=.35)
ev('braam', e + .05, -9, rev=.4); ev('sub_queda', e + .05, -10, rev=.2)
ev('pv_shine', e + .45, -11, rev=.4)

E.sort(key=lambda x: x['t'])
json.dump(E, open(SAIDA, 'w'), indent=0)
print(len(E), 'eventos')
