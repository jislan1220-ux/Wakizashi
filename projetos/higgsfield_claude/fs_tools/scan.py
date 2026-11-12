import sys, json, re
from concurrent.futures import ThreadPoolExecutor
import pyarrow.parquet as pq
from huggingface_hub import HfFileSystem
fs = HfFileSystem()
N0, N1, OUT = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
CAT = {
 'rugido': [r'\broar', r'\bgrowl', r'monster', r'dragon', r'creature', r'beast'],
 'fogo_jato': [r'flamethrower', r'fire ?ball', r'fire ?burst', r'fire ?whoosh', r'flame ?burst', r'fire ?blast', r'\bignit', r'dragon ?breath'],
 'fogo_crepita': [r'crackl', r'campfire', r'\bburning\b', r'bonfire', r'fireplace'],
 'vento': [r'\bwind\b', r'\bgust', r'howling ?wind', r'\bstorm\b'],
 'asas': [r'\bwing', r'flap'],
 'passos_madeira': [r'footstep', r'\bsteps?\b', r'running', r'\brun\b', r'walking'],
 'madeira': [r'wood', r'wooden', r'bridge', r'plank', r'deck'],
 'grito': [r'scream', r'\byell', r'shout'],
 'passagem': [r'fly ?by', r'flyby', r'pass ?by', r'whoosh'],
}
def scan(i):
    p = f'datasets/0x3/freesound-laion-640k/data/train-{i:05d}-of-01352.parquet'
    try:
        t = pq.ParquetFile(fs.open(p, block_size=2**20)).read(columns=['title', 'tags', 'license', 'freesound_id', 'description']).to_pylist()
    except Exception as e:
        return []
    out = []
    for k, r in enumerate(t):
        if r['license'] != 0: continue
        txt = (r['title'] + ' ' + ' '.join(r['tags'] or []) + ' ' + (r['description'] or '')[:300]).lower()
        hits = {c: sum(bool(re.search(w, txt)) for w in ws) for c, ws in CAT.items()}
        hits = {c: h for c, h in hits.items() if h}
        if hits: out.append({'shard': i, 'row': k, 'id': r['freesound_id'], 'title': r['title'], 'tags': r['tags'], 'hits': hits})
    return out
res = []
with ThreadPoolExecutor(16) as ex:
    for o in ex.map(scan, range(N0, N1)): res += o
json.dump(res, open(OUT, 'w'))
print(len(res), 'candidatos')
