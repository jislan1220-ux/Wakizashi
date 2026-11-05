"""Tira os tempos da narracao e da musica.
Uso: analisar.py narracao musica inicio_musica "texto digitado" [pasta_do_projeto]
Gera analise/palavras.json e anim/peaks.js."""
import json, pathlib, sys
import librosa, numpy as np
from faster_whisper import WhisperModel

sys.stdout.reconfigure(encoding='utf8')
voz, mus, ini, txt = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4]
root = pathlib.Path(sys.argv[5] if len(sys.argv) > 5 else '.')
(root / 'analise').mkdir(parents=True, exist_ok=True)
(root / 'anim').mkdir(parents=True, exist_ok=True)

a16, _ = librosa.load(voz, sr=16000, mono=True)
dur = len(a16) / 16000
print('NARRACAO', round(dur, 2), 's')
model = WhisperModel('base', device='cpu', compute_type='int8')
segs, _ = model.transcribe(a16.astype(np.float32), language='pt', word_timestamps=True, beam_size=5, initial_prompt=txt[:800])
W = []
for s in segs:
    print(f'[{s.start:6.2f}-{s.end:6.2f}] {s.text}')
    W += [dict(w=w.word.strip(), s=round(w.start, 2), e=round(w.end, 2)) for w in s.words]
(root / 'analise' / 'palavras.json').write_text(json.dumps(W, ensure_ascii=False), encoding='utf8')
print(' '.join(f"{w['w']}@{w['s']}" for w in W))

y, sr = librosa.load(voz, sr=22050, mono=True)
iv = librosa.effects.split(y, top_db=35)
print('PAUSAS', [(round(float(iv[i][1] / sr), 2), round(float(iv[i + 1][0] / sr), 2)) for i in range(len(iv) - 1) if (iv[i + 1][0] - iv[i][1]) / sr > .18])

total = dur + 6
y, sr = librosa.load(mus, sr=22050, mono=True, offset=ini, duration=total)
tempo, beats = librosa.beat.beat_track(y=y, sr=sr, units='time')
print('TEMPO', round(float(np.atleast_1d(tempo)[0]), 1), 'BATIDAS', [round(float(x), 2) for x in beats])
rms = librosa.feature.rms(y=y, hop_length=sr // 2)[0]
print('FORCA por 0,5s', [(round(i * .5, 1), round(float(r), 2)) for i, r in enumerate(rms)])

hop = sr // 30
v = np.array([np.sqrt((y[i:i + hop] ** 2).mean()) for i in range(0, len(y) - hop, hop)])
v = np.clip(v / np.percentile(v, 98), 0, 1) ** 1.2
(root / 'anim' / 'peaks.js').write_text('const PEAKS=' + json.dumps([round(float(x), 3) for x in v]) + ';')
print('picos:', len(v), 'quadros em anim/peaks.js')
