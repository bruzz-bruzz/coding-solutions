class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        d = {}
        res = []
        for x in range(len(s)):
            sl = s[x:10 + x]
            if len(sl) < 10:
                break
            d[sl] = 1 + d.get(sl,0)
        for x in d.keys():
            if d[x] > 1:
                res.append(x)
        return res