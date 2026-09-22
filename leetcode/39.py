class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def recur(arr,s,nums):
            if s == target:
                arr.sort()
                if arr not in res:
                    res.append(arr)
            elif s < target:
                for x in nums:
                    tmp = arr[:]
                    recur(tmp + [x],s + x,nums)
        for x in candidates:
            recur([x],x,candidates)
        return res