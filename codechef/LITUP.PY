# cook your dish here
for _ in range(int(input())):
    s = str(input()).split(" ")
    n,k = int(s[0]),int(s[1])
    ar = [int(x) for x in str(input()).split(" ")]
    pos = []
    c = float('inf')
    for x in range(n):
        for y in range(x+1,n):
            a,b = x + 1,y + 1
            if (a - k <= 1) and (b + k >= n) and ((b - a) <=  2 * k + 1):
                c = min(c, ar[x] + ar[y])
    if c == float('inf'):
        print(-1)
    else:
        print(c)