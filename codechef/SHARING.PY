# cook your dish here
s = str(input()).split(" ")
a,b = int(s[0]),int(s[1])
if a > b:
    if ((a-b ) / 2)% 2 == 0:
        print((a - b) // 2)
    else:
        print(-1)
else:
    print(-1)