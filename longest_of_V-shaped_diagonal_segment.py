from functools import lru_cache

class Solution:
    def longestVSegment(self, grid):
        n, m = len(grid), len(grid[0])
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # 4 diagonals

        # expected sequence for index -> value
        def expected(idx):
            if idx == 0: return 1
            return 2 if idx % 2 == 1 else 0

        @lru_cache(None)
        def dfs(i, j, d, idx, turned):
            if not (0 <= i < n and 0 <= j < m): 
                return 0
            if grid[i][j] != expected(idx): 
                return 0

            best = 1
            di, dj = directions[d]
            best = max(best, 1 + dfs(i+di, j+dj, d, idx+1, turned))  # continue straight

            # Try one clockwise turn if not yet turned
            if not turned:
                new_d = (d+1) % 4
                di2, dj2 = directions[new_d]
                best = max(best, 1 + dfs(i+di2, j+dj2, new_d, idx+1, True))
            return best

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:  # Start must be '1'
                    for d in range(4):
                        ans = max(ans, dfs(i, j, d, 0, False))
        return ans


# -------------------------
# Example Runs
# -------------------------
solution = Solution()
print(solution.longestVSegment([[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]))  # 5
print(solution.longestVSegment([[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]))  # 4
print(solution.longestVSegment([[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]))  # 5
print(solution.longestVSegment([[1]]))  # 1
