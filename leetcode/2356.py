import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    td = defaultdict(set)
    res = {
        'teacher_id':[],
        'cnt':[]
    }
    for x in range(len(teacher)):
        c = teacher.iloc[x]
        td[c['teacher_id']].add(c['subject_id'])
    for x in td:
        res['teacher_id'].append(x)
        res['cnt'].append(len(td[x]))
    res = pd.DataFrame(res)
    return res