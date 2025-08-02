def islandPerimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter

# Test Cases
grid1 = [[0,1,0,0],
         [1,1,1,0],
         [0,1,0,0],
         [1,1,0,0]]
print("Output:", islandPerimeter(grid1))  # Output: 16

grid2 = [[1]]
print("Output:", islandPerimeter(grid2))  # Output: 4

grid3 = [[1,0]]
print("Output:", islandPerimeter(grid3))  # Output: 4
