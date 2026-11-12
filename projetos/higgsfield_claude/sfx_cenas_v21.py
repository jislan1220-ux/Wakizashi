"""Som das cenas Seedance (v21): vento, rugido, asas, fogo, brasas, passos na ponte, passagem do dragao.

Tudo sintetizado (o Higgsfield estava sem creditos para gerar SFX) e mixado BAIXO, como som de cena de cinema,
por baixo da musica e dos efeitos de corte.

Uso: python sfx_cenas_v21.py times.json pasta_sfx sfx_base.json saida.json
- sintetiza <pasta_sfx>/cena_*.wav
- junta os eventos das cenas aos do sfx_base.json e grava saida.json
"""
import json, sys
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

SR = 48000
T, PASTA, BASE, SAIDA = sys.argv[1:5]
rng = np.random.RandomState(21)


def f(x, kind, fr, o=2):
    return sosfilt(butter(o, fr, kind, fs=SR, output='sos'), x)


def save(nome, x):
    x = x / (np.abs(x).max() + 1e-9) * 0.9
    wavfile.write(f'{PASTA}/{nome}.wav', SR, x.astype(np.float32))


def pink(n):
    w = rng.randn(n); b = np.cumsum(w); b -= np.convolve(b, np.ones(600) / 600, 'same'); return b / (np.abs(b).max() + 1e-9)


def var_bp(x, centers, q=1.4, B=1200):
    """passa-banda com centro variando no tempo (por blocos)"""
    out = np.zeros_like(x)
    for i in range(0, len(x), B):
        c = centers[min(i, len(centers) - 1)]
        seg = f(x[max(0, i - 3000):i + B], 'band', [c / q, min(c * q, 20000)])[-min(B, len(x) - i):]
        out[i:i + len(seg)] = seg
    return out


# --- vento: rajadas que sobem e descem (9 s) ---
n = int(9.5 * SR); tt = np.arange(n) / SR
gust = 0.55 + 0.45 * np.sin(2 * np.pi * tt / 3.1) * np.sin(2 * np.pi * tt / 1.7 + 1)
cent = 380 + 520 * (0.5 + 0.5 * np.sin(2 * np.pi * tt / 2.6))
x = var_bp(pink(n), cent, 1.6) * gust + f(pink(n), 'low', 260) * 0.6
x *= np.clip(tt / .6, 0, 1) * np.clip((tt[-1] - tt) / .8, 0, 1)
save('cena_vento', x)

# --- rugido do dragao: rosnado grave + respiracao, com formantes ---
n = int(2.4 * SR); tt = np.arange(n) / SR
env = np.clip(tt / .18, 0, 1) ** 1.5 * np.exp(-np.clip(tt - 1.3, 0, None) * 2.8)
f0 = 62 + 18 * np.exp(-tt * 1.4) + 4 * np.sin(2 * np.pi * 7.5 * tt) + 3 * rng.randn(n).cumsum() / np.sqrt(np.arange(1, n + 1))
ph = 2 * np.pi * np.cumsum(f0) / SR
saw = sum(np.sin(k * ph) / k for k in range(1, 30))
src = saw * (1 + .5 * rng.randn(n) * .3) + pink(n) * .9
form = sum(g * f(src, 'band', [c * .8, c * 1.25]) for c, g in ((420, 1), (900, .8), (2300, .35), (3400, .15)))
roar = np.tanh(2.5 * form * env) + .6 * np.sin(2 * np.pi * 38 * tt) * env
save('cena_rugido', roar)

# --- batida de asa: ar empurrado grave ---
n = int(.55 * SR); tt = np.arange(n) / SR
env = np.clip(tt / .12, 0, 1) ** 2 * np.exp(-np.clip(tt - .12, 0, None) * 9)
save('cena_asa', f(pink(n), 'low', 520) * env + f(pink(n), 'band', [300, 1600]) * env * .3)

# --- baforada de fogo: whoomph + rugido da chama + estalos ---
n = int(2.0 * SR); tt = np.arange(n) / SR
env = np.clip(tt / .08, 0, 1) * np.exp(-np.clip(tt - .9, 0, None) * 3)
body = var_bp(pink(n), 250 + 900 * np.clip(tt / .4, 0, 1), 2.2) * env
rumble = f(pink(n), 'low', 140) * env * 1.4
crk = np.zeros(n); idx = rng.choice(n, 260, replace=False); crk[idx] = rng.randn(260)
crk = f(crk, 'band', [1800, 7000]) * env * 3
save('cena_fogo', np.tanh(1.8 * (body + rumble + crk)))

