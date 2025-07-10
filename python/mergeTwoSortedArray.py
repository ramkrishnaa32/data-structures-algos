class Solution:
    def mergeTwoSortedArray(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        lenght = len(nums1) - 1
        for i in range(n - 1, -1, -1):
            if nums1[m - 1] < nums2[i]:
                nums1[lenght] = nums2[i]
                lenght -= 1
            else:
                nums1[lenght] = nums1[m - 1]
                nums1[m - 1] = nums2[i]

            print(nums1)

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        index = m + n - 1
        i = m - 1
        j = n - 1

        while (i >= 0 and j >= 0):
            if nums1[i] >= nums2[j]:
                nums1[index] = nums1[i]
                index -= 1
                i -= 1
            else:
                nums1[index] = nums2[j]
                index -= 1
                j -= 1

        while (j >= 0):
            nums1[index] = nums2[j]
            index -= 1
            j -= 1

        print(nums1)


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

s = Solution()
# s.mergeTwoSortedArray(nums1, m, nums2, n)
s.merge(nums1, m, nums2, n)