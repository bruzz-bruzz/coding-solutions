# cook your dish here
s = str(input()).split(" ")
x,a,y,b,d = int(s[0]),int(s[1]),int(s[2]),int(s[3]),int(s[4])
if (x * a) + (y * b) >= d:
    print("YES")
else:
    print("NO")