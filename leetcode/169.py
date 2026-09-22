class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        d = {}
        for idx,num in enumerate(numbers):
            comp = target - num
            if comp in d.keys():
                return [d[comp] + 1,idx + 1]
            d[num] = idx