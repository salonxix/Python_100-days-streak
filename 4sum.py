from typing import List

def four_sum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 3):
        # Skip duplicate elements for i
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            # Skip duplicate elements for j
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left, right = j + 1, n - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result

# Example usage:
if __name__ == "__main__":
    nums1 = [1,0,-1,0,-2,2]
    target1 = 0
    print(four_sum(nums1, target1))  # Expected: [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]

    nums2 = [2,2,2,2,2]
    target2 = 8
    print(four_sum(nums2, target2))  # Expected: [[2,2,2,2]]
