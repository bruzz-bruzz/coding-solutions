s = str(input())
sett = set(s)
sett.remove('{')
sett.remove('}')
if ',' in sett:
    sett.remove(',')
if ' ' in sett:
    sett.remove(' ')
print(len(sett))