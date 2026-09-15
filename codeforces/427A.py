n = int(input())
cur = 0
s = str(input()).split(' ')
res = 0
for x in s:
    if int(x) < 0:
        if cur + int(x) >= 0:
            cur += int(x)
        else:
            res += 1
    else:
        cur += int(x)
print(res)
