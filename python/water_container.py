class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        maxWater = 0
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            currentWater = w * h
            maxWater = max(maxWater, currentWater)
            print(f"sub-array:", height[left:right + 1])
            print(f"width: {w}, height: {h}, currentWater: {currentWater}, maxArea: {maxWater}")
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxWater


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
s = Solution()
result = s.maxArea(height)
print(f"result: {result}")
