def jump(nums):
    n = len(nums)
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest

    return jumps

# Example 1
nums1 = [2, 3, 1, 1, 4]
print("Output:", jump(nums1))  # Output: 2

# Example 2
nums2 = [2, 3, 0, 1, 4]
print("Output:", jump(nums2))  # Output: 2
