class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        d = {}
        for x in range(len(matrix)):
            d[x] = 0
            for y in range(len(matrix[x])):
                if matrix[x][y] == 1:
                    d[x] = 1 + d.get(x,0)
        return list(d.values())