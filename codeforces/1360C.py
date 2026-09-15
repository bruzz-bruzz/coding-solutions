t = int(input())
def isParity(a,b):
    if a % 2 == b % 2:
        return True
    elif abs(a-b) == 1:
        return True
    else:
        return False
while t > 0:
    n = int(input())
    arr = str(input()).split(' ')
    for x in range(len(arr)):
        arr[x] = int(arr[x])
    arr.sort()
    c = 0
    for x in range(len(arr) // 2):
        if isParity(arr[x*2],arr[(x*2)+1]):
            c += 1
    if c == len(arr) // 2:
        print("YES")
    else:
        print("NO")
    t -= 1