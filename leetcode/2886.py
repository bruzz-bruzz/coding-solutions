import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    d = {
        'student_id':[],
        'name':[],
        'age':[],
        'grade':[]
    }
    for x in range(len(students)):
        c = students.iloc[x]
        d['student_id'].append(c['student_id'])
        d['name'].append(c['name'])
        d['age'].append(c['age'])
        d['grade'].append(int(c['grade']))
    d = pd.DataFrame(d)
    return d