import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    c = {}
    s = set()
    for x in range(len(customers)):
        cur = customers.iloc[x]
        c[cur['id']] = cur['name']
    for x in range(len(orders)):
        s.add(orders.iloc[x]['customerId'])
    d = {
        'Customers':[]
    }
    for x in c.keys():
        if x not in s:
            d['Customers'].append(c[x])
    d = pd.DataFrame(d)
    return d