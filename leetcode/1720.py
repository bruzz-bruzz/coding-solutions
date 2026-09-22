class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        res = [first]
        for x in range(len(encoded) - 1):
            res.append(res[len(res) - 1] ^ encoded[x])
        res.append(res[len(res) - 1] ^ encoded.pop())
        return res