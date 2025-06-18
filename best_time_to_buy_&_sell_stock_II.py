from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

if __name__ == "__main__":
    sol = Solution()

    prices1 = [7,1,5,3,6,4]
    print("Example 1 Output:", sol.maxProfit(prices1))  # Output: 7

    prices2 = [1,2,3,4,5]
    print("Example 2 Output:", sol.maxProfit(prices2))  # Output: 4

    prices3 = [7,6,4,3,1]
    print("Example 3 Output:", sol.maxProfit(prices3))  # Output: 0
