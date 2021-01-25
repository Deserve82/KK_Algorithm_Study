from collections import deque

movements = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dfs(r, c):
    global have_same
    s = [(r, c, board[r][c])]
    while s:
        row, col, val = s.pop()
        for i in range(4):
            mr = row + movements[i][0]
            mc = col + movements[i][1]
            if 0 <= mr < N and 0 <= mc < M:
                if board[mr][mc] == val and board[mr][mc] != 0:
                    s.append((mr, mc, board[mr][mc]))
                    board[mr][mc] = 0
                    board[row][col] = 0
                    have_same = True

        if col == 0 or col == M - 1:
            mr = row
            if col == M - 1:
                mc = 0
            else:
                mc = M - 1
            if board[mr][mc] == val and board[mr][mc] != 0:
                s.append((mr, mc, val))
                board[mr][mc] = 0
                board[row][col] = 0
                have_same = True


N, M, T = map(int, input().split())
board = []
rotations = []
for _ in range(N):
    board.append(deque(list(map(int, input().split()))))
for _ in range(T):
    index, direction, distance = map(int, input().split())
    if direction == 0:
        direction = 1
    else:
        direction = -1
    rotations.append((index - 1, direction, distance))

for rotation in rotations:
    have_same = False
    idx, di, t = rotation
    baesu = 1
    while (idx + 1) * baesu - 1 < N:
        board[(idx + 1) * baesu - 1].rotate(di * t)
        baesu += 1

    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                dfs(i, j)
    if not have_same:
        cnt, sums = 0, 0
        for i in range(N):
            for j in range(M):
                if board[i][j] != 0:
                    cnt += 1
                    sums += board[i][j]
        if cnt != 0:
            avg = sums / cnt
        else:
            avg = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] > avg and board[i][j] != 0:
                    board[i][j] -= 1
                elif board[i][j] < avg and board[i][j] != 0:
                    board[i][j] += 1
answer = 0
for z in board:
    answer += sum(z)
print(answer)
