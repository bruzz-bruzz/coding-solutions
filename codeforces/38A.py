n = int(input())
arr = str(input()).split(' ')
inp = str(input()).split(' ')
res = 0
for x in range(int(inp[0]) - 1, int(inp[1]) - 1):
    res += int(arr[x])
print(res)