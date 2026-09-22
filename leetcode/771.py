class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for x in stones:
            if x in jewels:
                res += 1
        return res