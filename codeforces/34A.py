n = int(input())
arr = str(input()).split(' ')
from collections import defaultdict
d = defaultdict(list)
for x in range(len(arr)):
    d[int(arr[x])].append(x)
    arr[x] = int(arr[x])
res = []
k = list(d.keys())
k.sort()
arr = []
while k:
    p = k.pop(0)
    d[p].sort()
    for x in d[p]:
        arr.append(x)
print(arr[0] + 1, arr[1] + 1)