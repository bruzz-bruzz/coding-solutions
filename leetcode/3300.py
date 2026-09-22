class Solution:
    def minElement(self, nums: List[int]) -> int:
        def s(n):
            n = str(n)
            res = 0
            for x in n:
                res += int(x)
            return res
        for x in range(len(nums)):
            nums[x] = s(nums[x])
        return min(nums)