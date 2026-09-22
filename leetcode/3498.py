class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for x in range(len(s)):
            o = 52 - (ord(s[x]) - 71)
            res += (o * (x + 1))
        return res
