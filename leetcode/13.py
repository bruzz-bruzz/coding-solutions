class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I':1,
            'IV':4,
            'V':5,
            'IX':9,
            'X':10,
            'XL':40,
            'L':50,
            'XC':90,
            'C':100,
            'CD':400,
            'D':500,
            'CM':900,
            'M':1000
        }
        s = list(s)
        res = 0
        c = ''
        while s:
            p = s.pop(0)
            if c + p not in d.keys():
                res += d[c]
                c = p
            else:
                c += p
        if c in d.keys():
            res += d[c]
        return res