class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def xor(arr):
            if arr:
                pref = arr[0]
                for x in arr[1:]:
                    pref ^= x
                return pref
        subs = [[]]
        res = 0
        for x in nums:
            subs += [y + [x] for y in subs]
        for x in subs:
            res += xor(x)
        return res