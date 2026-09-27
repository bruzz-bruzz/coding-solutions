s = input().split(" ")
n,d = int(s[0]),int(s[1])
arr = [int(x) for x in input().split(" ")]
res = []
for x in range(n):
    c = 0
    for y in range(n):
        if x != y:
            if abs(arr[x] - arr[y]) >= d:
                c += 1
    if c == n - 1:
        res.append(str(x + 1))
print(len(res))
print(' '.join(res))