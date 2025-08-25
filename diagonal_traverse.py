def findDiagonalOrder(mat):
    if not mat or not mat[0]:
        return []
    
    m, n = len(mat), len(mat[0])
    result = []
    row, col, direction = 0, 0, 1  # start at top-left, going up-right

    for _ in range(m * n):
        result.append(mat[row][col])
        
        # Move according to direction
        if direction == 1:  # up-right
            if col == n - 1:   # hit right border
                row += 1
                direction = -1
            elif row == 0:     # hit top border
                col += 1
                direction = -1
            else:              # normal move
                row -= 1
                col += 1
        else:  # down-left
            if row == m - 1:   # hit bottom border
                col += 1
                direction = 1
            elif col == 0:     # hit left border
                row += 1
                direction = 1
            else:              # normal move
                row += 1
                col -= 1

    return result


# Example runs
print(findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))  # [1,2,4,7,5,3,6,8,9]
print(findDiagonalOrder([[1,2],[3,4]]))              # [1,2,3,4]
