class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        import math
        o,e = 0,0
        for x in range(1,n * 2 + 1):
            if x % 2 == 0:
                e += x
            else:
                o += x
        return math.gcd(o,e)