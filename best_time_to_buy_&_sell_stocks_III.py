from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0

        for price in prices:
            buy1 = max(buy1, -price)          # Buy first stock
            sell1 = max(sell1, buy1 + price)  # Sell first stock
            buy2 = max(buy2, sell1 - price)   # Buy second stock
            sell2 = max(sell2, buy2 + price)  # Sell second stock

        return sell2

if __name__ == "__main__":
    sol = Solution()

    prices1 = [3,3,5,0,0,3,1,4]
    print("Example 1 Output:", sol.maxProfit(prices1))  # Output: 6

    prices2 = [1,2,3,4,5]
    print("Example 2 Output:", sol.maxProfit(prices2))  # Output: 4

    prices3 = [7,6,4,3,1]
    print("Example 3 Output:", sol.maxProfit(prices3))  # Output: 0
