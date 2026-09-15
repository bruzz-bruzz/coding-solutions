l = int(input())
t = str(input())
left,right = 0,0
isLucky = True
for x in t[:len(t) // 2]:
    if x != '4' and x != '7':
        isLucky = False
    left += int(x)
for x in t[len(t) // 2:]:
    if x != '4' and x != '7':
        isLucky = False
    right += int(x)
if not isLucky:
    print("NO")
elif left != right:
    print("NO")
else:
    print("YES")