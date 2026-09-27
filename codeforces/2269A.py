for _ in range(int(input())):
    s = input().split(" ")
    n,k = int(s[0]), int(s[1])
    res = 0
    arr = []
    for x in range(n):
        c = 2 ** (x + 1)
        if x >= k:
            arr.append(c / (2 ** k))
        else:
            arr.append(c)
    l = 0
    while k > 0:
        arr.pop(0)
        res += 2
        k -= 1
        l += 1
    print(int(sum(arr)+res))