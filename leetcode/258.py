class Solution:
    def addDigits(self, num: int) -> int:
        def summ(s):
            c = 0
            for x in s:
                c += int(x)
            return str(c)
        num = str(num)
        while len(num) > 1:
            num = summ(num)
        return int(num)