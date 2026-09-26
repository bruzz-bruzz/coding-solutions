import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    d2 = {
        'score':[],
        'rank':[]
    }
    d = {}
    for x in range(len(scores)):
        c = scores.iloc[x]
        d[c['score']] = 1 + d.get(c['score'],0)
    k = list(d.keys())
    k.sort(reverse=True)
    for x in range(len(k)):
        for _ in range(d[k[x]]):
            d2['score'].append(k[x])
            d2['rank'].append(x + 1)
    d2 = pd.DataFrame(d2)
    return d2