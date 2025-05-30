def threeSum(nums):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n):
        # Skip duplicates for i
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Move both pointers and skip duplicates
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


# Sample Input Section
if __name__ == "__main__":
    nums_input = input("Enter nums array (comma-separated, e.g., -1,0,1,2,-1,-4): ").split(',')
    nums = [int(num.strip()) for num in nums_input if num.strip()]
    result = threeSum(nums)
    print("Triplets that sum to 0:", result)
