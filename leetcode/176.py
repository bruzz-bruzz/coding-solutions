import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    arr = []
    for x in range(len(employee)):
        arr.append(employee.iloc[x]['salary'])
    arr = list(set(arr))
    arr.sort()
    d = {
        'SecondHighestSalary':[]
    }
    if len(arr) > 1:
        d['SecondHighestSalary'].append(arr[len(arr) - 2])
        res = pd.DataFrame(d)
        return res
    d['SecondHighestSalary'].append(None)
    res = pd.DataFrame(d)
    return res