class Solution:
    def countMaxOrSubsets(self, nums):
        max_or = 0
        count = 0

        def backtrack(i, current_or):
            nonlocal max_or, count
            if i == len(nums):
                if current_or == max_or:
                    count += 1
                elif current_or > max_or:
                    max_or = current_or
                    count = 1
                return
            
            backtrack(i + 1, current_or | nums[i])
            backtrack(i + 1, current_or)

        backtrack(0, 0)
        return count

# --- Driver Code ---
if __name__ == "__main__":
    sol = Solution()

    nums1 = [3, 1]
    nums2 = [2, 2, 2]
    nums3 = [3, 2, 1, 5]

    print("Output for [3, 1]:", sol.countMaxOrSubsets(nums1))     # 2
    print("Output for [2, 2, 2]:", sol.countMaxOrSubsets(nums2))  # 7
    print("Output for [3, 2, 1, 5]:", sol.countMaxOrSubsets(nums3))  # 6
