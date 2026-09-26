class Solution:
    def mySqrt(self, x: int) -> int:
        c = 1
        while True:
            if c * c >= x:
                break
            c += 1
        if c * c == x:
            return c
        return c - 1