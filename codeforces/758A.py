cit = int(input())
welf = str(input()).split(' ')
m = 0
for x in welf:
    m = max(m,int(x))
res = 0
for x in welf:
    res += m - int(x)
print(res)