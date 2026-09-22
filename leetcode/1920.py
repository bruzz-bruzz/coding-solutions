class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        for x in range(len(nums)):
            ans.append(nums[nums[x]])
        return ans