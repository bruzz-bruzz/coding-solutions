n = int(input())
vols = str(input()).split(' ')
s = 0
for x in vols:
    s += int(x)
print(round(s / n,12))