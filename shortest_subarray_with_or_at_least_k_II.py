def shortestSubarrayWithORAtLeastK(nums, k):
    n = len(nums)
    min_len = float('inf')

    for i in range(n):
        curr_or = 0
        for j in range(i, n):
            curr_or |= nums[j]
            if curr_or >= k:
                min_len = min(min_len, j - i + 1)
                break  # Early stop if condition met

    return -1 if min_len == float('inf') else min_len

# Test cases
print("Example 1 Output:", shortestSubarrayWithORAtLeastK([1, 2, 3], 2))   # Output: 1
print("Example 2 Output:", shortestSubarrayWithORAtLeastK([2, 1, 8], 10))  # Output: 3
print("Example 3 Output:", shortestSubarrayWithORAtLeastK([1, 2], 0))      # Output: 1
