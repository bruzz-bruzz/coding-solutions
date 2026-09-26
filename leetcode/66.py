class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        r = len(digits) - 1
        digits[r] += 1
        while r > 0:
            c = digits[r]
            if c >= 10:
                if r == 0:
                    digits.insert(0,1)
                else:
                    digits[r-1] += 1
                digits[r] -= 10
            r -= 1
        if digits[0] >= 10:
            digits[0] -= 10
            digits.insert(0,1)
        return digits