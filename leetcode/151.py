class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split(" ")
        res = []
        for x in s[::-1]:
            if x:
                res.append(x.strip())
        return ' '.join(res)