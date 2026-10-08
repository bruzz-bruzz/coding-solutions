class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        l,r = 0,0
        s = set()
        c = 0
        while l < len(mat) and r < len(mat[0]):
            s.add(tuple([l,r]))
            l += 1
            r += 1
        l,r = 0, len(mat[0]) - 1
        while l < len(mat) and r >= 0:
            s.add(tuple([l,r]))
            l += 1
            r -= 1
        for x in s:
            c += mat[x[0]][x[1]]
        return c