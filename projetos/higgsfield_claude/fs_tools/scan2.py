import sys, json, re
from concurrent.futures import ThreadPoolExecutor
import pyarrow.parquet as pq
from huggingface_hub import HfFileSystem
fs = HfFileSystem()
N0, N1, OUT = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
KW = r'whoosh|swoosh|swish|woosh|impact|\bhit\b|slam|cinematic|trailer|\bboom\b|sub ?drop|bass ?drop|riser|uplifter|braam|reverse|\bclick|\bpop\b|keyboard|typing|shimmer|sparkle|twinkle|chime|shutter|laugh|giggle|woohoo|yay|cheer|armor|armour|chainmail|clank|sword|scream|roar|growl|dragon|fire|flame|wing|wind|footstep|wood|transition|glitch|swipe|riser|tension'
def scan(i):
    p = f'datasets/0x3/freesound-laion-640k/data/train-{i:05d}-of-01352.parquet'
    for _ in range(2):
        try:
            t = pq.ParquetFile(fs.open(p, block_size=2**20)).read(columns=['title', 'tags', 'license', 'freesound_id', 'description']).to_pylist(); break
        except Exception: t = []
    out = []
    for k, r in enumerate(t):
        if r['license'] != 0: continue
        txt = (r['title'] + ' ' + ' '.join(r['tags'] or [])).lower()
        if re.search(KW, txt): out.append({'shard': i, 'row': k, 'id': r['freesound_id'], 'title': r['title'], 'tags': r['tags'], 'desc': (r['description'] or '')[:200]})
    return out
res = []
with ThreadPoolExecutor(20) as ex:
    for o in ex.map(scan, range(N0, N1)): res += o
json.dump(res, open(OUT, 'w')); print(len(res), 'candidatos')
