class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        s = set()
        n,m = len(matrix), len(matrix[0])
        for x in range(n):
            for y in range(m):
                if tuple([x,y]) not in s and tuple([y,x]) not in s:
                    [matrix[x][y],matrix[y][x]] = [matrix[y][x],matrix[x][y]]
                    s.add(tuple([x,y]))
                    s.add(tuple([y,x]))
        for x in range(n):
            matrix[x] = matrix[x][::-1]
        return matrix