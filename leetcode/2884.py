import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    res = {
        'name':[],
        'salary':[]
    }
    for x in range(len(employees)):
        c = employees.iloc[x]
        res['name'].append(c['name'])
        res['salary'].append(c['salary'] * 2)
    res = pd.DataFrame(res)
    return res