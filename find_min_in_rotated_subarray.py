# find_min_rotated_sorted.py

class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

# 🧪 Test Cases
if __name__ == "__main__":
    sol = Solution()
    print("Output 1:", sol.findMin([3, 4, 5, 1, 2]))       # Output: 1
    print("Output 2:", sol.findMin([4, 5, 6, 7, 0, 1, 2])) # Output: 0
    print("Output 3:", sol.findMin([11, 13, 15, 17]))      # Output: 11
