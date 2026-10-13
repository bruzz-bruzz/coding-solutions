class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = 0
        for x in range(len(nums)):
            if len(nums) % (x + 1) == 0:
                res += (nums[x] ** 2)
        return res