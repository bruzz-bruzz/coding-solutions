num = int(input())
arr = str(input()).split(' ')
prev = [int(arr.pop(0))]
res = 0
while arr:
    curr = arr.pop(0)
    if int(curr) < min(prev) or int(curr) > max(prev):
        res += 1
    prev.append(int(curr))
print(res)