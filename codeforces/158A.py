inp = str(input()).split(' ')
n,k = int(inp[0]), int(inp[1])
arr = str(input()).split(' ')
res = 0
for x in range(len(arr)):
    if int(arr[x]) >= int(arr[k-1]) and int(arr[x]) > 0:
        res += 1
print(res)