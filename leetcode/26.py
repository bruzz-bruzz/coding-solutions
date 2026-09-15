class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = list(set(nums))
        for x in range(len(s)):
            nums[x] = s[x]
        for x in range(len(nums) - len(s)):
            nums.pop()
        nums.sort()
        return len(nums)