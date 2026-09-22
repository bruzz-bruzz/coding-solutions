class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = sum(nums)
        t = s // k
        return s - (t * k)