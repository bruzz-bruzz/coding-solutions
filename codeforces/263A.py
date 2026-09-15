arr = []
for x in range(5):
    arr.append(str(input()).split(' '))
for x in range(len(arr)):
    for y in range(len(arr[x])):
        if arr[x][y] == '1':
            print(abs(x-2) + abs(y-2))
