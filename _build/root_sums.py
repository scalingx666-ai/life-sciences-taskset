import hashlib, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
rows = []
for sub in ['data/chembl', 'data/vcc']:
    for fn in sorted(os.listdir(os.path.join(R, sub))):
        p = os.path.join(R, sub, fn)
        if os.path.isfile(p):
            rows.append(sha(p) + '  ' + sub + '/' + fn)
open(R + '/SHA256SUMS', 'w').write(chr(10).join(rows) + chr(10))
print('ROOT_SHA_ROWS', len(rows))