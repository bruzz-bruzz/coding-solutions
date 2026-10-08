class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = 0
        for z in str(x):
            s += int(z)
        if x % s == 0:
            return s
        return -1