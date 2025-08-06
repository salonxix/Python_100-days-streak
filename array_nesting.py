class Solution:
    def arrayNesting(self, nums):
        n = len(nums)
        visited = [False] * n
        max_len = 0

        for i in range(n):
            if not visited[i]:
                start = nums[i]
                count = 0
                while not visited[start]:
                    visited[start] = True
                    start = nums[start]
                    count += 1
                max_len = max(max_len, count)

        return max_len

# Example usage
nums = [5, 4, 0, 3, 1, 6, 2]
sol = Solution()
print(sol.arrayNesting(nums))
