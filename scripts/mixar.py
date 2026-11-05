"""Monta voz, trilha e SFX com os niveis aprovados.
Uso: mixar.py narracao musica inicio_musica duracao sfx.json pasta_entrega [--biblioteca PASTA] [--impacto 9.9] [--cta 31.6]

sfx.json e uma lista de eventos:
  {"nome": "Whoosh_Deep_Short_grave", "t": 9.92, "db": -5}            pico do som cai em t
  {"nome": "Digitacao_Sequencia", "t": 4.18, "db": -13, "alinhar": "inicio"}   comeca em t
  {"tecla": [5.1, 5.55], "db": -19}                                   teclas soltas; usa tecla.wav ou o arquivo em "som"

--impacto: ate esse tempo a musica sobe de 80% a 100%.
--cta: a partir desse tempo a musica sobe 45% para a chamada final.
Gera stems/, mix.wav e audio_para_aprovar.mp3."""
import argparse, functools, json, pathlib, re, subprocess
import librosa, numpy as np
from scipy.io import wavfile

ap = argparse.ArgumentParser()
for n in ('narracao', 'musica'): ap.add_argument(n)
ap.add_argument('inicio', type=float); ap.add_argument('dur', type=float)
ap.add_argument('sfx'); ap.add_argument('entrega')
ap.add_argument('--biblioteca', default='biblioteca_sfx')
ap.add_argument('--impacto', type=float, default=None); ap.add_argument('--cta', type=float, default=None)
a = ap.parse_args()
SR, DUR, LIB = 48000, a.dur, pathlib.Path(a.biblioteca)
ROOT = pathlib.Path(a.entrega); OUT = ROOT / 'stems'; OUT.mkdir(parents=True, exist_ok=True)
imp = a.impacto if a.impacto is not None else DUR * .3
cta = a.cta if a.cta is not None else DUR + 1
trk = np.zeros((int((DUR + 2) * SR), 2))

@functools.lru_cache(maxsize=None)
def carregar(nome):
    x, _ = librosa.load(str(LIB / f'{nome}.wav'), sr=SR, mono=False)
    x = np.atleast_2d(x)
    if x.shape[0] == 1: x = np.vstack([x, x])
    x = x[:2] / (np.abs(x).max() + 1e-9)
    env = np.convolve((x ** 2).sum(0), np.ones(960) / 960, 'same')
    return x.T, int(env.argmax())

def por(nome, t, db, alinhar='pico'):
    x, pk = carregar(nome); i = int(t * SR) - (pk if alinhar == 'pico' else 0); g = 10 ** (db / 20)
    c = max(0, -i); i = max(0, i); n = min(len(x) - c, len(trk) - i)
    if n > 0: trk[i:i + n] += x[c:c + n] * g

for ev in json.load(open(a.sfx, encoding='utf8')):
    if 'tecla' in ev:
        t0, t1 = ev['tecla']; r = np.random.RandomState(int(t0 * 10)); t = t0
        while t < t1:
            por(ev.get('som', 'tecla'), t, ev.get('db', -20) + r.rand() * 3, 'inicio'); t += .07 + r.rand() * .06
    else:
        por(ev['nome'], ev['t'], ev.get('db', -10), ev.get('alinhar', 'pico'))

def ff(*x):
    r = subprocess.run(['ffmpeg', '-y', '-hide_banner', *x], capture_output=True, text=True, encoding='utf8', errors='ignore')
    if r.returncode: raise SystemExit(r.stderr[-1500:])
    return r.stderr

trk = trk[:int(DUR * SR)]
sfx = OUT / 'sfx.wav'
wavfile.write(str(sfx), SR, trk.astype(np.float32))
s = ff('-i', str(sfx), '-af', 'ebur128', '-f', 'null', '-')
lufs = float(re.findall(r'I:\s+(-?[\d.]+) LUFS', s)[-1])
wavfile.write(str(sfx), SR, (trk * 10 ** ((-24.2 - lufs) / 20)).astype(np.float32))

voz = OUT / 'voz.wav'
ff('-i', a.narracao, '-af', f'aresample={SR},aformat=channel_layouts=stereo,highpass=f=80,afftdn=nf=-30,acompressor=threshold=-20dB:ratio=3:attack=8:release=120:makeup=3dB,equalizer=f=3000:t=q:w=1.2:g=2,deesser=i=0.35,apad=whole_dur={DUR}', '-t', str(DUR), '-c:a', 'pcm_f32le', str(voz))
# graves parados no centro; o resto gira devagar entre os ouvidos; abaixa sob a voz
ff('-ss', str(a.inicio), '-t', str(DUR), '-i', a.musica, '-i', str(voz), '-filter_complex',
   f"[0:a]aresample={SR},aformat=channel_layouts=stereo,volume=-16.5dB,volume='if(lt(t,{imp}),0.8+0.2*t/{imp},if(lt(t,{cta}),1,1.45))':eval=frame,afade=t=in:st=0:d=0.08,afade=t=out:st={DUR - 1.6}:d=1.6,asplit=2[ma][mb];[ma]lowpass=f=160[lo];[mb]highpass=f=160,apulsator=hz=0.125:amount=0.9:mode=sine[hi];[lo][hi]amix=inputs=2:normalize=0[m];[1:a]asplit=2[k][x];[x]anullsink;[m][k]sidechaincompress=threshold=0.04:ratio=6:attack=10:release=300,apad=whole_dur={DUR}[d]",
   '-map', '[d]', '-t', str(DUR), '-c:a', 'pcm_f32le', str(OUT / 'trilha.wav'))

mix = str(ROOT / 'mix.wav')
fc = '[0:a][1:a][2:a]amix=inputs=3:normalize=0:duration=first[a]'
base = ['-i', str(voz), '-i', str(OUT / 'trilha.wav'), '-i', str(sfx)]
s = ff(*base, '-filter_complex', fc + ';[a]loudnorm=I=-14:TP=-1:LRA=11:print_format=json[o]', '-map', '[o]', '-f', 'null', '-')
j = json.loads(s[s.rindex('{'):s.rindex('}') + 1])
ff(*base, '-filter_complex', fc + f";[a]loudnorm=I=-14:TP=-1:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true[l];[l]aresample={SR},aformat=sample_fmts=s32:channel_layouts=stereo[o]", '-map', '[o]', '-t', str(DUR), '-c:a', 'pcm_s24le', mix)
ff('-i', mix, '-c:a', 'libmp3lame', '-b:a', '320k', str(ROOT / 'audio_para_aprovar.mp3'))
s = ff('-i', mix, '-af', 'ebur128=peak=true', '-f', 'null', '-')
print(s[s.rindex('Summary:'):][:320])
