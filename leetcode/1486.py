class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = []
        for x in range(n):
            arr.append(start + (2 * x))
        res = arr[0]
        for x in arr[1:]:
            res ^= x
        return res