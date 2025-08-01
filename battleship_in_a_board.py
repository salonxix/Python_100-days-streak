# Day 72: Battleships in a Board

from typing import List

def countBattleships(board: List[List[str]]) -> int:
    if not board or not board[0]:
        return 0

    m, n = len(board), len(board[0])
    count = 0

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'X':
                if i > 0 and board[i-1][j] == 'X':
                    continue
                if j > 0 and board[i][j-1] == 'X':
                    continue
                count += 1
    return count

# -------- Terminal Input and Execution --------

if __name__ == "__main__":
    print("Enter board row by row using '.' and 'X'. Type 'end' to finish input:")
    board = []
    while True:
        line = input().strip()
        if line.lower() == 'end':
            break
        board.append(list(line))

    result = countBattleships(board)
    print("Number of battleships on board:", result)
