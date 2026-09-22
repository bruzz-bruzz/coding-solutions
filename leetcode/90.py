class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        subs = [[]]
        for x in nums:
            subs += [y + [x] for y in subs]
        res = []
        for x in subs:
            x.sort()
            if x not in res:
                res.append(x)
        return res