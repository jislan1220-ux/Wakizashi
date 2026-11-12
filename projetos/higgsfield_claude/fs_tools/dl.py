import sys, json, os
from concurrent.futures import ThreadPoolExecutor
import pyarrow.parquet as pq
from huggingface_hub import HfFileSystem
fs = HfFileSystem(); OUT = sys.argv[1]; items = json.loads(sys.argv[2])
def get(it):
    nome, sh, row = it
    pf = pq.ParquetFile(fs.open(f'datasets/0x3/freesound-laion-640k/data/train-{sh:05d}-of-01352.parquet', block_size=2**20))
    acc = 0
    for g in range(pf.num_row_groups):
        n = pf.metadata.row_group(g).num_rows
        if row < acc + n:
            t = pf.read_row_group(g, columns=['audio', 'freesound_id', 'title', 'username', 'license']).to_pylist()[row - acc]
            ext = os.path.splitext(t['audio'].get('path') or 'x.wav')[1] or '.wav'
            open(f'{OUT}/{nome}{ext}', 'wb').write(t['audio']['bytes'])
            return f"{nome}{ext} id={t['freesound_id']} lic={t['license']} '{t['title']}' por {t['username']}"
        acc += n
with ThreadPoolExecutor(8) as ex:
    for r in ex.map(get, items): print(r)
