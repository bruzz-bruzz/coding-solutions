for _ in range(int(input())):
    s = str(input()).split(" ")
    n,k = int(s[0]),int(s[1])
    if k == n - 1:
        print("No")
    else:
        print("Yes")