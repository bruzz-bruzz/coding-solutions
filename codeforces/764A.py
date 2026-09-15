s = str(input()).split(' ')
n,m,z = int(s[0]), int(s[1]), int(s[2])
c,d = n,m
a,b = [],[]
while n <= z:
    a.append(n)
    n += c
while m <= z:
    b.append(m)
    m += d
res = 0
for x in a:
    if x in b:
        res += 1
print(res)