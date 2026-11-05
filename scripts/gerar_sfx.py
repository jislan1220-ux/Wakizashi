"""Cria um kit de SFX por sintese, sem baixar nada e sem sons de terceiros.
Uso: gerar_sfx.py [pasta_saida] [--seed N]
Padrao: ~/video-tools/motion-vidro/sfx_gerados. Um seed diferente gera variacoes novas.
A pasta entra em --biblioteca no mixar.py, e o nome de cada .wav entra em sfx.json."""
import argparse, pathlib
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

SR = 48000
ap = argparse.ArgumentParser()
ap.add_argument('pasta', nargs='?', default=str(pathlib.Path.home() / 'video-tools' / 'motion-vidro' / 'sfx_gerados'))
ap.add_argument('--seed', type=int, default=7)
a = ap.parse_args()


def tempo(dur):
    return np.arange(int(dur * SR)) / SR


def filtro(x, tipo, freq, ordem=2):
    return sosfilt(butter(ordem, freq, tipo, fs=SR, output='sos'), x)


def varredura(x, corte, q=1.1):
    """Filtro passa-banda cujo centro acompanha a curva corte, amostra por amostra."""
    g = np.tan(np.pi * np.clip(corte, 20, SR * .45) / SR)
    k, ic1, ic2, y = 1 / q, 0.0, 0.0, np.zeros_like(x)
    for i, (s, gi) in enumerate(zip(x, g)):
        a1 = 1 / (1 + gi * (gi + k))
        v1 = a1 * (ic1 + gi * (s - ic2))
        v2 = ic2 + gi * v1
        ic1, ic2 = 2 * v1 - ic1, 2 * v2 - ic2
        y[i] = v1
    return y


def ruido(r, n):
    """Ruido mais encorpado que o branco, com menos agudo."""
    return filtro(r.standard_normal(n), 'low', 9000, 1) + .35 * r.standard_normal(n) * .3


def seno(freq):
    return np.sin(2 * np.pi * np.cumsum(freq) / SR)


def whoosh(r, dur, f0, f1, f2, pico=.62, largura=.9, corpo=0.0):
    """Sobe de f0 a f1 ate o pico e cai ate f2, passando de um ouvido para o outro."""
    t = tempo(dur)
    u = t / dur
    sobe = (u / pico).clip(0, 1) ** 2.2
    cai = ((1 - u) / (1 - pico)).clip(0, 1) ** 1.6
    env = sobe * cai
    corte = np.where(u < pico, f0 * (f1 / f0) ** (u / pico), f1 * (f2 / f1) ** ((u - pico) / (1 - pico)))
    e = varredura(ruido(r, len(t)), corte) * env
    d = varredura(ruido(r, len(t)), corte * 1.12) * env
    if corpo:
        grave = seno(np.clip(corte * .22, 28, 170)) * env ** 1.4 * corpo
        e, d = e + grave, d + grave
    lado = np.sin(np.pi * (u - .5)) * largura * .5
    return np.stack([e * (1 - lado), d * (1 + lado)], 1)


def riser(r, dur=3.0):
    t = tempo(dur)
    u = t / dur
    env = u ** 2.6
    corte = 180 * (7000 / 180) ** (u ** 1.3)
    e = varredura(ruido(r, len(t)), corte, 2.2) * env
    d = varredura(ruido(r, len(t)), corte * 1.06, 2.2) * env
    tom = seno(70 * (640 / 70) ** u)
    tom2 = seno(70.8 * (640 / 70) ** u)
    return np.stack([e + .10 * tom * env, d + .10 * tom2 * env], 1)


def clique_grave(r):
    t = tempo(.32)
    corpo = seno(58 + 115 * np.exp(-t / .018)) * np.exp(-t / .075)
    ataque = filtro(r.standard_normal(len(t)), 'high', 1800) * np.exp(-t / .0035) * .45
    x = np.tanh((corpo + ataque) * 1.6)
    return np.stack([x, x], 1)


def impacto(r):
    t = tempo(1.5)
    sub = seno(36 + 72 * np.exp(-t / .05)) * np.exp(-t / .42)
    estalo = filtro(r.standard_normal(len(t)), 'low', 3200) * np.exp(-t / .05) * .55
    cauda_e = filtro(r.standard_normal(len(t)), 'band', [90, 900]) * np.exp(-t / .3) * .16
    cauda_d = filtro(r.standard_normal(len(t)), 'band', [90, 900]) * np.exp(-t / .3) * .16
    return np.stack([np.tanh((sub + estalo + cauda_e) * 1.7), np.tanh((sub + estalo + cauda_d) * 1.7)], 1)


def tecla(r):
    t = tempo(.07)
    batida = filtro(r.standard_normal(len(t)), 'band', [r.uniform(1800, 2600), r.uniform(5200, 7500)]) * np.exp(-t / .006)
    fundo = seno(np.full(len(t), r.uniform(190, 280))) * np.exp(-t / .014) * .5
    x = batida + fundo
    return np.stack([x, x], 1)


def digitacao(r, dur=2.2):
    x = np.zeros((int(dur * SR), 2))
    p = .02
    while p < dur - .1:
        k = tecla(r) * r.uniform(.55, 1)
        i = int(p * SR)
        x[i:i + len(k)] += k
        p += r.uniform(.055, .15) + (r.uniform(.12, .28) if r.random() < .12 else 0)
    return x


def clique_ui(r):
    t = tempo(.11)
    x = seno(1750 * np.exp(-t / .05) + 500) * np.exp(-t / .016) + seno(np.full(len(t), 320.0)) * np.exp(-t / .012) * .6
    return np.stack([x, x], 1)


def salvar(pasta, nome, x):
    x = np.asarray(x, float)
    x = np.stack([filtro(x[:, 0], 'high', 22), filtro(x[:, 1], 'high', 22)], 1)
    n = min(int(.004 * SR), len(x) // 4)
    rampa = np.linspace(0, 1, n)[:, None]
    x[:n] *= rampa
    x[-n:] *= rampa[::-1]
    x = x / (np.abs(x).max() + 1e-9) * 10 ** (-1 / 20)
    wavfile.write(str(pasta / f'{nome}.wav'), SR, (x * 32767).astype(np.int16))
    print(f'{nome}.wav  {len(x) / SR:.2f} s')


pasta = pathlib.Path(a.pasta).expanduser()
pasta.mkdir(parents=True, exist_ok=True)
r = np.random.default_rng(a.seed)
sons = {
    'whoosh_curto_1': lambda: whoosh(r, .38, 500, 5200, 1500),
    'whoosh_curto_2': lambda: whoosh(r, .46, 380, 3900, 1100, .55),
    'whoosh_curto_3': lambda: whoosh(r, .34, 700, 6500, 2200, .68),
    'whoosh_medio_1': lambda: whoosh(r, .8, 260, 3400, 700),
    'whoosh_medio_2': lambda: whoosh(r, .95, 200, 2700, 520, .58),
    'whoosh_grave': lambda: whoosh(r, 1.15, 90, 950, 110, .5, .6, .9),
    'whoosh_reverso': lambda: whoosh(r, 1.0, 240, 4200, 1500, .97, .8, .25),
    'riser': lambda: riser(r),
    'clique_grave': lambda: clique_grave(r),
    'impacto': lambda: impacto(r),
    'clique_ui': lambda: clique_ui(r),
    'tecla': lambda: tecla(r),
    'digitacao': lambda: digitacao(r),
}
for nome, gerar in sons.items():
    salvar(pasta, nome, gerar())
print('Pasta:', pasta)
