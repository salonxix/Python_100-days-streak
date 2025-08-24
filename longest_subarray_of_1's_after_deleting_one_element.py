def longestSubarray(nums):
    left = 0
    zeros = 0
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        while zeros > 1:  # shrink window if >1 zero
            if nums[left] == 0:
                zeros -= 1
            left += 1

        # Update max length of valid window
        max_len = max(max_len, right - left + 1)

    # Subtract 1 because one element must be deleted
    return max_len - 1


# Example runs
print(longestSubarray([1,1,0,1]))            # Output: 3
print(longestSubarray([0,1,1,1,0,1,1,0,1])) # Output: 5
print(longestSubarray([1,1,1]))             # Output: 2
