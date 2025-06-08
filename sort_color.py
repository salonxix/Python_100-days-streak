def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# 🧪 Test Case 1
nums1 = [2, 0, 2, 1, 1, 0]
sortColors(nums1)
print("Sorted Colors:", nums1)  # Output: [0, 0, 1, 1, 2, 2]

# 🧪 Test Case 2
nums2 = [2, 0, 1]
sortColors(nums2)
print("Sorted Colors:", nums2)  # Output: [0, 1, 2]
