# Day 72: Pacific Atlantic Water Flow

from typing import List
import sys
sys.setrecursionlimit(10000)

def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    if not heights:
        return []

    m, n = len(heights), len(heights[0])
    pacific = [[False]*n for _ in range(m)]
    atlantic = [[False]*n for _ in range(m)]

    def dfs(r, c, visited, prev_height):
        if (r < 0 or r >= m or c < 0 or c >= n or 
            visited[r][c] or heights[r][c] < prev_height):
            return
        visited[r][c] = True
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            dfs(r+dr, c+dc, visited, heights[r][c])

    # Pacific ocean DFS from top and left borders
    for i in range(m):
        dfs(i, 0, pacific, heights[i][0])
        dfs(i, n-1, atlantic, heights[i][n-1])
    for j in range(n):
        dfs(0, j, pacific, heights[0][j])
        dfs(m-1, j, atlantic, heights[m-1][j])

    result = []
    for i in range(m):
        for j in range(n):
            if pacific[i][j] and atlantic[i][j]:
                result.append([i, j])
    return result

# -------- Terminal Input and Execution --------

if __name__ == "__main__":
    print("Enter matrix row by row. Type 'end' to finish input:")
    heights = []
    while True:
        line = input()
        if line.strip().lower() == 'end':
            break
        row = list(map(int, line.strip().split()))
        heights.append(row)

    result = pacificAtlantic(heights)
    print("Cells that can reach both oceans:")
    for cell in result:
        print(cell)
