# single_number.py

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


# 🔧 Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    print("Single Number in [2, 2, 1]:", sol.singleNumber([2, 2, 1]))  # Output: 1
    print("Single Number in [4, 1, 2, 1, 2]:", sol.singleNumber([4, 1, 2, 1, 2]))  # Output: 4
    print("Single Number in [1]:", sol.singleNumber([1]))  # Output: 1
