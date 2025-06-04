def rotate(matrix):
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

# --- MAIN PROGRAM ---

# Take input from the user
n = int(input("Enter size of matrix (n x n): "))
print(f"Enter the matrix row by row, each row with {n} space-separated integers:")

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

rotate(matrix)

print("\nRotated Matrix:")
for row in matrix:
    print(row)
