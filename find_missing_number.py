def find_missing(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)

print(find_missing([0, 1, 2, 4]))  # Output: 3
