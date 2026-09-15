n = int(input())
res = [[1] * n]
s = 1 * n
for x in range(1,n):
    tmp = [1]
    for y in range(1,n):
        tmp.append(res[x-1][y] + tmp[y-1])
        s = max(s,res[x-1][y] + tmp[y-1])
    res.append(tmp)
print(s)