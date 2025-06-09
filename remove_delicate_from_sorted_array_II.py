def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)

    i = 2  # pointer for position to insert next valid number

    for j in range(2, len(nums)):
        if nums[j] != nums[i - 2]:
            nums[i] = nums[j]
            i += 1

    return i

# Test Case 1
nums1 = [1, 1, 1, 2, 2, 3]
k1 = removeDuplicates(nums1)
print("Output:", k1)
print("Modified nums:", nums1[:k1])

# Test Case 2
nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
k2 = removeDuplicates(nums2)
print("Output:", k2)
print("Modified nums:", nums2[:k2])
