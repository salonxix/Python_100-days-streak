from collections import defaultdict

def sortDiagonals(grid):
    n = len(grid)
    diagonals = defaultdict(list)

    # Step 1: Collect elements from each diagonal
    for i in range(n):
        for j in range(n):
            diagonals[i - j].append(grid[i][j])

    # Step 2: Sort diagonals
    for key in diagonals:
        if key >= 0:  # top-right diagonals
            diagonals[key].sort()  # ascending
        else:  # bottom-left diagonals
            diagonals[key].sort(reverse=True)  # descending

    # Step 3: Put sorted values back
    for i in range(n):
        for j in range(n):
            grid[i][j] = diagonals[i - j].pop(0)

    return grid


# 🔹 Example runs
print(sortDiagonals([[1,7,3],[9,8,2],[4,5,6]]))  
# Output: [[8,2,3],[9,6,7],[4,5,1]]

print(sortDiagonals([[0,1],[1,2]]))  
# Output: [[2,1],[1,0]]

print(sortDiagonals([[1]]))  
# Output: [[1]]
