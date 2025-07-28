class Solution:
    def countHillValley(self, nums):
        count = 0
        n = len(nums)
        
        for i in range(1, n - 1):
            left = i - 1
            while left >= 0 and nums[left] == nums[i]:
                left -= 1

            right = i + 1
            while right < n and nums[right] == nums[i]:
                right += 1

            if left >= 0 and right < n:
                if nums[i] > nums[left] and nums[i] > nums[right]:
                    count += 1
                elif nums[i] < nums[left] and nums[i] < nums[right]:
                    count += 1

        return count

# --- Driver code ---
if __name__ == "__main__":
    sol = Solution()

    nums1 = [2, 4, 1, 1, 6, 5]
    nums2 = [6, 6, 5, 5, 4, 1]

    print("Output for [2, 4, 1, 1, 6, 5]:", sol.countHillValley(nums1))  # Output: 3
    print("Output for [6, 6, 5, 5, 4, 1]:", sol.countHillValley(nums2))  # Output: 0
