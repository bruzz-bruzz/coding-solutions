n = int(input())
res = [2]
if n == 1:
    print(2)
else:
    for x in range(1,n):
        res.append((2*(res[x-1])) + 2)
    print(res.pop())