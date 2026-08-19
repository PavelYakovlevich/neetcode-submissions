class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = []
        combined.extend(nums1)
        combined.extend(nums2)
        combined.sort()

        m = (len(combined) - 1) // 2

        if len(combined) % 2 != 0:
            return combined[m]

        return (combined[m] + combined[m + 1]) / 2
