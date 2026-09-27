# cook your dish here
n = int(input())
from collections import defaultdict
s = str(input()).split(" ")
for x in range(len(s)):
    s[x] = int(s[x])
s.sort()
a,b = s[0],s[len(s) - 1]
m = (a+b) / 2
res = defaultdict(list)
for x in s:
    res[abs(x - m)].append(x)
maxx = min(res.keys())
print(min(res[maxx]))