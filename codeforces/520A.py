n = int(input())
s = str(input())
sett = set()
for x in s:
    sett.add(x.lower())
if len(sett) == 26:
    print("YES")
else:
    print("NO")