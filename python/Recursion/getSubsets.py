class Solution:
    def getSubsets(self, nums: list[int], current: list[int], i: int, allSubSets: list[list[int]]):
        if i == len(nums):
            allSubSets.append(current.copy())
            return

            # Include nums[i]
        current.append(nums[i])
        self.getSubsets(nums, current, i + 1, allSubSets)

        # Exclude nums[i]
        current.pop()
        self.getSubsets(nums, current, i + 1, allSubSets)

    def getAllUniqueSubsets(self, nums: list[int], current: list[int], i: int, allSubSets: list[list[int]]):
        if i == len(nums):
            allSubSets.append(current.copy())
            return

            # Include nums[i]
        current.append(nums[i])
        self.getAllUniqueSubsets(nums, current, i + 1, allSubSets)

        # Backtrack
        current.pop()

        # Skip duplicates
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

        # Exclude nums[i]
        self.getAllUniqueSubsets(nums, current, i + 1, allSubSets)


sol = Solution()

# Test normal subsets
nums = [1, 2, 3]
allSubSets = []
sol.getSubsets(nums, [], 0, allSubSets)
print("All Subsets:", allSubSets)

# Test unique subsets with duplicates
nums2 = [1, 2, 2]
nums2.sort()  # Sorting is important for deduplication
uniqueSubSets = []
sol.getAllUniqueSubsets(nums2, [], 0, uniqueSubSets)
print("Unique Subsets:", uniqueSubSets)
