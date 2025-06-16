def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    
    # Initialize a 2D DP table with (m+1)x(n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base Case: An empty target "" is a subsequence of any prefix of s
    for i in range(m + 1):
        dp[i][0] = 1

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[m][n]

# 🧪 Test Cases
print(numDistinct("rabbbit", "rabbit"))  # Output: 3
print(numDistinct("babgbag", "bag"))     # Output: 5
