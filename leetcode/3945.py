class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        d = {}
        for x in str(n):
            d[x] = 1 + d.get(x,0)
        res = 0
        for x in d.keys():
            res += int(x) * int(d[x])
        return res
