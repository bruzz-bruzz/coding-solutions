n= int(input())
s = str(input()).split(' ')
for x in range(len(s)):
    s[x] = int(s[x])
sereja,dima = 0,0
cur = 1
while s:
    l,r = s[0],s[len(s) - 1]
    if l > r:
        if cur % 2 != 0:
            sereja += s.pop(0)
        else:
            dima += s.pop(0)
    else:
        if cur % 2 != 0:
            sereja += s.pop(len(s) - 1)
        else:
            dima += s.pop(len(s) - 1)
    cur += 1
print(sereja,dima)