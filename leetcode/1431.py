class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        m = max(candies)
        res = []
        for x in candies:
            if x + extraCandies >= m:
                res.append(True)
            else:
                res.append(False)
        return res