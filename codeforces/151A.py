s = str(input()).split(' ')
arr = [(int(s[1]) * int(s[2])) // int(s[6]),int(s[3]) * int(s[4]),int(s[5]) // int(s[7])]
if min(arr) > int(s[0]):
    print(min(arr) // int(s[0]))
elif min(arr) < int(s[0]):
    print(0)
else:
    print(min(arr))