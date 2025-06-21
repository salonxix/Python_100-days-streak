# single_number_ii.py

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for i in range(32):
            bit_sum = 0
            for num in nums:
                # Mask for bit i
                if (num >> i) & 1:
                    bit_sum += 1
            if bit_sum % 3:
                result |= (1 << i)

        # Handle negative numbers
        if result >= 2**31:
            result -= 2**32

        return result


# 🔧 Test Cases
if __name__ == "__main__":
    sol = Solution()
    print("Single Number in [2, 2, 3, 2]:", sol.singleNumber([2, 2, 3, 2]))  # Output: 3
    print("Single Number in [0, 1, 0, 1, 0, 1, 99]:", sol.singleNumber([0, 1, 0, 1, 0, 1, 99]))  # Output: 99
