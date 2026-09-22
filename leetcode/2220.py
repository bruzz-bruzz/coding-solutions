class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a,b = bin(start)[2:],bin(goal)[2:]
        c = 0
        while len(a) < len(b):
            a = '0' + a
        while len(b) < len(a):
            b = '0' + b
        for x in range(len(a)):
            if a[x] != b[x]:
                c += 1
        return c
