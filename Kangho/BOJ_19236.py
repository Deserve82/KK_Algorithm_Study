import sys
from copy import deepcopy
sys.setrecursionlimit(10000)

def teenager_shark_durududdu():
    global answer, how_much_shark_ate, board, fishes
    answer = max(answer, how_much_shark_ate)

    before_shark_board = deepcopy(board)
    before_shark_fishes = deepcopy(fishes)

    for i in range(1, 17):
        if fishes[i] != [-1, -1, -1]:
            fr, fc, fd = fishes[i]
            for _ in range(8):
                mr = fr + directions[fd][0]
                mc = fc + directions[fd][1]
                if 0 <= mr < 4 and 0 <= mc < 4:
                    if board[mr][mc] != -1:
                        fishes[i] = [mr, mc, fd]
                        fishes[board[mr][mc]][0], fishes[board[mr][mc]][1] = fr, fc
                        board[fr][fc], board[mr][mc] = board[mr][mc], board[fr][fc]
                        break
                    else:
                        fd = (fd + 1) % 8
                else:
                    fd = (fd+1) % 8
    candies = []
    for k in range(1, 4):
        sr, sc, sd = shark
        smr, smc = sr + directions[sd][0]*k, sc + directions[sd][1]*k
        if 0 <= smr < 4 and 0 <= smc < 4:
            if board[smr][smc] != 0:
                candies.append((smr, smc, board[smr][smc]))

    if candies:
        for can in candies:
            board[shark[0]][shark[1]] = 0
            r, c, ate_fish = can
            how_much_shark_ate += ate_fish
            t, ori_row, ori_col, bd = fishes[ate_fish], shark[0], shark[1], shark[2]
            shark[0], shark[1], shark[2] = fishes[ate_fish]
            fishes[ate_fish] = [-1, -1, -1]
            board[r][c] = -1
            teenager_shark_durududdu()
            how_much_shark_ate -= ate_fish
            fishes[ate_fish] = t
            board[r][c] = ate_fish
            shark[0], shark[1], shark[2] = ori_row, ori_col, bd
            board[shark[0]][shark[1]] = -1

    board = before_shark_board
    fishes = before_shark_fishes
    return


answer = 0
how_much_shark_ate = 0
directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
board = [[0]*4 for _ in range(4)]
fishes = [[]]*17
fishes[0] = [-1, -1, -1]
shark = [0, 0, -1]
for i in range(4):
    fs = list(map(int, input().split()))
    for j in range(4):
        board[i][j] = fs[j*2]
        fishes[fs[j*2]] = [i, j, fs[j*2+1]-1]

shark[2] = fishes[board[0][0]][2]
how_much_shark_ate += board[0][0]
fishes[board[0][0]] = [-1, -1, -1]
board[0][0] = -1
teenager_shark_durududdu()
print(answer)
