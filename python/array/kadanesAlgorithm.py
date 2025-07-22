def find_max_subarray(nums):
    """
    Finds the contiguous subarray within a list of integers that has the largest sum.
    Parameters:
        nums (List[int]): A list of integers (can be positive, negative, or zero).
    Returns:
        Tuple[List[int], int]: A tuple containing:
            - The subarray with the maximum sum.
            - The maximum subarray sum.
    Example:
        find_max_subarray([3, -4, 5, 4, -1, 7, -8])
        ([5, 4, -1, 7], 15)
    """

    maxSum = float("-inf")
    currSum = 0
    subArr = []
    finalArray = []

    for num in nums:
        currSum += num
        subArr.append(num)

        if currSum > maxSum:
            maxSum = currSum
            finalArray = subArr.copy()

        if currSum < 0:
            currSum = 0
            subArr = []

    return finalArray, maxSum

nums = [3, -4, 5, 4, -1, 7, -8]
subarray, max_sum = find_max_subarray(nums)
print(f"finalSubArray: {subarray}, maxSum: {max_sum}")

