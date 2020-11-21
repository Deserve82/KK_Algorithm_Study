def lcs(board, row, col, h, X, Y, Z):
    for i in range(row + 1):
        board[i][0][0] = 0
    for j in range(col + 1):
        board[0][j][0] = 0
    for k in range(h + 1):
        board[0][0][k] = 0

    for k in range(1, h + 1):
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if X[i - 1] == Y[j - 1] == Z[k - 1]:
                    board[i][j][k] = board[i - 1][j - 1][k - 1] + 1
                else:
                    board[i][j][k] = max(board[i - 1][j][k], board[i][j - 1][k], board[i][j][k-1])
    return board[row][col][h]


a = input()
b = input()
c = input()
td_board = [[[0]*(len(c)+1) for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
print(lcs(td_board, len(a), len(b), len(c), a, b, c))
