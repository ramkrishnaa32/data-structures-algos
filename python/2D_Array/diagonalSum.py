class Solution:
    def diagonalSum(self, nums: list[list[int]], rows: int):
        total = 0
        for i in range(rows):
            # Primary diagonal
            print("Primary:", nums[i][i])
            total += nums[i][i]

            # Secondary diagonal (avoid double-counting center)
            if i != rows - i - 1:
                print("Secondary:", nums[i][rows - i - 1])
                total += nums[i][rows - i - 1]

        print("Diagonal Sum:", total)

s = Solution()

arr = [[1,2,3],[4,5,6],[7,8,9]]
s.diagonalSum(arr, 3)
