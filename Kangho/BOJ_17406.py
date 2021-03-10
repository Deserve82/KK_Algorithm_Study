from copy import deepcopy
from collections import deque
from itertools import permutations


def rotate(start_row, start_col, length):
    for l in range(length, 1, -2):
        d = deque()
        for i in range(l):
            d.append(board[start_row][start_col + i])
        for i in range(1, l - 1):
            d.append(board[start_row + i][start_col+l-1])
        for i in range(l - 1, -1, -1):
            d.append(board[start_row+l-1][start_col + i])
        for i in range(l - 2, 0, -1):
            d.append(board[start_row + i][start_col])
        d.rotate(1)
        d_idx = 0
        for i in range(l):
            board[start_row][start_col + i] = d[d_idx]
            d_idx += 1
        for i in range(1, l - 1):
            board[start_row + i][start_col+l-1] = d[d_idx]
            d_idx += 1
        for i in range(l - 1, -1, -1):
            board[start_row+l-1][start_col + i] = d[d_idx]
            d_idx += 1
        for i in range(l - 2, 0, -1):
            board[start_row + i][start_col] = d[d_idx]
            d_idx += 1
        start_row += 1
        start_col += 1


def get_min_row():
    global answer
    for i in range(R):
        tmp_val = 0
        for j in range(C):
            tmp_val += board[i][j]
        answer = min(answer, tmp_val)


answer = 9999999
R, C, K = map(int, input().split())
board = []
commands = []
for _ in range(R):
    board.append(list(map(int, input().split())))

for _ in range(K):
    z, x, y = map(int, input().split())
    commands.append((z, x, y))
permus = list(permutations(commands))
ori_board = deepcopy(board)
for commands in permus:
    for command in commands:
        r, c, s = command
        rotate(r - s - 1, c - s - 1, 2 * s + 1)
    get_min_row()
    board = deepcopy(ori_board)

print(answer)
