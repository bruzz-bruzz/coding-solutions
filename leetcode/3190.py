class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            div = x // 3
            lb,ub = abs((div * 3) - x), abs(((div + 1) * 3) - x)
            res += min(lb,ub)
        return res