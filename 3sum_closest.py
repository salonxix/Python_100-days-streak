def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')
    min_diff = float('inf')

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            current_diff = abs(current_sum - target)

            if current_diff < min_diff:
                min_diff = current_diff
                closest_sum = current_sum

            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum  # Exact match found

    return closest_sum


# Sample Input Section
if __name__ == "__main__":
    nums_input = input("Enter nums array (comma-separated, e.g., -1,2,1,-4): ").split(',')
    nums = [int(num.strip()) for num in nums_input if num.strip()]
    target = int(input("Enter target: "))
    result = threeSumClosest(nums, target)
    print("Closest Sum:", result)
