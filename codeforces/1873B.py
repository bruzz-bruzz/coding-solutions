t = int(input())
while t > 0:
    n = int(input())
    arr = str(input()).split(' ')
    for x in range(len(arr)):
        arr[x] = int(arr[x])
    arr.sort()
    arr[0] += 1
    s = 1
    for x in arr:
        s *= x
    print(s)
    t -= 1