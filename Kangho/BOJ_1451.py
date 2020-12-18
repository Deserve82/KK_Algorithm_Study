# import random
from itertools import combinations

r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(map(int, list(input()))))
rows = [i for i in range(1, r)]
cols = [i for i in range(1, c)]
cross_comb = []
for i in range(1, r):
    for j in range(1, c):
        cross_comb.append((i, j))
row_comb = list(combinations(rows, 2))
col_comb = list(combinations(cols, 2))
answers = []


def cal_upper_cross(rp, cp):
    if rp == 3 and cp == 4:
        pass
    sq1 = 0
    for i in range(rp):
        for j in range(cp):
            sq1 += board[i][j]
    sq2 = 0
    for i in range(rp):
        for j in range(cp, c):
            sq2 += board[i][j]
    sq3 = 0
    for i in range(rp, r):
        for j in range(c):
            sq3 += board[i][j]
    answers.append(sq1 * sq2 * sq3)
    return


def cal_lower_cross(rp, cp):
    sq1 = 0

    for i in range(rp):
        for j in range(c):
            sq1 += board[i][j]
    sq2 = 0
    for i in range(rp, r):
        for j in range(cp):
            sq2 += board[i][j]

    sq3 = 0
    for i in range(rp, r):
        for j in range(cp, c):
            sq3 += board[i][j]

    answers.append(sq1 * sq2 * sq3)
    return


def cal_right_cross(rp, cp):
    sq1 = 0
    for i in range(r):
        for j in range(cp):
            sq1 += board[i][j]
    sq2 = 0
    for i in range(rp):
        for j in range(cp, c):
            sq2 += board[i][j]
    sq3 = 0
    for i in range(rp, r):
        for j in range(cp, c):
            sq3 += board[i][j]
    answers.append(sq1 * sq2 * sq3)
    return


def cal_left_cross(rp, cp):
    sq1 = 0
    for i in range(rp):
        for j in range(cp):
            sq1 += board[i][j]
    sq2 = 0
    for i in range(rp, r):
        for j in range(cp):
            sq2 += board[i][j]

    sq3 = 0
    for i in range(r):
        for j in range(cp, c):
            sq3 += board[i][j]
    answers.append(sq1 * sq2 * sq3)
    return


def cal_row(row1, row2):
    sq1 = 0
    for i in range(row1):
        for j in range(c):
            sq1 += board[i][j]

    sq2 = 0
    for i in range(row1, row2):
        for j in range(c):
            sq2 += board[i][j]

    sq3 = 0
    for i in range(row2, r):
        for j in range(c):
            sq3 += board[i][j]
    answers.append(sq1 * sq2 * sq3)
    return


def cal_col(col1, col2):
    sq1 = 0
    for i in range(r):
        for j in range(col1):
            sq1 += board[i][j]

    sq2 = 0
    for i in range(r):
        for j in range(col1, col2):
            sq2 += board[i][j]

    sq3 = 0
    for i in range(r):
        for j in range(col2, c):
            sq3 += board[i][j]

    answers.append(sq1 * sq2 * sq3)
    return


for rc in row_comb:
    cal_row(rc[0], rc[1])
for cc in col_comb:
    cal_col(cc[0], cc[1])
for crc in cross_comb:
    cal_lower_cross(crc[0], crc[1])
    cal_upper_cross(crc[0], crc[1])
    cal_left_cross(crc[0], crc[1])
    cal_right_cross(crc[0], crc[1])
print(max(answers))

# n, m = map(int, input().split())
# print(n, m)
# for i in range(n):
#     start = ''
#     for j in range(m):
#         start += str(random.randrange(0,10))
#     print(start)
