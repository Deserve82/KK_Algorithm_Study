import sys
board = []


def checker():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True


def hori(x, val):
    if val in board[x]:
        return False
    return True


def vert(y, val):
    for i in range(9):
        if val == board[i][y]:
            return False
    return True


def bythree(x, y, val):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[nx + i][ny + j] == val:
                return False
    return True


def sudoku(row):
    if checker():
        for b in board:
            print(" ".join(map(str, b)))
        print("")
        sys.exit()

    for i in range(row, 9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if hori(i, num) and vert(j, num) and bythree(i, j, num):
                        board[i][j] = num
                        sudoku(i)
                        board[i][j] = 0
                return
    return


if __name__ == '__main__':
    for _ in range(9):
        board.append(list(map(int, input().split())))
    sudoku(0)
