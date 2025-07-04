def checkMove(board, rMove, cMove, color):
    ROWS, COLS = 8, 8
    directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    opp = 'W' if color == 'B' else 'B'

    for dr, dc in directions:
        r, c = rMove + dr, cMove + dc
        found_opposite = False

        while 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == '.':
                break
            if board[r][c] == opp:
                found_opposite = True
            elif board[r][c] == color:
                if found_opposite:
                    return True
                break
            else:
                break
            r += dr
            c += dc
    return False

# Test case
board = [
    [".",".",".","B",".",".",".","."],
    [".",".",".","W",".",".",".","."],
    [".",".",".","W",".",".",".","."],
    [".",".",".","W",".",".",".","."],
    ["W","B","B",".","W","W","W","B"],
    [".",".",".","B",".",".",".","."],
    [".",".",".","B",".",".",".","."],
    [".",".",".","W",".",".",".","."]
]
print(checkMove(board, 4, 3, "B"))  # Output: True
