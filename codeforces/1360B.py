t = int(input())
while t > 0:
    n = int(input())
    s = str(input()).split(' ')
    for x in range(len(s)):
        s[x] = int(s[x])
    s.sort()
    dif = float('inf')
    for x in range(len(s) - 1):
        if s[x+1] - s[x] < dif:
            dif = s[x+1] - s[x]
    print(dif)
    t -= 1