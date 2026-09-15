l = str(input())
r = str(input())
res = ''
for x in range(len(l)):
    if l[x] != r[x]:
        res += '1'
    else:
        res += '0'
print(res)