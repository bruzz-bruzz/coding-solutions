num = str(input())
res = 0
for x in num:
    if x == '4' or x == '7':
        res += 1
res = str(res)
ret = True
for x in res:
    if x != '4' and x != '7':
        ret = False
if not ret:
    print("NO")
else:
    print("YES")