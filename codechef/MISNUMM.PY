# cook your dish here
n = int(input())
s = str(input()).split(" ")
m = int(input())
s2 = str(input()).split(" ")
d1,d2 = {},{}
for x in s:
    d1[x] = 1 + d1.get(x,0)
for x in s2:
    d2[x] = 1 + d2.get(x,0)
res = []
k = set(list(d1.keys()) + list(d2.keys()))
for x in k:
    if d1.get(x,0) < d2.get(x,0):
        res.append(int(x))
res.sort()
for x in range(len(res)):
    res[x] = str(res[x])
if res:
    print(' '.join(res))
else:
    print(-1)