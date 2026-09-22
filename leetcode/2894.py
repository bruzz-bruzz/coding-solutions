class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        a,b = 0,0
        for x in range(1,n+1):
            if x % m == 0:
                b += x
            else:
                a += x
        return a - b