# cook your dish here
s = str(input()).split(" ")
p,r,c = int(s[0]),int(s[1]),int(s[2])
arr = [[p]]
for _ in range(r):
    prev = arr[len(arr) - 1]
    nextt = [0] * (len(prev) + 1)
    for x in range(len(prev)):
        over = max(0,(prev[x] - 1) / 2)
        nextt[x * 1] += over
        nextt[(x * 1) + 1] += over
    arr.append(nextt)
print(f"{min(1,arr[r][c]):.5f}")