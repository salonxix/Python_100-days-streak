# find_min_rotated_duplicates.py

class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1  # Skip the duplicate

        return nums[left]

# 🧪 Test Cases
if __name__ == "__main__":
    sol = Solution()
    print("Output 1:", sol.findMin([1, 3, 5]))          # Output: 1
    print("Output 2:", sol.findMin([2, 2, 2, 0, 1]))     # Output: 0
    print("Output 3:", sol.findMin([10, 1, 10, 10, 10])) # Output: 1
