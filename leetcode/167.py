class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i,val in enumerate(numbers):
            n = target - val
            if n in d.keys():
                return [d[n] + 1, i + 1]
            d[val] = i