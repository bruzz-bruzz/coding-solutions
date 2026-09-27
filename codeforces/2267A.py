for _ in range(int(input())):
    s = str(input()).split(" ")
    n,c = int(s[0]),str(s[1])
    s = str(input())
    l,r = 0, len(s) - 1
    res = 0
    while l < r:
        if s[l] != s[r]:
            if s[l] == c or s[r] == c:
                res += 1
            else:
                res += 2
        l += 1
        r -= 1
    print(res)