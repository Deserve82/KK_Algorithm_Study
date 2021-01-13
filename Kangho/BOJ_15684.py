def check():
    same = True
    for j in range(N):
        t = j
        for i in range(H):
            t += board[i][t]
        if t != j:
            same = False
            break
    return same


def solve(cnt, idx):
    global la
    if check():
        answer.add(cnt)

    if cnt >= 3:
        return

    for k in range(idx, la):
        row, col = able_space[k]
        if board[row][col] == 0:
            board[row][col], board[row][col + 1] = 1, -1
            solve(cnt + 1, k + 1)
            board[row][col], board[row][col + 1] = 0, 0


answer = set()
N, M, H = map(int, input().split())
board = [[0] * (N+1) for _ in range(H+1)]
for _ in range(M):
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    board[s][e] = 1
    board[s][e + 1] = -1
able_space = []
for i in range(H):
    for j in range(N - 1):
        if board[i][j] == 0 and board[i][j + 1] == 0:
            able_space.append((i, j))
la = len(able_space)
solve(0, 0)
if answer:
    print(min(answer))
else:
    print(-1)
