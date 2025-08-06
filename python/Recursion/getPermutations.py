class Solution:
    def getPermutations(self, nums: list[int], index: int, ans: list[list[int]]):
        """
        Recursive helper function to generate all permutations of a list of integers using backtracking.

        Parameters:
        - nums (list[int]): The list of integers to permute.
        - index (int): The current index to fix and generate permutations for the rest.
        - ans (list[list[int]]): A list that accumulates all permutations.

        Logic:
        - If index reaches the end of the list, a complete permutation has been formed.
        - Swap the current index with every index from index to end to explore all branches.
        - Use backtracking to restore the original state after recursion.
        """
        if index == len(nums):
            ans.append(nums.copy())  # Append a copy to avoid referencing the same list
            return

        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]  # Swap to fix the element at index
            self.getPermutations(nums, index + 1, ans)   # Recurse for the next index
            nums[i], nums[index] = nums[index], nums[i]  # Backtrack to restore original state

    def permutations(self, nums: list[int]) -> list[list[int]]:
        """
        Generates all permutations of a given list of integers.

        Parameters:
        - nums (list[int]): The input list of integers.

        Returns:
        - list[list[int]]: A list containing all possible permutations.
        """
        ans = []
        self.getPermutations(nums, 0, ans)
        return ans

# Example usage
sol = Solution()
nums = [1, 2, 3]
result = sol.permutations(nums)
print(result)
