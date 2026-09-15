class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index,val in enumerate(nums):
            num2 = target - val
            if num2 in d.keys():
                return [d[num2],index]
            d[val] = index