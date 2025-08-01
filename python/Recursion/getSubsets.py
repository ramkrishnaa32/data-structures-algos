class Solution:
    def getSubsets(
            self,
            nums: list[int],  # Input list of integers
            current: list[int],  # The current subset being built
            i: int,  # Current index in nums
            allSubSets: list[list[int]]  # The final list of all subsets
    ):
        # Base case: we've considered all elements
        if i == len(nums):
            allSubSets.append(current.copy())  # Append a copy to avoid reference issues
            return

        # --- Include nums[i] in current subset ---
        current.append(nums[i])
        self.getSubsets(nums, current, i + 1, allSubSets)

        # --- Backtrack: remove the last added element ---
        current.pop()

        # --- Exclude nums[i] and move on ---
        self.getSubsets(nums, current, i + 1, allSubSets)



sol = Solution()
nums = [1, 2, 3]
allSubSets = []
sol.getSubsets(nums, [], 0, allSubSets)
print(allSubSets)