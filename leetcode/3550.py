class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def summ(s):
            res = 0
            for x in str(s):
                res += int(x)
            return res
        for x in range(len(nums)):
            if summ(nums[x]) == x:
                return x
        return -1