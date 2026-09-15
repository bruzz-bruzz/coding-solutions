t = int(input())
d = {
    0:"a",
    1:"b",
    2:"c"
}
while t > 0:
    s = str(input())
    c = 0
    for x in range(len(s)):
        if s[x] != d[x]:
            c += 1
    if c > 2:
        print("No")
    else:
        print("yes")
    t -= 1