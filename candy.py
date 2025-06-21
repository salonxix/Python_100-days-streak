# candy_distribution.py

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # Left to right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right to left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


# 🔧 Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    print("Minimum candies for [1,0,2]:", sol.candy([1, 0, 2]))  # Output: 5
    print("Minimum candies for [1,2,2]:", sol.candy([1, 2, 2]))  # Output: 4
