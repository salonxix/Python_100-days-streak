from itertools import permutations
import math

class Solution:
    def judgePoint24(self, cards):
        def dfs(nums):
            # Base case: if only one number remains
            if len(nums) == 1:
                return math.isclose(nums[0], 24, rel_tol=1e-5)

            # Try every pair of numbers
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        # Remaining numbers after removing nums[i] and nums[j]
                        next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]

                        # All possible operations between nums[i] and nums[j]
                        for op in self.compute(nums[i], nums[j]):
                            if dfs(next_nums + [op]):
                                return True
            return False

        return dfs(cards)

    def compute(self, a, b):
        """Return all possible results of applying +, -, *, / on a and b"""
        results = [a + b, a - b, b - a, a * b]
        if b != 0:
            results.append(a / b)
        if a != 0:
            results.append(b / a)
        return results


# Example Usage
sol = Solution()
print(sol.judgePoint24([4, 1, 8, 7]))  # True (since (8-4)*(7-1) = 24)
print(sol.judgePoint24([1, 2, 1, 2]))  # False
