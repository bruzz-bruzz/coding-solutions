n = int(input())
mishka,chris = 0,0
while n > 0:
    s = str(input()).split(' ')
    m,c = int(s[0]),int(s[1])
    if m > c:
        mishka += 1
    elif m < c:
        chris += 1
    n -= 1
if chris > mishka:
    print("Chris")
elif chris < mishka:
    print("Mishka")
else:
    print("Friendship is magic!^^")