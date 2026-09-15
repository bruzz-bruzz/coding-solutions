class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for x in nums:
            d[x] = 1 + d.get(x,0)
        v = list(d.values())
        v.sort()
        v = v[len(v) - k:]
        res = []
        for x in d.keys():
            if d[x] in v:
                res.append(x)
        return res