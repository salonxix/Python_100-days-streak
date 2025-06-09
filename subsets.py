def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])  # Add a copy of the current subset
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()  # Backtrack

    backtrack(0, [])
    return result

# Test Case 1
nums1 = [1, 2, 3]
print("Input:", nums1)
print("Output:", subsets(nums1))

# Test Case 2
nums2 = [0]
print("\nInput:", nums2)
print("Output:", subsets(nums2))
