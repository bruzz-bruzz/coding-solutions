n = int(input())
d = {
    1:'I hate',
    0:'I love'
}
res = ''
for x in range(1,n):
    res += d[x % 2] + ' that '
res += d[n % 2] + ' it'
print(res)