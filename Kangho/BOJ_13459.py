movements = [(0, -1), (0, 1), (-1, 0), (1, 0)]
answer = 11


def move_red(d):
    global red
    if red == hole:
        return
    rr, rc = red
    board[rr][rc] = '.'
    while 0 <= rr + movements[d][0] < R and 0 <= rc + movements[d][1] < C:
        mrr, mrc = rr + movements[d][0], rc + movements[d][1]
        if mrr == hole[0] and mrc == hole[1]:
            red = [mrr, mrc]
            return
        elif board[mrr][mrc] == '.':
            rr = mrr
            rc = mrc
        else:
            break
    board[rr][rc] = 'R'
    red = [rr, rc]


def move_blue(d):
    global blue
    if blue == hole:
        return
    br, bc = blue
    board[br][bc] = '.'
    while 0 <= br + movements[d][0] < R and 0 <= bc + movements[d][1] < C:
        mrr, mrc = br + movements[d][0], bc + movements[d][1]
        if mrr == hole[0] and mrc == hole[1]:
            blue = [mrr, mrc]
            return
        elif board[mrr][mrc] == '.':
            br = mrr
            bc = mrc
        else:
            break
    board[br][bc] = 'B'
    blue = [br, bc]


def tilt(d):
    # 0은 왼쪽, 1은 오른쪽, 2는 위, 3은 아래
    board[hole[0]][hole[1]] = '0'
    if d == 0:
        if red[1] < blue[1]:
            move_red(d)
            move_blue(d)
        else:
            move_blue(d)
            move_red(d)
    elif d == 1:
        if red[1] < blue[1]:
            move_blue(d)
            move_red(d)
        else:
            move_red(d)
            move_blue(d)
    elif d == 2:
        if red[0] < blue[0]:
            move_red(d)
            move_blue(d)
        else:
            move_blue(d)
            move_red(d)
    else:
        if red[0] < blue[0]:
            move_blue(d)
            move_red(d)
        else:
            move_red(d)
            move_blue(d)


def brute_force(cnt, prev):
    global answer, red, blue
    if cnt > 10 or answer <= 10:
        return
    if red == hole and blue != hole:
        answer = min(answer, cnt)
        return

    for rot in range(4):
        if prev != rot:
            temp_row_r, temp_col_r = red
            temp_row_b, temp_col_b = blue
            tilt(rot)
            brute_force(cnt + 1, rot)
            board[red[0]][red[1]] = '.'
            board[blue[0]][blue[1]] = '.'
            red = [temp_row_r, temp_col_r]
            blue = [temp_row_b, temp_col_b]
            board[red[0]][red[1]] = 'R'
            board[blue[0]][blue[1]] = 'B'


R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input()))
hole, red, blue = [-1, -1], [-1, -1], [-1, -1]
for i in range(R):
    for j in range(C):
        if board[i][j] == 'B':
            blue = [i, j]
        elif board[i][j] == 'R':
            red = [i, j]
        elif board[i][j] == 'O':
            hole = [i, j]
brute_force(0, -1)
if answer > 10:
    print(0)
else:
    print(1)
    print(answer)
