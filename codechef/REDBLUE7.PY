# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = str(input()).split(" ")
    for x in range(len(s)):
        s[x] = int(s[x])
    s.sort()
    res = 0
    red,blue = 0,len(s)
    sr,sb = 0,sum(s)
    for x in range(len(s) - 1):
        p = s[x]
        red += 1
        blue -= 1
        sb -= p
        sr += p
        calc = (sr * blue) + (sb * red)
        res = max(res,calc)
    print(res)