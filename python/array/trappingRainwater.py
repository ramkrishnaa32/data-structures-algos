class Solution:
    """
    A class to solve the Trapping Rainwater problem using two different approaches:

    1. Prefix & Suffix Max Arrays (O(n) space, O(n) time)
    2. Two Pointer Technique (O(1) space, O(n) time)
    """

    def trappingRainwater(self, height: list[int]) -> int:
        """
        Calculate the total amount of trapped rainwater using
        prefix (left max) and suffix (right max) arrays.
        Args:
            height (list[int]): List of non-negative integers
                                representing the height of bars.
        Returns:
            int: Total units of trapped rainwater.
        """
        n = len(height)
        if n == 0:
            return 0

        # Arrays to store maximum height to the left and right of each index
        lmax = [0] * n
        rmax = [0] * n

        # Initialize boundary values
        lmax[0] = height[0]
        rmax[n - 1] = height[n - 1]

        # Fill lmax array (max height from left up to index i)
        for i in range(1, n):
            lmax[i] = max(lmax[i - 1], height[i])

        # Fill rmax array (max height from right up to index i)
        for i in range(n - 2, -1, -1):
            rmax[i] = max(rmax[i + 1], height[i])

        # Water trapped at each index = min(lmax[i], rmax[i]) - height[i]
        ans = 0
        for i in range(n):
            ans += min(lmax[i], rmax[i]) - height[i]

        return ans

    def trappingRainwaterTwoPointer(self, height: list[int]) -> int:
        """
        Calculate the total amount of trapped rainwater using
        the two-pointer approach.
        Args:
            height (list[int]): List of non-negative integers
                                representing the height of bars.
        Returns:
            int: Total units of trapped rainwater.
        """
        n = len(height)
        if n == 0:
            return 0

        ans = 0
        left, right = 0, n - 1
        lmax, rmax = 0, 0

        # Move two pointers inward while calculating trapped water
        while left < right:
            lmax = max(lmax, height[left])
            rmax = max(rmax, height[right])

            if lmax < rmax:
                ans += lmax - height[left]
                left += 1
            else:
                ans += rmax - height[right]
                right -= 1
        return ans


# Example usage
if __name__ == "__main__":
    s = Solution()
    height = [4, 2, 0, 3, 2, 5]

    result = s.trappingRainwater(height)
    print(f"Answer using Prefix/Suffix arrays: {result}")

    result = s.trappingRainwaterTwoPointer(height)
    print(f"Answer using Two Pointers: {result}")
