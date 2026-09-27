class Solution:
    def findMaximumPairs(self, students: str) -> int:
        # write your code here
        s = students
        res = 0
        l = 0
        while l < len(s) - 1:
            if s[l] == 'x' and s[l + 1] == 'y':
                res += 1
                l += 2
            elif s[l] == 'y' and s[l + 1] == 'x':
                res += 1
                l += 2
            else:
                l += 1
        return res