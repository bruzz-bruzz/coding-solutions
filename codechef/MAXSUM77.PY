t = int(input())
while t > 0:
    s = str(input()).split(" ")
    n,k = int(s[0]),int(s[1])
    arr = str(input()).split(" ")
    for x in range(len(arr)):
        arr[x] = int(arr[x])
    length = n - k
    summ = sum(arr[:length])
    res = summ
    for x in range(1,k + 1):
        summ = summ - arr[x - 1] + arr[length + x - 1]
        res = max(res,summ)
    print(res)
    t -= 1