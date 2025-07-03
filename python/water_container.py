# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    left = 0
    right = len(height) - 1
    maxWater = 0
    while left < right:
        w = right - left
        h = min(height[left], height[right])
        currentWater = w * h
        maxWater = max(maxWater, currentWater)
        print(f"left: {left}, right: {right}")
        print(f"w: {w}, h: {h}, currentWater: {currentWater}, maxWater: {maxWater}")
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxWater

nums = [8, 7, 2, 1]
result = maxArea(nums)
print(f"maxWater: {result}")
