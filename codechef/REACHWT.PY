# cook your dish here
t = int(input())
while t > 0:
    n = int(input())
    rem = n % 2
    c = ((n // 2) * 30) + (rem * 20)
    print(c)
    t -= 1