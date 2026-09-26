class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        n = len(nums)
        def recur(arr,nums,n):
            if len(arr) == n:
                if arr not in res:
                    res.append(arr)
            elif len(arr) < n:
                tmp = arr[:]
                for x in nums:
                    if x not in tmp:
                        recur(tmp + [x],nums,n)
        for x in nums:
            recur([x],nums,n)
        return res