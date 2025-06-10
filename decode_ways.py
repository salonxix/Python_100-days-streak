def numDecodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # empty string base case
    dp[1] = 1  # first char is guaranteed non-zero here

    for i in range(2, n + 1):
        # Check single digit decode (s[i-1])
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]

        # Check two digit decode (s[i-2:i])
        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

    return dp[n]

# Example test cases:
print(numDecodings("12"))    # Output: 2
print(numDecodings("226"))   # Output: 3
print(numDecodings("06"))    # Output: 0
