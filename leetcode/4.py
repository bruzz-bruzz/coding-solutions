class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        if len(nums1) % 2 == 0:
            m = len(nums1) // 2
            summ = (nums1[m - 1] + nums1[m]) / 2
            return summ
        m = len(nums1) // 2
        return nums1[m]