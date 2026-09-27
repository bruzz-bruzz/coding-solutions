# cook your dish here
for _ in range(int(input())):
    s = str(input()).split(" ")
    n,k = int(s[0]),int(s[1])
    c = 1
    while c < n:
        c += 1
        if c % k == 0:
            n += 1
    print(c)