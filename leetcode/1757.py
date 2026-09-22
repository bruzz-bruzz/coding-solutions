import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    d = {
        'product_id':[]
    }
    for x in range(len(products)):
        c = products.iloc[x]
        if c['low_fats'] == 'Y' and c['recyclable'] == 'Y':
            d['product_id'].append(c['product_id'])
    res = pd.DataFrame(d)
    return res