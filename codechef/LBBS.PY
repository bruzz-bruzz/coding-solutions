# cook your dish here
s = str(input())
k = int(input())

res = 0
for x in range(len(s)):
    c0,c1 = 0,0
    for y in range(x,len(s)):
        if s[y] == '0':
            c0 += 1
        else:
            c1 += 1
        l = y - x + 1
        if l % 2 == 0:
            diff = abs(c0 - c1)
            if diff <= 2 * k:
                res = max(res,l)
print(res)