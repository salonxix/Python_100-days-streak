class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(r, c, ch):
            # check row & column
            for i in range(9):
                if board[r][i] == ch or board[i][c] == ch:
                    return False
            # check 3x3 box
            box_row, box_col = 3 * (r // 3), 3 * (c // 3)
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if board[i][j] == ch:
                        return False
            return True

        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for ch in "123456789":
                            if is_valid(i, j, ch):
                                board[i][j] = ch
                                if backtrack():
                                    return True
                                board[i][j] = "."
                        return False
            return True

        backtrack()
