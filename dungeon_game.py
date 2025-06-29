def calculateMinimumHP(dungeon):
    if not dungeon or not dungeon[0]:
        return 0

    m, n = len(dungeon), len(dungeon[0])
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
    dp[m][n - 1] = dp[m - 1][n] = 1  # Princess's cell base case

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            min_health_needed = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
            dp[i][j] = max(1, min_health_needed)

    return dp[0][0]

# Example usage:
dungeon1 = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
dungeon2 = [[0]]

print("Output 1:", calculateMinimumHP(dungeon1))  # ➤ 7
print("Output 2:", calculateMinimumHP(dungeon2))  # ➤ 1
