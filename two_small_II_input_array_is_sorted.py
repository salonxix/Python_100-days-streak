def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]  # Return 1-based indices
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []  # Should never hit due to guarantee of one solution


# ✅ Test Cases
if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))    # ➤ [1, 2]
    print(twoSum([2, 3, 4], 6))         # ➤ [1, 3]
    print(twoSum([-1, 0], -1))          # ➤ [1, 2]
