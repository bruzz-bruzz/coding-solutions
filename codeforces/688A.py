s = str(input()).split(' ')
n,d = int(s[0]),int(s[1])
res = 0
cur = 0
while d > 0:
    s = str(input())
    if s.count('1') != len(s):
        cur += 1
    else:
        res = max(res,cur)
        cur = 0
    d -= 1
if cur:
    res = max(res,cur)
print(res)