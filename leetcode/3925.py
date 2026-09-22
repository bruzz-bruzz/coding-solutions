class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        n2 = reversed(nums)
        nums += n2
        return nums