class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1,2,3]
        for x in range(3,n):
            dp.append(dp[x - 2] + dp[x - 1] )
        return dp[n - 1]