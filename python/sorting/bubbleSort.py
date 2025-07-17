"""
Bubble Sort Algorithm

Overview:
    Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly steps through
    the list, compares adjacent elements, and swaps them if they are in the wrong order.
    This process continues until the list is sorted.

Algorithm Steps:
    1. Compare each pair of adjacent elements in the list.
    2. Swap them if they are in the wrong order.
    3. Repeat steps 1–2 for all elements, decreasing the number of elements compared each time.
    4. Stop when no swaps are needed (i.e., the list is sorted).

Time Complexity:
    - Worst-case: O(n^2)
    - Average-case: O(n^2)
    - Best-case: O(n) [when the array is already sorted]

Space Complexity:
    - O(1) (in-place sorting)
"""

class Solution:
    def bubbleSort(self, arr: list[int]) -> None:
        n = len(arr)
        while n > 1:
            isSwap = False
            for i in range(0, n - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    isSwap = True

            if isSwap:
                n = n - 1
                print(arr)
            else:
                break
        return arr

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(Solution().bubbleSort(nums))
sol = Solution()
result = sol.bubbleSort(nums)
print(f"Sorted Array: {result}")
