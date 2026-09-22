class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        for x in nums:
            d[x] = 1 + d.get(x,0)
        res = []
        for x in d.keys():
            if d[x] >= 2:
                res.append(x)
        return res