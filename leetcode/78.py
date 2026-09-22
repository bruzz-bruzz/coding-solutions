class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subs = [[]]
        for x in nums:
            subs += [y + [x] for y in subs]
        return subs