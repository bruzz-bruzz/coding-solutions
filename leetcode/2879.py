import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    res = {
        'employee_id':[],
        'name':[],
        'department':[],
        'salary':[]
    }
    for x in range(3):
        c = employees.iloc[x]
        res['employee_id'].append(c['employee_id'])
        res['name'].append(c['name'])
        res['department'].append(c['department'])
        res['salary'].append(c['salary'])
    res = pd.DataFrame(res)
    return res