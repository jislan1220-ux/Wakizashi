"""Junta imagens de uma pasta em uma folha para conferir.
Uso: folha.py pasta saida.png [colunas] [largura]   (padrao: 4 colunas, 640 px)"""
import pathlib, shutil, subprocess, sys, tempfile

pasta, saida = pathlib.Path(sys.argv[1]), sys.argv[2]
cols = int(sys.argv[3]) if len(sys.argv) > 3 else 4
larg = int(sys.argv[4]) if len(sys.argv) > 4 else 640
imgs = sorted(pasta.glob('t_*.png')) or sorted(pasta.glob('*.png'))
if not imgs:
    sys.exit('nenhuma imagem em ' + str(pasta))
lin = -(-len(imgs) // cols)
with tempfile.TemporaryDirectory() as d:
    for i, f in enumerate(imgs):
        shutil.copy(f, f'{d}/s_{i:04d}.png')
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', f'{d}/s_%04d.png', '-vf', f'scale={larg}:-1,tile={cols}x{lin}', '-frames:v', '1', '-update', '1', saida], check=True)
print(saida, len(imgs), 'imagens')
