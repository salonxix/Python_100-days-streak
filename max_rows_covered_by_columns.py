from itertools import combinations

def maximumRows(matrix, numSelect):
    m, n = len(matrix), len(matrix[0])
    max_rows = 0

    # Try every combination of numSelect columns
    for cols in combinations(range(n), numSelect):
        selected = set(cols)
        count = 0

        for row in matrix:
            # Check if all 1s in this row are in selected columns
            if all(j in selected for j, val in enumerate(row) if val == 1):
                count += 1

        max_rows = max(max_rows, count)

    return max_rows

# 🔍 Test Cases
matrix1 = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]]
numSelect1 = 2
print(maximumRows(matrix1, numSelect1))  # Output: 3

matrix2 = [[1],[0]]
numSelect2 = 1
print(maximumRows(matrix2, numSelect2))  # Output: 2
