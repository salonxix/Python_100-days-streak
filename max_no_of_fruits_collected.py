from functools import lru_cache

def maxFruitsDungeon(fruits):
    n = len(fruits)

    @lru_cache(None)
    def dfs(r1, c1, r2, c2, r3, c3):
        # Check bounds
        if not (0 <= r1 < n and 0 <= c1 < n and
                0 <= r2 < n and 0 <= c2 < n and
                0 <= r3 < n and 0 <= c3 < n):
            return float('-inf')

        # Base case: all at bottom-right
        if (r1, c1) == (n-1, n-1) and (r2, c2) == (n-1, n-1) and (r3, c3) == (n-1, n-1):
            return fruits[n-1][n-1]

        # Collect fruits without double counting
        collected = fruits[r1][c1]
        if (r2, c2) != (r1, c1):
            collected += fruits[r2][c2]
        if (r3, c3) != (r1, c1) and (r3, c3) != (r2, c2):
            collected += fruits[r3][c3]

        max_next = float('-inf')
        movesA = [(1,0),(0,1),(1,1)]
        movesB = [(1,0),(1,-1),(1,1)]
        movesC = [(-1,1),(0,1),(1,1)]

        for dr1, dc1 in movesA:
            for dr2, dc2 in movesB:
                for dr3, dc3 in movesC:
                    max_next = max(max_next,
                                   dfs(r1+dr1, c1+dc1,
                                       r2+dr2, c2+dc2,
                                       r3+dr3, c3+dc3))

        return collected + max_next

    return dfs(0, 0, 0, n-1, n-1, 0)


# Example Runs
print(maxFruitsDungeon([[1,2,3,4],
                        [5,6,8,7],
                        [9,10,11,12],
                        [13,14,15,16]]))  # Output: 100

print(maxFruitsDungeon([[1,1],[1,1]]))  # Output: 4
