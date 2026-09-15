s = str(input()).split(' ')
k,n,w = int(s[0]),int(s[1]),int(s[2])
res = 0
total = 0
for x in range(1,w+1):
    total += (x*k)
if total > n:
    print(total-n)
else:
    print(0)