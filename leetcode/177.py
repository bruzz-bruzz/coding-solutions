import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    arr = []
    for x in range(len(employee)):
        arr.append(employee.iloc[x]['salary'])
    arr = list(set(arr))
    arr.sort()
    d = {
        f'getNthHighestSalary({N})':[]
    }
    if len(arr) >= N and N > 0:
        d[f'getNthHighestSalary({N})'].append(arr[len(arr) - N])
        res = pd.DataFrame(d)
        return res
    d[f'getNthHighestSalary({N})'].append(None)
    res = pd.DataFrame(d)
    return res