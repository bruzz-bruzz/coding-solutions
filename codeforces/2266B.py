for _ in range(int(input())):
    s = str(input()).split(" ")
    a,b,c = int(s[0]),int(s[1]),int(s[2])
    res = max(abs(a-b), abs((a + c) - b))
    print(res)