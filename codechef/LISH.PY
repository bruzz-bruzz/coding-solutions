# cook your dish here
w = int(input())
n = int(input())
s = str(input()).split(" ")
for x in range(len(s)):
    s[x] = int(s[x])
s.sort()
summ = 0
c = 0
res = []
while s:
    p = s.pop()
    if summ + p >= w:
        c += 1
        summ += p
        break
    elif summ + (p * 2) >= w:
        c += 2
        summ += p * 2
        break
    else:
        c += 2
        summ += p * 2
if summ >= w:
    print(c)
else:
    print(-1)