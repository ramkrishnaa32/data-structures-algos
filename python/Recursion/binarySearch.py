class Solution:
    def binarySearch(self, nums: list[int], target: int) -> None:
        """
        Performs binary search to find the target in a sorted list.
        Parameters:
        nums (list[int]): A sorted list of integers.
        target (int): The integer to search for.
        Returns:
        None: Prints the result to stdout.

        Example:
        binarySearch([-1, 0, 3, 4, 5, 9, 12], 5)
        Target: 5, present at index 4
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                print(f"Target: {target}, present at index {mid}")
                return

            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        print(f"Target: {target}, is not present")


    def binarySearchRecursion(self, nums: list[int], target: int, left: int, right: int) -> bool:
        """
        Recursively performs binary search on a sorted list to find the target.
        Parameters:
        nums (list[int]): A sorted list of integers.
        target (int): The integer to search for.
        left (int): Left boundary of the current search range.
        right (int): Right boundary of the current search range.
        Returns:
        bool: True if target is found, False otherwise.
        """
        if left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                return self.binarySearchRecursion(nums, target, mid + 1, right)
            else:
                return self.binarySearchRecursion(nums, target, left, mid - 1)

        return False

    def search(self, nums: list[int], target: int) -> bool:
        """
        Wrapper function to initiate recursive binary search.
        Parameters:
        nums (list[int]): Sorted list of integers.
        target (int): Integer to search for.
        Returns:
        bool: Result of the search.
        """
        return self.binarySearchRecursion(nums, target, 0, len(nums) - 1)

s = Solution()
nums = [-1, 0, 3, 4, 5, 9, 12]
target = 6
s.binarySearch(nums, target)

result = s.search(nums, target)
if result:
    print(f"Target: {target}, present at index {result}")
else:
    print(f"Target: {target}, is not present")


