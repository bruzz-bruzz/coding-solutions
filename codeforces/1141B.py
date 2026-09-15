n = int(input())
arr = str(input()).split(' ')
res = 0
for x in range(len(arr)):
    arr.append(arr[x])
while arr:
    p = arr.pop(0)
    if p == '1':
        tmp = 1
        while arr:
            p2 = arr.pop(0)
            if p2 == '0':
                break
            tmp += 1
        res = max(res,tmp)
print(res)