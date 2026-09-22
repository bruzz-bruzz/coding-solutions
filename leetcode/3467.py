class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for x in range(len(nums)):
            if nums[x] % 2 == 0:    
                nums[x] = 0
            else:
                nums[x] = 1
        nums.sort()
        return nums