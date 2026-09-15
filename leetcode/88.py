class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        c = 0
        while nums2:
            nums1[m + c] = nums2.pop(0)
            c += 1
        for x in range(len(nums1)):
            for y in range(x+1,len(nums1)):
                if nums1[x] > nums1[y]:
                    [nums1[x],nums1[y]] = [nums1[y],nums1[x]]