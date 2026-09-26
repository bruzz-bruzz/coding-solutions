import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    d = {
        'firstName':[],
        'lastName':[],
        'city':[],
        'state':[]
    }
    d1,d2,d3,d4 = {},{},{},{}
    for x in range(len(person)):
        c = person.iloc[x]
        d1[c['personId']] = c['lastName']
        d2[c['personId']] = c['firstName']
    for x in range(len(address)):
        c = address.iloc[x]
        d3[c['personId']] = c['city']
        d4[c['personId']] = c['state']
    k = list(d1.keys()) + list(d3.keys())
    s = set()
    for x in k:
        if x not in s and d2.get(x):
            d['firstName'].append(d2.get(x,None))
            d['lastName'].append(d1.get(x,None))
            d['city'].append(d3.get(x,None))
            d['state'].append(d4.get(x,None))
        s.add(x)
    res = pd.DataFrame(d)
    return res