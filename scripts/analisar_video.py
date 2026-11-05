"""Estuda um video enviado: quadros, cortes secos, ritmo e volume.
Uso: analisar_video.py video pasta_saida [num_quadros]   (padrao: 16 quadros)
Gera folha.png, resumo.json e audio.wav (se o video tiver som)."""
import json, math, pathlib, re, subprocess, sys, tempfile
import librosa, numpy as np

sys.stdout.reconfigure(encoding='utf8')
if len(sys.argv) < 3:
    sys.exit(__doc__)
video, saida = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
N = int(sys.argv[3]) if len(sys.argv) > 3 else 16
if not video.exists():
    sys.exit(f'video nao encontrado: {video}')
saida.mkdir(parents=True, exist_ok=True)

def ff(*x):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-y', *x], capture_output=True, text=True, encoding='utf8', errors='ignore')
    if r.returncode:
        sys.exit(r.stderr[-800:])
    return r.stderr

p = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration:stream=codec_type,width,height,avg_frame_rate', '-of', 'json', str(video)], capture_output=True, text=True, encoding='utf8', errors='ignore')
if p.returncode:
    sys.exit(f'nao consegui abrir o video: {p.stderr[:200]}')
info = json.loads(p.stdout)
dur = float(info['format']['duration'])
v = next((s for s in info['streams'] if s['codec_type'] == 'video'), None)
if not v:
    sys.exit('o arquivo nao tem imagem')
tem_som = any(s['codec_type'] == 'audio' for s in info['streams'])
a, b = v['avg_frame_rate'].split('/')
resumo = dict(arquivo=video.name, duracao_s=round(dur, 2), largura=v['width'], altura=v['height'], fps=round(int(a) / max(int(b), 1), 2), tem_som=tem_som)

log = ff('-i', str(video), '-vf', "scale=320:-2,select='gt(scene,0.3)',showinfo", '-an', '-f', 'null', '-')
cortes = [round(float(x), 2) for x in re.findall(r'pts_time:([\d.]+)', log)]
pontos = [0] + cortes + [dur]
planos = np.diff(pontos)
resumo.update(cortes_secos=len(cortes), cortes_por_minuto=round(len(cortes) / dur * 60, 1), plano_medio_s=round(float(planos.mean()), 2), plano_mais_longo_s=round(float(planos.max()), 2), tempos_dos_cortes=cortes)

cols = 4
larg = 480 if v['width'] >= v['height'] else 270
with tempfile.TemporaryDirectory() as d:
    for i in range(N):
        ff('-ss', f'{dur * (i + .5) / N:.3f}', '-i', str(video), '-frames:v', '1', '-update', '1', f'{d}/s_{i:04d}.png')
    ff('-i', f'{d}/s_%04d.png', '-vf', f'scale={larg}:-2,tile={cols}x{math.ceil(N / cols)}', '-frames:v', '1', '-update', '1', str(saida / 'folha.png'))
resumo['tempos_da_folha'] = [round(dur * (i + .5) / N, 2) for i in range(N)]

if tem_som:
    wav = saida / 'audio.wav'
    ff('-i', str(video), '-vn', '-ac', '2', '-ar', '48000', str(wav))
    achados = re.findall(r'I:\s+(-?[\d.]+) LUFS', ff('-i', str(wav), '-af', 'ebur128', '-f', 'null', '-'))
    resumo['volume_lufs'] = float(achados[-1]) if achados else None
    y, sr = librosa.load(str(wav), sr=22050, mono=True)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    resumo['batidas_por_minuto'] = round(float(np.atleast_1d(tempo)[0]), 1)
    trechos = librosa.effects.split(y, top_db=35)
    resumo['parte_com_som'] = round(float(sum(f - i for i, f in trechos) / len(y)), 2)

(saida / 'resumo.json').write_text(json.dumps(resumo, ensure_ascii=False, indent=1), encoding='utf8')
print(json.dumps({k: x for k, x in resumo.items() if not k.startswith('tempos')}, ensure_ascii=False))
print('Abra', saida / 'folha.png', 'e olhe os quadros antes de opinar.')
