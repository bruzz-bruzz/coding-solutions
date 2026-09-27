# cook your dish here
for _ in range(int(input())):
    s = str(input()).split(" ")
    n,k = int(s[0]),int(s[1])
    arr = [0] * n
    while k > 0:
        if 0 in arr:
            idx = arr.index(0)
            arr[idx] += 1
            k -= 1
        else:
            for x in range(len(arr)):
                if arr[x] < 2:
                    arr[x] += 1
                    k -= 1
                    break
    print(arr.count(2) * 2)