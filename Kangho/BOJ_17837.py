from collections import deque

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
rd = [1, 0, 3, 2]


def move_family(f, t, node, is_reverse):
    from_row, from_col = f
    to_row, to_col = t
    tmp = deque()
    while curr_state[from_row][from_col]:
        t = curr_state[from_row][from_col].pop()
        mals[t][0], mals[t][1] = to_row, to_col
        if t == node:
            tmp.appendleft(t)
            break
        else:
            tmp.appendleft(t)
    if not is_reverse:
        curr_state[to_row][to_col].extend(tmp)
    else:
        tmp.reverse()
        curr_state[to_row][to_col].extend(tmp)


N, K = map(int, input().split())
mals = []
tboard = []
for _ in range(N):
    tboard.append(list(map(int, input().split())))
board = [[2]*(N+2) for _ in range(N+2)]
for i in range(N):
    for j in range(N):
        board[i+1][j+1] = tboard[i][j]
curr_state = [[deque() for _ in range(N+2)] for _ in range(N+2)]
for i in range(K):
    x, y, z = map(int, input().split())
    mals.append([x, y, z - 1])
    curr_state[x][y].append(i)
time = 0
game_over = False
while time <= 1000 and not game_over:
    time += 1
    for k, mal in enumerate(mals):
        row, col, d = mal
        m_row, m_col = row+directions[d][0], col+directions[d][1]
        if board[m_row][m_col] == 0:
            move_family((row, col), (m_row, m_col), k, False)
            if len(curr_state[m_row][m_col]) > 3:
                game_over = True
        elif board[m_row][m_col] == 1:
            move_family((row, col), (m_row, m_col), k, True)
            if len(curr_state[m_row][m_col]) > 3:
                game_over = True
        else:
            rm_row, rm_col = row + directions[rd[d]][0], col + directions[rd[d]][1]
            mals[k][2] = rd[d]
            if board[rm_row][rm_col] == 2:
                continue
            elif board[rm_row][rm_col] == 1:
                move_family((row, col), (rm_row, rm_col), k, True)
                if len(curr_state[rm_row][rm_col]) > 3:
                    game_over = True
            else:
                move_family((row, col), (rm_row, rm_col), k, False)
                if len(curr_state[rm_row][rm_col]) > 3:
                    game_over = True
if time > 1000:
    print(-1)
else:
    print(time)
