class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Edge cases
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0
        
        dp = [0.0] * (n + 1)
        dp[0] = 1.0  # Start at 0 with probability 1
        windowSum = 1.0
        result = 0.0

        for i in range(1, n + 1):
            dp[i] = windowSum / maxPts  # Probability of reaching i

            if i < k:
                windowSum += dp[i]   # Still can draw, add dp[i]
            else:
                result += dp[i]      # Reached >= k, stop game

            if i - maxPts >= 0:
                windowSum -= dp[i - maxPts]  # Slide window

        return result
