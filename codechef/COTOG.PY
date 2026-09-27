# cook your dish here
n = int(input())
s = [int(x) for x in str(input()).split(" ")]
positions = {}
for idx,val in enumerate(s):
    positions[val] = idx
res = 0
for x in range(0, 2 * n, 2):
    first = s[x]
    couple = first ^ 1
    if s[x + 1] != couple:
        res += 1
        coupleIdx = positions[couple]
        curr = s[x + 1]
        s[x + 1],s[coupleIdx] = s[coupleIdx],s[x + 1]
        positions[curr] = coupleIdx
        positions[couple] = x + 1
print(res)