def numTrees(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = 1  # Empty tree
    dp[1] = 1  # Single node

    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]

    return dp[n]

# --------- Main Program ---------
if __name__ == "__main__":
    n = int(input("Enter number of nodes (n): "))
    result = numTrees(n)
    print(f"Number of structurally unique BSTs for n = {n} is: {result}")
