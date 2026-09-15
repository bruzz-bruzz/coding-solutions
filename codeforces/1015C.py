s = str(input()).split(' ')
n,m = int(s[0]), int(s[1])
original,compressed = [],[]
diffs = []
while n > 0:
    s = str(input()).split(' ')
    original.append(int(s[0]))
    compressed.append(int(s[1]))
    diffs.append(int(s[0]) - int(s[1]))
    n -= 1
if sum(original) <= m:
    print(0)
elif sum(compressed) > m:
    print(-1)
else:
    diffs.sort()
    s = sum(original)
    res = 0
    while diffs:
        p = diffs.pop()
        if s <= m:
            break
        s -= p
        res += 1
    print(res)