l,r = str(input()), str(input())
if l == ''.join(reversed(r)):
    print("YES")
else:
    print("NO")