def shortestSubarrayWithORAtLeastK(nums, k):
    n = len(nums)
    min_len = float('inf')

    for i in range(n):
        current_or = 0
        for j in range(i, n):
            current_or |= nums[j]
            if current_or >= k:
                min_len = min(min_len, j - i + 1)
                break  # No need to continue if already >= k

    return min_len if min_len != float('inf') else -1

# Test Cases
print("Example 1:", shortestSubarrayWithORAtLeastK([1, 2, 3], 2))     # Output: 1
print("Example 2:", shortestSubarrayWithORAtLeastK([2, 1, 8], 10))    # Output: 3
print("Example 3:", shortestSubarrayWithORAtLeastK([1, 2], 0))        # Output: 1
