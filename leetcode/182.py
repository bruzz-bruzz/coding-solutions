import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    s = set()
    arr = set()
    for x in range(len(person)):
        c = person.iloc[x]
        if c['email'] in s:
            arr.add(c['email'])
        s.add(c['email'])
    res = pd.DataFrame({
        'Email':[x for x in arr]
    })
    return res