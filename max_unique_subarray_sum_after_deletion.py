class Solution:
    def maximumUniqueSubarray(self, nums):
        seen = set()
        left = 0
        max_sum = 0
        current_sum = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            seen.add(nums[right])
            current_sum += nums[right]
            max_sum = max(max_sum, current_sum)

        return max_sum


# --- Driver code ---
if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, 1, 0, 1, 1]
    nums3 = [1, 2, -1, -2, 1, 0, -1]

    print("Output for [1, 2, 3, 4, 5]:", sol.maximumUniqueSubarray(nums1))      # 15
    print("Output for [1, 1, 0, 1, 1]:", sol.maximumUniqueSubarray(nums2))      # 1
    print("Output for [1, 2, -1, -2, 1, 0, -1]:", sol.maximumUniqueSubarray(nums3))  # 3
