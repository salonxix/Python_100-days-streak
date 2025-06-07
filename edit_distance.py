def min_distance(word1, word2):
    m, n = len(word1), len(word2)
    # Create a 2D DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i  # Deleting all characters
    for j in range(n + 1):
        dp[0][j] = j  # Inserting all characters

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # Delete
                    dp[i][j - 1],    # Insert
                    dp[i - 1][j - 1] # Replace
                )

    return dp[m][n]

# Example usage
print(min_distance("horse", "ros"))         # Output: 3
print(min_distance("intention", "execution")) # Output: 5
