n = int(input())
arr = []
if n % 2 == 1:
    print(-1)
else:
    for x in range(1,n+1):
        arr.append(str(x))
    arr.reverse()
    print(' '.join(arr))