curr = int(input())
res = 0
while curr != 0:
    arr = input().split(' ')
    if arr.count('1') >= 2:
        res += 1
    curr -= 1
print(res)