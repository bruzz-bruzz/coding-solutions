class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        def fact(n):
            res = 1
            for x in range(1,n+1):
                res *= x
            return res
        def comb(n,r):
            return int((fact(n)) / ((fact(n-r)) * fact(r)))
        d = {}
        for x in nums:
            d[x] = 1 + d.get(x,0)
        res = 0
        for x in d.keys():
            if d[x] >= 2:
                res += comb(d[x],2)
        return res