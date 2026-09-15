class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        neg = x[0] == '-'
        if neg:
            x = x[1:]
        x = int(x[::-1])
        res = x
        if neg:
            res = x - (x * 2)
        if x < (-2 ** 31) or x >(2 ** 31) - 1:
            return 0
        return res