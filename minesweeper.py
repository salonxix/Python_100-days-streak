def updateBoard(board, click):
    m, n = len(board), len(board[0])
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    def countMines(r, c):
        return sum(0 <= r+dr < m and 0 <= c+dc < n and board[r+dr][c+dc] == 'M'
                   for dr, dc in directions)

    def dfs(r, c):
        if not (0 <= r < m and 0 <= c < n) or board[r][c] != 'E':
            return
        mines = countMines(r, c)
        if mines:
            board[r][c] = str(mines)
        else:
            board[r][c] = 'B'
            for dr, dc in directions:
                dfs(r+dr, c+dc)

    r, c = click
    if board[r][c] == 'M':
        board[r][c] = 'X'
    else:
        dfs(r, c)

    return board

# Example Usage:
board1 = [["E","E","E","E","E"],
          ["E","E","M","E","E"],
          ["E","E","E","E","E"],
          ["E","E","E","E","E"]]
click1 = [3, 0]
print(updateBoard(board1, click1))

board2 = [["B","1","E","1","B"],
          ["B","1","M","1","B"],
          ["B","1","1","1","B"],
          ["B","B","B","B","B"]]
click2 = [1, 2]
print(updateBoard(board2, click2))
