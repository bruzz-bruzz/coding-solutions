n = int(input())
res = 0
while n > 0:
    if n - 5 >= 0:
        res += 1
        n -= 5
    elif n - 4 >= 0:
        res += 1
        n -= 4
    elif n - 3 >= 0:
        res += 1
        n -= 3
    elif n - 2 >= 0:
        res += 1
        n -= 2
    elif n - 1 >= 0:
        res += 1
        n -= 1
print(res)