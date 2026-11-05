"""Monta os arquivos finais a partir de <entrega>/_frames, stems/ e mix.wav.
Uso: empacotar.py pasta_entrega nome [--so-preview]
Gera preview_<nome>.mp4 e, sem --so-preview, <nome>.mov (ProRes 422 HQ), <nome>_com_audio.mov e timeline.fcpxml.
Para com erro se quadros ou duracao nao baterem."""
import json, pathlib, subprocess, sys

args = [x for x in sys.argv[1:] if x != '--so-preview']
so_preview = '--so-preview' in sys.argv
R, nome = pathlib.Path(args[0]), args[1]
frames = R / '_frames'
N = len(list(frames.glob('f_*.png')))
if not N:
    sys.exit('sem quadros em ' + str(frames))
fim = sorted(frames.glob('f_*.png'))[-1].stem
if int(fim[2:]) != N - 1:
    sys.exit(f'faltam quadros: {N} arquivos, ultimo {fim}')
if not (R / 'mix.wav').exists():
    sys.exit('falta mix.wav')
DUR = N / 30

def ff(*x):
    subprocess.run(['ffmpeg', '-y', '-v', 'error', *x], check=True)

def checar(arq, audio=False):
    p = subprocess.run(['ffprobe', '-v', 'error', '-count_packets', '-show_entries', 'stream=codec_type,nb_read_packets', '-show_entries', 'format=duration', '-of', 'json', str(arq)], capture_output=True, text=True)
    if p.returncode:
        sys.exit(f'{arq} NAO ABRE: {p.stderr[:200]}')
    d = json.loads(p.stdout)
    v = [s for s in d['streams'] if s['codec_type'] == 'video']
    if v and int(v[0]['nb_read_packets']) != N:
        sys.exit(f'{arq}: {v[0]["nb_read_packets"]} quadros, esperava {N}')
    if abs(float(d['format']['duration']) - DUR) > .05:
        sys.exit(f'{arq}: duracao {d["format"]["duration"]}, esperava {DUR}')
    if audio and not any(s['codec_type'] == 'audio' for s in d['streams']):
        sys.exit(f'{arq}: sem audio')
    print('ok', arq, round(arq.stat().st_size / 1e6), 'MB')

seq = str(frames / 'f_%05d.png')
prev = R / f'preview_{nome}.mp4'
ff('-framerate', '30', '-i', seq, '-i', str(R / 'mix.wav'), '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-t', str(DUR), str(prev))
checar(prev, True)
if so_preview:
    sys.exit(0)

mov = R / f'{nome}.mov'
ff('-framerate', '30', '-i', seq, '-c:v', 'prores_ks', '-profile:v', '3', '-pix_fmt', 'yuv422p10le', '-vendor', 'apl0', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-an', str(mov))
checar(mov)
junto = R / f'{nome}_com_audio.mov'
ff('-i', str(mov), '-i', str(R / 'mix.wav'), '-map', '0:v:0', '-map', '1:a:0', '-c:v', 'copy', '-c:a', 'pcm_s24le', '-ar', '48000', '-t', str(DUR), str(junto))
checar(junto, True)

faltam = [s for s in ('voz', 'trilha', 'sfx') if not (R / 'stems' / f'{s}.wav').exists()]
if faltam:
    sys.exit(f'faltam stems: {faltam}')
for s in ('voz', 'trilha', 'sfx'):
    checar(R / 'stems' / f'{s}.wav')

d = f'{N}/30s'
ativos = ''.join(f'    <asset id="r{i}" name="{s}" src="stems/{s}.wav" start="0s" duration="{d}" hasAudio="1" audioSources="1" audioChannels="2" audioRate="48000"/>\n' for i, s in enumerate(('voz', 'trilha', 'sfx'), 3))
clipes = ''.join(f'              <asset-clip name="{s}" ref="r{i}" lane="-{i - 2}" offset="0s" start="0s" duration="{d}" audioRole="{p}"/>\n' for i, (s, p) in enumerate((('voz', 'dialogue'), ('trilha', 'music'), ('sfx', 'effects')), 3))
(R / 'timeline.fcpxml').write_text(f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE fcpxml>
<fcpxml version="1.9">
  <resources>
    <format id="r1" name="FFVideoFormat1080p30" frameDuration="1/30s" width="1920" height="1080"/>
    <asset id="r2" name="{nome}" src="{nome}.mov" start="0s" duration="{d}" hasVideo="1" format="r1"/>
{ativos}  </resources>
  <library>
    <event name="Motion">
      <project name="{nome}">
        <sequence format="r1" duration="{d}" tcStart="0s" tcFormat="NDF" audioLayout="stereo" audioRate="48k">
          <spine>
            <asset-clip name="{nome}" ref="r2" offset="0s" start="0s" duration="{d}" format="r1">
{clipes}            </asset-clip>
          </spine>
        </sequence>
      </project>
    </event>
  </library>
</fcpxml>
''', encoding='utf8')
print('pacote pronto:', N, 'quadros,', DUR, 's')
