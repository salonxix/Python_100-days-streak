def numTilings(n: int) -> int:
    """
    Find the number of ways to tile a 2 x n board with domino and tromino tiles.
    
    Args:
        n: Width of the 2 x n board
        
    Returns:
        Number of ways to tile the board modulo 10^9 + 7
    """
    MOD = 10**9 + 7
    
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # dp[i][0]: ways to fill first i columns completely
    # dp[i][1]: ways to fill first i columns with top cell of next column filled
    # dp[i][2]: ways to fill first i columns with bottom cell of next column filled
    dp = [[0] * 3 for _ in range(n + 1)]
    
    # Base cases
    dp[0][0] = 1
    dp[1][0] = 1
    
    for i in range(2, n + 1):
        # Complete fill: can come from complete fill + vertical domino or 2 horizontal dominoes
        # or from partial fills + completing tromino
        dp[i][0] = (dp[i-1][0] + dp[i-2][0] + dp[i-1][1] + dp[i-1][2]) % MOD
        
        # Partial fill top: can come from complete fill + tromino or partial bottom + horizontal
        dp[i][1] = (dp[i-2][0] + dp[i-1][2]) % MOD
        
        # Partial fill bottom: can come from complete fill + tromino or partial top + horizontal  
        dp[i][2] = (dp[i-2][0] + dp[i-1][1]) % MOD
    
    return dp[n][0]

# Test cases
def test_solution():
    # Example 1
    n1 = 3
    print(f"Input: n = {n1}")
    print(f"Output: {numTilings(n1)}")  # Expected: 5
    print()
    
    # Example 2
    n2 = 1
    print(f"Input: n = {n2}")
    print(f"Output: {numTilings(n2)}")  # Expected: 1
    print()

if __name__ == "__main__":
    test_solution()