# --- brasas: estalos esparsos e chiado (3 s) ---
n = int(3.0 * SR); tt = np.arange(n) / SR
crk = np.zeros(n); idx = rng.choice(n, 140, replace=False); crk[idx] = rng.randn(140) * rng.rand(140) ** 2
crk = f(crk, 'band', [1500, 8000]) * 4 + f(pink(n), 'band', [2500, 9000]) * .15
crk *= np.clip(tt / .2, 0, 1) * np.clip((tt[-1] - tt) / .5, 0, 1)
save('cena_brasa', crk)

# --- passo em ponte de madeira ---
n = int(.25 * SR); tt = np.arange(n) / SR
wood = sum(np.sin(2 * np.pi * fr * tt) * np.exp(-tt * d) * g for fr, d, g in ((140, 28, 1), (310, 40, .6), (620, 60, .3)))
click = f(rng.randn(n), 'band', [1500, 5000]) * np.exp(-tt * 300) * .4
save('cena_passo', wood + click)

# --- passagem do dragao: whoosh enorme que vem e vai ---
n = int(2.2 * SR); tt = np.arange(n) / SR
env = np.exp(-((tt - 1.1) / .45) ** 2)
cent = 300 + 1600 * env
save('cena_passagem', var_bp(pink(n), cent, 1.8) * env + f(pink(n), 'low', 180) * env * .8)

# ---------- eventos ----------
J = json.load(open(T)); I1, I2 = J['ins'][0], J['ins'][1]
E = json.load(open(BASE))
def ev(nome, t, db, az=(0, 0), el=(0, 0), rev=.35, al='inicio'):
    E.append({"nome": nome, "t": round(t, 3), "db": round(db, 1), "az": list(az), "el": list(el), "rev": rev, "alinhar": al})

# dragao (c1 em tela cheia a partir de 0,2 s do clipe; card com o1)
a = I1['t']
ev('cena_vento', a - .1, -21, (-60, 60), (.2, .4), rev=.25)          # vento durante toda a cena
ev('cena_rugido', a + 1.1, -15, (0, 0), (0, 0), rev=.45)             # o dragao vira e ruge (clipe 1,2 s)
for k in range(4): ev('cena_asa', a + 3.0 + k * .78, -15, (-40, 40), rev=.3)
for k in range(6): ev('cena_asa', a + I1['half'] + .3 + k * .8, -16, (30, -30), rev=.3)
ev('cena_passagem', a + I1['q'] - .2, -14, (-90, 90), (.3, 0), rev=.4)   # o dragao sai para o por do sol

# cavaleiros (c2 a partir de 1,0 s; card com o2 e depois c2 a partir de 4,0 s)
b = I2['t']
for k in range(4): ev('cena_passo', b + .05 + k * .26, -17, (-20 + k * 10, 0), rev=.2)             # andando na ponte
ev('cena_rugido', b + .75, -19, (60, 30), (.4, .4), rev=.5)                                        # dragao na janela
ev('cena_fogo', b + .95, -13, (70, -40), (.4, 0), rev=.4, al='inicio')                            # baforada (clipe 2,0 s)
ev('cena_brasa', b + 2.3, -12, (-20, 20), rev=.25)                                                 # bundas pegando fogo
for k in range(9): ev('cena_passo', b + 2.6 + k * .2, -16, (0, -40 + k * 5), rev=.2)            # fogem correndo
for k in range(14): ev('cena_passo', b + I2['half'] + .1 + k * .2, -15, (0, 0), rev=.2)         # correndo pela ponte (o2)
ev('cena_vento', b + I2['half'], -27, (40, -40), rev=.2)
ev('cena_brasa', b + I2['q'], -12, (0, 0), rev=.25)                                                # fogem queimados (c2)
for k in range(7): ev('cena_passo', b + I2['q'] + .05 + k * .2, -16, (10, -20), rev=.2)

E.sort(key=lambda e: e['t'])
json.dump(E, open(SAIDA, 'w'), indent=0)
print(len(E), 'eventos')
