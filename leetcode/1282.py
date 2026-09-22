class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        import math
        d = defaultdict(list)
        for x in range(len(groupSizes)):
            d[groupSizes[x]].append(x)
        res = []
        k = list(d.keys())
        k.sort()
        res = []
        for x in k:
            t = math.ceil(len(d[x]) / x)
            for y in range(t):
                res.append(d[x][y * x:(y + 1) * x])
        return res