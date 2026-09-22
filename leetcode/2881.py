import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    res = {
        'name':[],
        'salary':[],
        'bonus':[]
    }
    for x in range(len(employees)):
        c = employees.iloc[x]
        res['name'].append(c['name'])
        res['salary'].append(c['salary'])
        res['bonus'].append(c['salary'] * 2)
    res = pd.DataFrame(res)
    return res