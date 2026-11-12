"""SFX de cinema sintetizados (sem sons de terceiros): passagem com doppler, hit metalico,
swell reverso, riser longo e cauda de impacto. Uso: sfx_cinema.py pasta_sfx"""
import sys, pathlib, numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

SR = 48000; pasta = pathlib.Path(sys.argv[1]); r = np.random.RandomState(5)
def f(x, k, fr, o=2): return sosfilt(butter(o, fr, k, fs=SR, output='sos'), x)
def tt(d): return np.arange(int(d * SR)) / SR
def salvar(nome, x):
    x = np.asarray(x, float); n = int(.004 * SR); x[:n] *= np.linspace(0, 1, n); x[-n:] *= np.linspace(1, 0, n)
    wavfile.write(str(pasta / f'{nome}.wav'), SR, (x / (np.abs(x).max() + 1e-9) * 0.89 * 32767).astype(np.int16))
def varre(x, centros, q=0.9, bloco=480):
    y = np.zeros_like(x)
    for i in range(0, len(x), bloco):
        c = float(np.clip(centros[i], 80, SR / 4.5)); a, b = max(0, i - 4 * bloco), min(len(x), i + bloco)
        y[i:b] = f(x[a:b], 'band', [c / (1 + q), min(c * (1 + q), SR / 2.05)])[-(b - i):]
    return y

# passagem com doppler: a fonte chega, passa rente e vai embora
d = 1.4; t = tt(d); u = t / d
corpo = np.exp(-((u - 0.55) / 0.17) ** 2)
pitch = 1 + 0.35 * np.tanh(-(u - 0.55) * 9)
tom = np.sin(2 * np.pi * np.cumsum(140 * pitch) / SR) + 0.5 * np.sin(2 * np.pi * np.cumsum(283 * pitch) / SR)
ar = varre(r.randn(len(t)), 900 * pitch ** 3 + 1600 * corpo)
salvar('passagem_doppler', (ar * 1.2 + tom * 0.35) * corpo)

# whoosh pesado de camera mergulhando
d = 1.1; t = tt(d); u = t / d; corpo = np.exp(-((u - 0.6) / 0.2) ** 2)
ar = varre(r.randn(len(t)), 300 + 3500 * corpo, q=1.2)
sub = np.sin(2 * np.pi * np.cumsum(60 + 50 * corpo) / SR) * corpo
salvar('mergulho', ar * corpo + sub * 0.7)

# hit metalico para palavra batendo na tela
d = 1.8; t = tt(d)
parc = [(173, 1.0, .9), (419, .7, .6), (787, .5, .4), (1290, .35, .3), (2113, .25, .2), (3307, .18, .12)]
met = sum(a * np.sin(2 * np.pi * fr * t + r.rand() * 6) * np.exp(-t / dec) for fr, a, dec in parc)
clique = f(r.randn(len(t)), 'high', 1500) * np.exp(-t / 0.012)
thump = np.sin(2 * np.pi * np.cumsum(45 + 90 * np.exp(-t / 0.03)) / SR) * np.exp(-t / 0.18)
salvar('hit_metal', met * 0.5 + clique * 0.8 + thump * 1.1)

# swell reverso: ar crescendo ate o impacto
d = 1.6; t = tt(d); u = t / d
sw = varre(r.randn(len(t)), 1500 + 7000 * u ** 3, q=2.5) * u ** 3
salvar('swell_reverso', sw + 0.4 * np.sin(2 * np.pi * np.cumsum(50 + 40 * u) / SR) * u ** 2)

# riser longo com tensao: ruido e serras subindo, tremolo acelerando
d = 3.4; t = tt(d); u = t / d
fr = 110 * 2 ** (2.2 * u ** 1.6)
serra = sum(2 * ((fr * k * (1 + dt) * t) % 1) - 1 for k, dt in ((1, 0), (1, .006), (2, -.004)))
trem = 0.6 + 0.4 * np.sin(2 * np.pi * np.cumsum(3 + 22 * u ** 2) / SR)
rui = varre(r.randn(len(t)), 500 + 9000 * u ** 2)
salvar('riser_cinema', (f(serra, 'low', 1800) * 0.25 + rui) * u ** 2.2 * trem)

# queda de grave para a logo
d = 3.0; t = tt(d)
salvar('sub_queda', np.tanh(1.8 * np.sin(2 * np.pi * np.cumsum(25 + 70 * np.exp(-t / 0.5)) / SR)) * np.exp(-t / 1.1) * np.minimum(1, t / .01))
print('ok')
