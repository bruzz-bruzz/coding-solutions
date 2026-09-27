# cook your dish here
s = str(input()).split(" ")
n,k = int(s[0]),int(s[1])
s = str(input()).split(" ")
for x in range(len(s)):
    s[x] = int(s[x])
c = 0
for x in range(len(s)):
    if x <= k:
        c += min(s[x],s[k])
    else:
        c += min(s[x],s[k] - 1)
print(c)