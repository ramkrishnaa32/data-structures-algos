# Subarray sum equals to K

nums = [9, 4, 20, 3, 10, 5]
target = 33

# Bruteforce approach
def subArraySum(nums, target):
    count = 0
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            print(f"sub-array: {nums[i:j + 1]}, total: {total}")
            if total == target:
                count += 1
    return count


result = subArraySum(nums, target)
print(result)

# Optional solution using a prefix sum
def subArraySum1(nums, target):
    prefix_sums = {0: 1}  # Prefix sum of 0 occurs once by default
    total = 0
    count = 0
    for num in nums:
        total += num
        diff = total - target
        print(f"total: {total}, diff: {diff}")

        count += prefix_sums.get(diff, 0)
        prefix_sums[total] = prefix_sums.get(total, 0) + 1

    print(count)


subArraySum1(nums, target)







