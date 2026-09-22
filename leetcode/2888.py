import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    res = {
        'student_id':[],
        'name':[],
        'age':[]
    }
    for x in range(len(df1)):
        c = df1.iloc[x]
        res['student_id'].append(c['student_id'])
        res['name'].append(c['name'])
        res['age'].append(c['age'])
    for x in range(len(df2)):
        c = df2.iloc[x]
        res['student_id'].append(c['student_id'])
        res['name'].append(c['name'])
        res['age'].append(c['age'])
    res = pd.DataFrame(res)
    return res