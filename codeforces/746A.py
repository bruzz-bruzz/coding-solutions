lemons = int(input())
apples = int(input())
pears = int(input())
res = 0
for x in range(1,lemons + 1):
    temp = [x, x * 2, x * 4]
    if temp[0] > lemons or temp[1] > apples or temp[2] > pears:
        break
    else:
        res += 7
print(res)