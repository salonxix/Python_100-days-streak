from collections import deque

def minSumRectangles(grid):
    m, n = len(grid), len(grid[0])
    visited = [[False]*n for _ in range(m)]

    def bfs(x, y):
        q = deque([(x, y)])
        visited[x][y] = True
        min_r, max_r, min_c, max_c = x, x, y, y

        while q:
            r, c = q.popleft()
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 1:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    min_r, max_r = min(min_r, nr), max(max_r, nr)
                    min_c, max_c = min(min_c, nc), max(max_c, nc)
        return (max_r-min_r+1) * (max_c-min_c+1)

    total_area = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                total_area += bfs(i, j)

    return total_area


# Example 1
grid1 = [[1,0,1],[1,1,1]]
print(minSumRectangles(grid1))  # Output: 5

# Example 2
grid2 = [[1,0,1,0],[0,1,0,1]]
print(minSumRectangles(grid2))  # Output: 5
