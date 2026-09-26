class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res = [[1]]
        for x in range(1,rowIndex + 1):
            tmp = [1]
            for y in range(len(res[len(res) - 1]) - 1):
                tmp.append(res[len(res) - 1][y] + res[len(res) - 1][y + 1])
            tmp.append(1)
            res.append(tmp)
        return res[rowIndex]