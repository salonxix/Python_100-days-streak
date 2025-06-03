def firstMissingPositive(nums):
    n = len(nums)

    for i in range(n):
        # Place nums[i] at the correct index if it's in the range [1, n]
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            correct_index = nums[i] - 1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]

    # After rearranging, the first place where the index doesn't match the value
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # If all positions are correct, then the missing number is n + 1
    return n + 1


# ----------- Example usage -------------
if __name__ == "__main__":
    test_cases = [
        [1, 2, 0],            # Output: 3
        [3, 4, -1, 1],        # Output: 2
        [7, 8, 9, 11, 12],    # Output: 1
        [1, 2, 3, 4, 5],      # Output: 6
        [0, -10, 1, 3],       # Output: 2
    ]

    for nums in test_cases:
        print(f"Input: {nums} → First Missing Positive: {firstMissingPositive(nums.copy())}")
