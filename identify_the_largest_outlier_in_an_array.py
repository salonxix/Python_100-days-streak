# outlier_finder.py

def find_largest_outlier(nums):
    total = sum(nums)
    n = len(nums)
    outliers = []

    for i in range(n):
        for j in range(i + 1, n):
            remaining_sum = total - nums[i] - nums[j]
            if remaining_sum == nums[i]:
                outliers.append(nums[j])
            elif remaining_sum == nums[j]:
                outliers.append(nums[i])
    
    return max(outliers) if outliers else -1

# 🚀 Sample Test Cases
if __name__ == "__main__":
    test_cases = [
        ([2, 3, 5, 10], 10),
        ([-2, -1, -3, -6, 4], 4),
        ([1, 1, 1, 1, 1, 5, 5], 5),
        ([1, 2, 3, 6, 99], 99),        # Edge case: obvious outlier
        ([4, 5, 9], 9),                # Edge case: only one possible
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = find_largest_outlier(nums)
        print(f"Test Case {i+1}: Input: {nums}")
        print(f"Expected: {expected}, Got: {result}")
        print("✅ Pass" if result == expected else "❌ Fail", end="\n\n")
