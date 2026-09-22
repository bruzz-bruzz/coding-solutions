class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for x in range(len(s) - 1):
            res += abs(ord(s[x]) - ord(s[x + 1]))
        return res