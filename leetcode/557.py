class Solution:
    def reverseWords(self, s: str) -> str:
        def rev(st):
            st = list(st)
            l,r = 0, len(st) - 1
            while l < r:
                st[l],st[r] = st[r],st[l]
                l += 1
                r -= 1
            return ''.join(st)
        s = s.split(" ")
        res = []
        for x in s:
            res.append(rev(x))
        return ' '.join(res)