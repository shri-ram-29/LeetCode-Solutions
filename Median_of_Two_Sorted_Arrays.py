class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            mid1 = (left + right) // 2
            mid2 = (m + n + 1) // 2 - mid1

            if mid1 > 0 and nums1[mid1 - 1] > nums2[mid2]:
                right = mid1 - 1
            elif mid1 < m and nums2[mid2 - 1] > nums1[mid1]:
                left = mid1 + 1
            else:
                if mid1 == 0:
                    max_of_left = nums2[mid2 - 1]
                elif mid2 == 0:
                    max_of_left = nums1[mid1 - 1]
                else:
                    max_of_left = max(nums1[mid1 - 1], nums2[mid2 - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if mid1 == m:
                    min_of_right = nums2[mid2]
                elif mid2 == n:
                    min_of_right = nums1[mid1]
                else:
                    min_of_right = min(nums1[mid1], nums2[mid2])

                return (max_of_left + min_of_right) / 2
