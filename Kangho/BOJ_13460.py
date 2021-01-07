from collections import deque
import sys
directions = (
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1)
)
ans = []


def move(r, c, mr, mc, is_red):
    if is_red:
        while N > r >= 0 and mr != 0:
            if board[r][c] == "#" or board[r][c] == "B":
                r -= mr
                break
            elif board[r][c] == "O":
                break
            r += mr

        while M > c >= 0 and mc != 0:
            if board[r][c] == "#" or board[r][c] == "B":
                c -= mc
                break
            elif board[r][c] == "O":
                break
            c += mc
    else:
        while N > r >= 0 and mr != 0:
            if board[r][c] == "#" or board[r][c] == "R":
                r -= mr
                break
            elif board[r][c] == "O":
                break
            r += mr

        while M > c >= 0 and mc != 0:
            if board[r][c] == "#" or board[r][c] == "R":
                c -= mc
                break
            elif board[r][c] == "O":
                break
            c += mc
    return r, c


def which_is_first(r, rr, rc, br, bc, dr, dc):
    tr, tb = None, None
    if r:
        rtr, rtc = move(rr, rc, dr, dc, True)
        if board[rtr][rtc] != "O":
            tr = board[rtr][rtc]
            board[rr][rc] = "."
            board[rtr][rtc] = "R"
        else:
            board[rr][rc] = "."
        btr, btc = move(br, bc, dr, dc, False)
    else:
        btr, btc = move(br, bc, dr, dc, False)
        if board[btr][btc] != "O":
            tb = board[btr][btc]
            board[br][bc] = "."
            board[btr][btc] = "B"
        else:
            board[br][bc] = "."
        rtr, rtc = move(rr, rc, dr, dc, True)

    if tr is not None:
        board[rtr][rtc] = tr
    if tb is not None:
        board[btr][btc] = tb
    board[rr][rc] = "R"
    board[br][bc] = "B"
    return (rtr, rtc), (btr, btc)


def bfs():
    q = deque()
    q.append((red_idx, blue_idx, 0))
    while q:
        ri, bi, cost = q.popleft()
        if cost > 9:
            continue
        rr, rc = ri
        br, bc = bi
        board[rr][rc], board[br][bc] = "R", "B"

        for i in range(4):
            dr, dc = directions[i]
            if i == 0:
                if rr < br:
                    red, blue = which_is_first(True, rr, rc, br, bc, dr, dc)
                else:
                    red, blue = which_is_first(False, rr, rc, br, bc, dr, dc)
            elif i == 1:
                if rr > br:
                    red, blue = which_is_first(True, rr, rc, br, bc, dr, dc)
                else:
                    red, blue = which_is_first(False, rr, rc, br, bc, dr, dc)
            elif i == 2:
                if rc > bc:
                    red, blue = which_is_first(True, rr, rc, br, bc, dr, dc)
                else:
                    red, blue = which_is_first(False, rr, rc, br, bc, dr, dc)
            else:
                if rc > bc:
                    red, blue = which_is_first(False, rr, rc, br, bc, dr, dc)
                else:
                    red, blue = which_is_first(True, rr, rc, br, bc, dr, dc)

            if board[red[0]][red[1]] == "O" and board[blue[0]][blue[1]] != "O":
                print(cost + 1)
                exit(0)
            else:
                if (red != ri or blue != bi) and red != blue and board[blue[0]][blue[1]] != "O":
                    q.append((red, blue, cost + 1))

        board[rr][rc] = "."
        board[br][bc] = "."
    print("-1")


N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(sys.stdin.readline()))
red_idx = (-1, -1)
blue_idx = (-1, -1)
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red_idx = (i, j)
        elif board[i][j] == 'B':
            blue_idx = (i, j)
bfs()
