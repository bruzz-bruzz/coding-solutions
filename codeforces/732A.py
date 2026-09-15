s = str(input()).split(' ')
k,r = int(s[0]), int(s[1])
res = 1
while ((k * res) - r) % 10 != 0 and (k * res) % 10 != 0:
    res += 1
print(res)