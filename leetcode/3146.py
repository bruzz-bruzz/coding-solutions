class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        a,b = {},{}
        res = 0
        for x in range(len(s)):
            a[s[x]] = x
        for x in range(len(t)):
            b[t[x]] = x
        for x in b.keys():
            res += abs(b[x] - a[x])
        return res