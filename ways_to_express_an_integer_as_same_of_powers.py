MOD = 10**9 + 7

def numOfWays(n, x):
    powers = []
    base = 1
    while base**x <= n:
        powers.append(base**x)
        base += 1
    
    from functools import lru_cache

    @lru_cache(None)
    def dfs(i, target):
        if target == 0:
            return 1
        if target < 0 or i >= len(powers):
            return 0
        # Option 1: include powers[i]
        include = dfs(i + 1, target - powers[i])
        # Option 2: skip powers[i]
        skip = dfs(i + 1, target)
        return (include + skip) % MOD

    return dfs(0, n)

# Example usage
print(numOfWays(10, 2))  # Output: 1
print(numOfWays(4, 1))   # Output: 2
