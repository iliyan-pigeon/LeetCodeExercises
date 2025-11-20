from typing import List


class Solution(object):
    def merge(self, nums1, m, nums2, n):

        p1 = m - 1
        p2 = n - 1

        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1


a = Solution()
print(a.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))


# Solution 2
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m + i] = nums2[i]

        nums1.sort()


# Solution 3
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):

        index = len(nums1)-1

        while m and n:
            if nums1[m-1] >= nums2[n-1]:
                nums1[index] = nums1[m-1]
                m -= 1
            else:
                nums1[index] = nums2[n-1]
                n -= 1
            index -= 1

        while m:
            nums1[index] = nums1[m - 1]
            m -= 1
            index -= 1

        while n:
            nums1[index] = nums2[n - 1]
            n -= 1
            index -= 1

        return nums1
