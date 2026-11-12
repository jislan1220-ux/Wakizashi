"""Som das cenas Seedance com gravacoes REAIS (Freesound, licenca CC0, via dataset 0x3/freesound-laion-640k no Hugging Face).

Substitui os sons sintetizados de sfx_cenas_v21.py. Cada som e um recorte de uma gravacao real, com fade, salvo em
<pasta_sfx>/real_*.wav; os eventos sao somados aos do sfx_base.json.

Uso: python sons_reais_v21.py times.json pasta_gravacoes pasta_sfx sfx_base.json saida.json

Gravacoes (todas CC0, sem atribuicao obrigatoria):
  rugido_c  546391 'Dragon Roar' (Dreeme)          rugido_b 442964 'Dragon Roar' (qubodup)
  rugido_d  449820 'Monster Growl' (DylanTheFish)   asas_gigante 572216 'Giant Wings Flapping' (shatterstars)
  vento_a   516452 'wind noise' (queenjamjam)       vento_c 592324 'windy-sound' (mt_moon8)
  vento_gust 449996 'whoosh short mid' (DJT4NN3R)   fogo_burnair 242721 'burning air' (sergeeo)
  fogo_torch 483316 'R09-74-Fire Torch' (craigsmith) brasa_a 444127 'Lit Fireplace' (lurpsis)
  corre_b   273403 'wood 15c darkshoes run' (sturmankin)  madeira_range 504059 'Wood Floor Creaking Long' (Joao_Janz)
  grito_c   445007 'Man Scream2' (LayZerg)          grito_a 416543 'Male Scream 3' (tonsil5)
"""
import json, sys
import numpy as np, soundfile as sf
from scipy.signal import resample_poly

T, GRAV, PASTA, BASE, SAIDA = sys.argv[1:6]
SR = 48000


def rec(nome, a, b, fi=.03, fo=.15, vel=1.0):
    x, sr = sf.read(f'{GRAV}/{nome}.flac', always_2d=True); x = x.mean(1)
    if sr != SR: x = resample_poly(x, SR, sr)
    x = x[int(a * SR):int(b * SR)]
    if vel != 1.0: x = resample_poly(x, 100, int(100 * vel))      # acelera (passos correndo)
    n = len(x); e = np.ones(n)
    e[:int(fi * SR)] = np.linspace(0, 1, int(fi * SR)); e[n - int(fo * SR):] = np.linspace(1, 0, int(fo * SR))
    return x * e


def save(nome, x):
    sf.write(f'{PASTA}/{nome}.wav', (x / (np.abs(x).max() + 1e-9) * .9).astype(np.float32), SR)


def mix(*partes):
    n = max(len(p) + int(o * SR) for p, o, g in partes); y = np.zeros(n)
    for p, o, g in partes:
        i = int(o * SR); y[i:i + len(p)] += p / (np.abs(p).max() + 1e-9) * g
    return y


save('real_vento', rec('vento_a', 3.0, 12.6, .6, 1.0))
save('real_vento_grave', rec('vento_c', 0.0, 8.9, .5, 1.0))
save('real_rugido', mix((rec('rugido_c', .45, 4.4, .02, .5), 0, 1), (rec('rugido_d', 1.6, 4.6, .2, .6), .15, .55)))
save('real_rugido_janela', rec('rugido_b', 0.0, 3.1, .01, .4))
save('real_asas', rec('asas_gigante', .15, 7.6, .05, .4))
save('real_passagem', mix((rec('vento_gust', 0.0, 2.6, .01, .5), 0, 1), (rec('asas_gigante', .9, 1.4, .02, .2), .05, .7)))
save('real_fogo', mix((rec('fogo_burnair', 2.85, 4.7, .02, .4), 0, 1), (rec('fogo_torch', .68, 2.15, .01, .3), .02, .8)))
save('real_brasa', rec('brasa_a', 70.0, 73.2, .2, .5))
save('real_andando', rec('corre_b', 1.15, 2.45, .01, .08))
save('real_correndo', rec('corre_b', 5.95, 10.1, .01, .1, vel=1.45))
save('real_ponte', rec('madeira_range', 0.0, 2.08, .02, .3))
save('real_grito', rec('grito_c', .05, 2.2, .01, .3))
save('real_grito2', rec('grito_a', 0.0, 1.37, .01, .2))

J = json.load(open(T)); a, b = J['ins'][0]['t'], J['ins'][1]['t']; I1, I2 = J['ins']
E = json.load(open(BASE))
def ev(nome, t, db, az=(0, 0), el=(0, 0), rev=.3, al='inicio'):
    E.append({"nome": nome, "t": round(t, 3), "db": round(db, 1), "az": list(az), "el": list(el), "rev": rev, "alinhar": al})

# dragao: vento o tempo todo, rugido quando ele vira para a camera, asas batendo, passagem para o por do sol
ev('real_vento', a - .1, -19, (-60, 60), (.2, .4), rev=.15)
ev('real_vento_grave', a, -23, rev=.1)
ev('real_rugido', a + 1.0, -11, rev=.35)
ev('real_asas', a + 3.0, -13, (-30, 30), rev=.25)
ev('real_passagem', a + I1['q'] - .25, -10, (-90, 90), (.3, 0), rev=.3)

# cavaleiros: passos na ponte, dragao rosna na janela, baforada, gritos, bundas pegando fogo, fuga correndo
ev('real_andando', b + .02, -12, (-15, 15), rev=.15)
ev('real_ponte', b + .1, -21, rev=.15)
ev('real_rugido_janela', b + .55, -19, (60, 40), (.4, .4), rev=.45)
ev('real_fogo', b + .95, -9, (70, -30), (.3, 0), rev=.3)
ev('real_grito', b + 1.95, -16, (-25, -25), rev=.25)
ev('real_grito2', b + 2.15, -19, (30, 30), rev=.25)
ev('real_brasa', b + 2.3, -17, (-10, 10), rev=.15)
ev('real_correndo', b + 2.55, -9, (0, -40), rev=.15)
ev('real_correndo', b + I2['half'] + .05, -8, (0, 0), rev=.15)
ev('real_ponte', b + I2['half'] + .3, -19, rev=.15)
ev('real_brasa', b + I2['q'], -16, rev=.15)
ev('real_correndo', b + I2['q'] + .02, -9, (10, -20), rev=.15)

E.sort(key=lambda e: e['t'])
json.dump(E, open(SAIDA, 'w'), indent=0)
print(len(E), 'eventos')
