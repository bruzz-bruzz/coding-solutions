# cook your dish here
n = int(input())
arr = [int(x) for x in str(input()).split(" ")]
tmp = [1] + arr + [1]
dp = [[0] * (n + 2) for _ in range(n + 2)]
for x in range(2,n + 2):
    for y in range(n + 2 - x):
        z = y + x
        for k in range(y + 1, z):
            dp[y][z] = max(dp[y][z], dp[y][k] + dp[k][z] + tmp[y] * tmp[k] * tmp[z])
print(dp[0][n + 1])