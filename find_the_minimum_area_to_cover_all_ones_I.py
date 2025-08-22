class Solution:
    def minimumArea(self, grid):
        rows, cols = len(grid), len(grid[0])
        
        minRow, maxRow = rows, -1
        minCol, maxCol = cols, -1
        
        # Find boundaries of rectangle
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    minRow = min(minRow, r)
                    maxRow = max(maxRow, r)
                    minCol = min(minCol, c)
                    maxCol = max(maxCol, c)
        
        # Area = (height * width)
        return (maxRow - minRow + 1) * (maxCol - minCol + 1)
