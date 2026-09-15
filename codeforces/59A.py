s = str(input())
u,l = 0,0
for x in s:
    if x == x.lower():
        l += 1
    else:
        u += 1
if l == u:
    res = ''
    for x in s:
        res += x.lower()
    print(res)
else:
    res = ''
    if u > l:
        for x in s:
            res += x.upper()
    else:
        for x in s:
            res += x.lower()
    print(res)