# cook your dish here
n = int(input())
import math
quad = (1 + math.isqrt(1 + (8*n))) // 2
if quad * (quad - 1) // 2 > n:
    quad -= 1
difference = n - (quad * (quad - 1) // 2)
print(quad + difference)