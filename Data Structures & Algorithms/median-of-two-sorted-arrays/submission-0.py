class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # also die aufgabe ist es aus zwei arrays den gemiensamen median zu finden
        # die erste Idee wäre es einfach deie zwei arrays zu mergen
        merged = nums1 + nums2
        merged.sort()
        total = len(merged)
        if total %2 == 0:
            return (merged[total // 2 - 1] + merged[total // 2]) / 2.0
        else:
            return merged[total//2]