from collections import defaultdict

def max_partitions(nums, k):
    total = sum(nums)
    n = len(nums)
    prefix = 0
    res = 0
    count = defaultdict(int)
    for i in range(n - 1):
        prefix += nums[i]
        count[prefix - (total - prefix)] += 1
    res = count[0]

    prefix = 0
    prefix_map = defaultdict(int)
    suffix_map = defaultdict(int)
    for i in range(n - 1):
        prefix += nums[i]
        suffix_map[prefix - (total - prefix)] += 1

    prefix = 0
    for i in range(n):
        diff = k - nums[i]
        if i > 0:
            prefix += nums[i - 1]
            prefix_map[prefix - (total - prefix)] += 1
            suffix_map[prefix - (total - prefix)] -= 1

        res = max(res, prefix_map[-diff] + suffix_map[diff])

    return res

# Example 1
nums1 = [2, -1, 2]
k1 = 3
print("Output Example 1:", max_partitions(nums1, k1))  # Expected: 1

# Example 2
nums2 = [0, 0, 0]
k2 = 1
print("Output Example 2:", max_partitions(nums2, k2))  # Expected: 2

# Example 3
nums3 = [22, 4, -25, -20, -15, 15, -16, 7, 19, -10, 0, -13, -14]
k3 = -33
print("Output Example 3:", max_partitions(nums3, k3))  # Expected: 4
