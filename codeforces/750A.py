s = str(input()).split(' ')
n,k = int(s[0]), int(s[1])
midnight = 24 * 60 
midnight -= k
cur = 20 * 60
res = 0
prob = 1
while prob <= n:
    if cur + (prob * 5) > midnight:
        break
    else:
        cur += prob * 5
        prob += 1
        res += 1
print(res)