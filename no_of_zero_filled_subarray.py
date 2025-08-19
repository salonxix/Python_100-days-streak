def zeroFilledSubarray(nums):
    count = 0      # Current streak of zeros
    total = 0      # Total zero-filled subarrays

    for num in nums:
        if num == 0:
            count += 1
            total += count
        else:
            count = 0  # Reset streak

    return total

# ---- Test Cases ----
nums1 = [1,3,0,0,2,0,0,4]
print(zeroFilledSubarray(nums1))  # Output: 6

nums2 = [0,0,0,2,0,0]
print(zeroFilledSubarray(nums2))  # Output: 9

nums3 = [2,10,2019]
print(zeroFilledSubarray(nums3))  # Output: 0
