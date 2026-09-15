n = int(input())
arr = str(input()).split(' ')
for x in range(len(arr)):
    arr[x] = int(arr[x])
arr.sort()
arr.pop()
print(max(arr) - min(arr))