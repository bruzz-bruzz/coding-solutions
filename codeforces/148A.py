k,l,m,n,d = int(input()),int(input()),int(input()),int(input()),int(input())
res = 0
for x in range(1,d+1):
    if x % k == 0:
        res += 1
    elif x % l == 0:
        res += 1
    elif x % m == 0:
        res += 1
    elif x % n == 0:
        res += 1
print(res)