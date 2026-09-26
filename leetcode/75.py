class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for x in range(n):
            for y in range(x+1,n):
                if nums[y] < nums[x]:
                    nums[x],nums[y] = nums[y],nums[x]
        return nums