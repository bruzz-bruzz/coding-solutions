class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r,c = [],[]
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == 0:
                    c.append(y)
                    r.append(x)
        for x in c:
            for y in range(len(matrix)):
                matrix[y][x] = 0
        for x in r:
            for y in range(len(matrix[0])):
                matrix[x][y] = 0