
#
class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        actualSum = 0
        n = len(grid)
        ans = []
        numList = []
        for arr in grid:
            for num in arr:
                actualSum += num
                if num in numList:
                    ans.append(num)
                else:
                    numList.append(num)

        expectedSum = ((n * n) * ((n * n) + 1)) // 2
        missingNum = expectedSum + ans[0] - actualSum
        ans.append(missingNum)
        return ans


grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
s = Solution()
result = s.findMissingAndRepeatedValues(grid)
print(f"Result: {result}")