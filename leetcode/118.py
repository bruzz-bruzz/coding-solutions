class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]
        for x in range(1,numRows):
            tmp = [1]
            for y in range(len(res[len(res) - 1]) - 1):
                tmp.append(res[len(res) - 1][y] + res[len(res) - 1][y + 1])
            tmp.append(1)
            res.append(tmp)
        return res