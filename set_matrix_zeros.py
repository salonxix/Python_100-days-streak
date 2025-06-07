def set_zeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    row_zero = False

    # Step 1: Mark zeros in the first row/col
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                if i > 0:
                    matrix[i][0] = 0
                else:
                    row_zero = True

    # Step 2: Use marks to set 0s (excluding first row and col)
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Step 3: Zero out first column if needed
    if matrix[0][0] == 0:
        for i in range(rows):
            matrix[i][0] = 0

    # Step 4: Zero out first row if needed
    if row_zero:
        for j in range(cols):
            matrix[0][j] = 0


# Utility function to print matrix
def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

# 🚀 Test Case 1
matrix1 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
print("Before (Test Case 1):")
print_matrix(matrix1)
set_zeroes(matrix1)
print("After (Test Case 1):")
print_matrix(matrix1)

# 🚀 Test Case 2
matrix2 = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]
print("Before (Test Case 2):")
print_matrix(matrix2)
set_zeroes(matrix2)
print("After (Test Case 2):")
print_matrix(matrix2)
