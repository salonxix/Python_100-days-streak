def minimizeMax(nums, p):
    nums.sort()

    def can_form_pairs(max_diff):
        count = 0
        i = 1
        while i < len(nums):
            if nums[i] - nums[i - 1] <= max_diff:
                count += 1
                i += 2  # skip the next index to make pairs disjoint
            else:
                i += 1
        return count >= p

    low, high = 0, nums[-1] - nums[0]
    while low < high:
        mid = (low + high) // 2
        if can_form_pairs(mid):
            high = mid
        else:
            low = mid + 1
    return low

# 🔍 Example usage:
nums1 = [10, 1, 2, 7, 1, 3]
p1 = 2
print("Output:", minimizeMax(nums1, p1))  # ➤ 1

nums2 = [4, 2, 1, 2]
p2 = 1
print("Output:", minimizeMax(nums2, p2))  # ➤ 0
