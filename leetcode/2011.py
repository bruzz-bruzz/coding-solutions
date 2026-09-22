class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        z = 0
        for x in operations:
            if x == '--X' or x == 'X--':
                z -= 1
            else:
                z += 1
        return z