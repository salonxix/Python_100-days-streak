# max_product_subarray.py

class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0

        max_product = nums[0]
        max_so_far = nums[0]
        min_so_far = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                max_so_far, min_so_far = min_so_far, max_so_far

            max_so_far = max(num, max_so_far * num)
            min_so_far = min(num, min_so_far * num)

            max_product = max(max_product, max_so_far)

        return max_product

# 🧪 Test Cases
if __name__ == "__main__":
    sol = Solution()
    print("Output 1:", sol.maxProduct([2, 3, -2, 4]))       # Output: 6
    print("Output 2:", sol.maxProduct([-2, 0, -1]))         # Output: 0
    print("Output 3:", sol.maxProduct([-2, 3, -4]))         # Output: 24
