# cook your dish here
n = int(input())
s = str(input()).split(" ")
target = str(input())
c = []
for x in range(len(s)):
    if s[x] == target:
        c.append(x)
if len(c) == 0:
    print(-1)
elif len(c) == 1:
    print(-2)
else:
    print(c.pop(1))