class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        res = 0
        for x in accounts:
            res = max(res,sum(x))
        return res