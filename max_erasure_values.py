def maximumUniqueSubarray(nums):
    seen = set()
    left = 0
    curr_sum = 0
    max_sum = 0

    for right in range(len(nums)):
        while nums[right] in seen:
            seen.remove(nums[left])
            curr_sum -= nums[left]
            left += 1

        seen.add(nums[right])
        curr_sum += nums[right]
        max_sum = max(max_sum, curr_sum)

    return max_sum

# Test cases
print(maximumUniqueSubarray([4, 2, 4, 5, 6]))     # Output: 17
print(maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5])) # Output: 8
