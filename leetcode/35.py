class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        import math
        l,r = 0,len(nums) - 1
        res = 0
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            res = (l + r) / 2
        return math.ceil(res)