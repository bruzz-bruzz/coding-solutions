s = str(input())
v = 'aeiouy'
r = len(s)  - 1
while r >= 0:
    if s[r].isalnum():
        if s[r].lower() in v:
            print("YES")
        else:
            print("NO")
        break
    r -= 1