class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        def xor(arr):
            pref = arr[0]
            for x in arr[1:]:
                pref |= x
            return pref
        subs = [[]]
        d = defaultdict(list)
        for x in nums:
            subs += [y + [x] for y in subs]
        for x in subs:
            if x:
                d[xor(x)].append(x)
        m = max(d.keys())
        return len(d[m])