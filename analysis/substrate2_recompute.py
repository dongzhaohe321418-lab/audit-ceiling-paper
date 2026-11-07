"""Study 23 (BigCodeBench), third run: independent recomputation of union flag rates from the raw readings."""
import json, itertools, random, collections
R='records/code/substrate2/'
a=json.load(open(R+'audit_set.json')); ids=set(a['instance_ids'])
inst={json.loads(l)['instance_id']:json.loads(l) for l in open(R+'instances.jsonl') if l.strip()}
def readings(fam):
    out={}
    for d in range(1,9):
        for l in open(R+f'cache/holistic__{fam}__d{d}.jsonl'):
            r=json.loads(l)
            if r['instance_id'] in ids and r.get('ok', True): out[(r['instance_id'],d)]=bool(r['flagged'])
    return out
for fam in ('cross','self'):
    rd=readings(fam)
    for stratum in ('P','C'):
        S=sorted(i for i in ids if inst[i]['stratum']==stratum)
        full=[i for i in S if all((i,d) in rd for d in range(1,9))]
        res=[]
        for K in (1,2,4,8):
            subs=list(itertools.combinations(range(1,9),K))
            v=[sum(any(rd[(i,d)] for d in s) for s in subs)/len(subs) for i in full]
            res.append((K, round(100*sum(v)/len(v),1)))
        # cluster bootstrap at K=8
        byp=collections.defaultdict(list)
        for i in full: byp[inst[i]['problem_id']].append(float(any(rd[(i,d)] for d in range(1,9))))
        P=list(byp); rng=random.Random(0); dr=[]
        for _ in range(4000):
            vs=[x for p in (rng.choice(P) for _ in P) for x in byp[p]]; dr.append(sum(vs)/len(vs))
        dr.sort()
        print(fam, stratum, len(S), len(full), res, 'K8 CI', round(100*dr[100],1), round(100*dr[3899],1))
