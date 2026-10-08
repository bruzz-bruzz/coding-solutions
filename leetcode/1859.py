class Solution:
    def sortSentence(self, s: str) -> str:
        d = {}
        for x in s.split(" "):
            d[x[len(x) - 1]] = x[:len(x) - 1]
        k = sorted(d.keys())
        res = []
        for x in k:
            res.append(d[x])
        return ' '.join(res)