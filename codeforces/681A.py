n = int(input())
res = 'NO'
while n > 0:
    s = str(input()).split(' ')
    before,after = int(s[1]), int(s[2])
    if before >= 2400:
        if after > before:
            res = 'YES'
    n -= 1
print(res)