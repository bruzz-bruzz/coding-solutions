s = list(str(input()))
res = ''
d = {
    '.':'0',
    '-.':'1',
    '--':'2'
}
prev = s.pop(0)
while s:
    cur = s.pop(0)
    if prev in d.keys():
        res += d[prev]
        prev = cur
    else:
        prev += cur
if prev:
    res += d[prev]
print(res)