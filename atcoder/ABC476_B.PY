n = int(input())
s = str(input())
t = str(input())
f = False
for x in range(len(s)):
    if t[x] != '*':
        if s[x] != t[x]:
            f = True
            break
if f:
    print("No")
else:
    print('Yes')