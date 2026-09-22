class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l,r = [],[]
        for x in range(len(nums)):
            s = nums[:x]
            s2 = nums[x+1:]
            l.append(sum(s) if s else 0)
            r.append(sum(s2) if s2 else 0)
        res = []
        for x in range(len(l)):
            res.append(abs(l[x] - r[x]))
        return res