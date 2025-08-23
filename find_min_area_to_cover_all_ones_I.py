def minAreaRect(grid):
    rows, cols = len(grid), len(grid[0])
    
    min_row, max_row = rows, -1
    min_col, max_col = cols, -1
    
    # Find the bounds where 1's are present
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                min_row = min(min_row, r)
                max_row = max(max_row, r)
                min_col = min(min_col, c)
                max_col = max(max_col, c)
    
    # If no 1's present, area is 0
    if max_row == -1:
        return 0
    
    return (max_row - min_row + 1) * (max_col - min_col + 1)

# Example Test Cases
print(minAreaRect([[0,1,0],[1,0,1]]))  # Output: 6
print(minAreaRect([[1,0],[0,0]]))      # Output: 1
