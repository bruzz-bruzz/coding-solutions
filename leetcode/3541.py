class Solution:
    def maxFreqSum(self, s: str) -> int:
        v,c = {},{}
        for x in s:
            if x.lower() in 'aeiou':
                v[x.lower()] = 1 + v.get(x.lower(),0)
            else:
                c[x.lower()] = 1 + c.get(x.lower(),0)
        m1,m2 = max(v.values()) if v.values() else 0, max(c.values()) if c.values() else 0
        return m1 + m2