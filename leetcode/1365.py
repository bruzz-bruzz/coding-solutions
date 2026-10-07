class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        res = []
        n = len(nums)
        for x in range(n):
            c = 0
            for y in range(n):
                if nums[y] < nums[x]:
                    c += 1
            res.append(c)
        return res