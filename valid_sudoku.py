from typing import List

def is_valid_sudoku(board: List[List[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]  # Each box is a 3x3 grid

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == ".":
                continue

            if num in rows[i]:
                return False
            rows[i].add(num)

            if num in cols[j]:
                return False
            cols[j].add(num)

            box_index = (i // 3) * 3 + (j // 3)
            if num in boxes[box_index]:
                return False
            boxes[box_index].add(num)

    return True

# Example usage
if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    if is_valid_sudoku(board):
        print("The Sudoku board is valid.")
    else:
        print("The Sudoku board is invalid.")
