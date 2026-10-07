class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        s = sum(nums)
        p = 0
        res = []
        for x in range(len(nums) - 1,-1,-1):
            p += nums[x]
            res.append(s)
            s -= nums[x]
        return [x for x in reversed(res)]