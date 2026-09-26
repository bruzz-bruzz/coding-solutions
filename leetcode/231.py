class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for x in range(-31,32):
            if 2 ** x == n:
                return True
            elif 2 ** x > n:
                return False