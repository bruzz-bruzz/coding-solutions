from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in str(input()).split(" ")]
    m = 0
    d = {}
    for x in arr:
        m = max(m,x)
        d[x] = 1 + d.get(x,0)
    k = list(d.keys())
    k.sort(reverse=True)
    res = []
    while True:
        num = None
        for x in k:
            if d[x] > 0:
                num = x
                break
        if not num:
            break
        t = d[num]
        for _ in range(t):
            res.append(str(num))
        d[num] = 0
        for x in k:
            if d[x] > 0:
                t2 = min(d[x],t)
                for _ in range(t2):
                    res.append(str(x))
                    d[x] -= 1
    print(' '.join(res))