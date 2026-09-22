class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        s = list(s)
        l,r = 0, k - 1
        while l < r:
            s[l],s[r] = s[r],s[l]
            l += 1
            r -= 1
        return ''.join(s)