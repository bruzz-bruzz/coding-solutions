class Solution:
    def mirrorDistance(self, n: int) -> int:
        n2 = int(str(n)[::-1])
        return abs(n - n2)