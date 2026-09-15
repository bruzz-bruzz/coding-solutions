s = str(input()).split(' ')
n,h = int(s[0]),int(s[1])
arr = str(input()).split(' ')
res = 0
for x in arr:
    if int(x) > h:
        res += 2
    else:
        res += 1
print(res)