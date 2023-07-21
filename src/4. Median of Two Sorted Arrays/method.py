from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_array = sorted(nums1 + nums2)
        middle_number = int(len(sorted_array) / 2)

        if len(sorted_array) % 2 == 0:
            first_number = middle_number - 1
            last_number = middle_number
            return (sorted_array[first_number] + sorted_array[last_number]) / 2

        else:
            return sorted_array[middle_number]


assert (Solution().findMedianSortedArrays([1, 3], [2])) == 2
assert (Solution().findMedianSortedArrays([1, 2], [3, 4])) == 2.5
