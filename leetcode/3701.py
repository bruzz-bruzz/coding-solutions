class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        res = 0
        for x in range(len(nums)):
            if x % 2 == 0:
                res += nums[x]
            elif x % 2 != 0:
                res -= nums[x]
        return res