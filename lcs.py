# longest_consecutive.py

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:  # Only start from beginning of a sequence
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)

        return longest


# 🔧 Test the function in VS Code
if __name__ == "__main__":
    sol = Solution()

    nums1 = [100, 4, 200, 1, 3, 2]
    print("Example 1 Output:", sol.longestConsecutive(nums1))  # Output: 4

    nums2 = [0,3,7,2,5,8,4,6,0,1]
    print("Example 2 Output:", sol.longestConsecutive(nums2))  # Output: 9

    nums3 = [1,0,1,2]
    print("Example 3 Output:", sol.longestConsecutive(nums3))  # Output: 3
