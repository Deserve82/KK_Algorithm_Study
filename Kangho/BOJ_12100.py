from copy import deepcopy

directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def move(idx):
    global max_num
    if idx == 3:
        for j in range(N):
            added = []
            for i in range(1, N):
                if board[i][j] != 0:
                    t = i
                    while t > 0:
                        if board[t - 1][j] == board[t][j] and t - 1 not in added:
                            board[t - 1][j] = 2 * board[t][j]
                            max_num = max(board[i - 1][j], max_num)
                            board[t][j] = 0
                            added.append(t - 1)
                            break
                        elif board[t - 1][j] == board[t][j] and t - 1 in added:
                            break
                        elif board[t - 1][j] != 0 and board[t][j] != board[t - 1][j]:
                            break
                        else:
                            board[t - 1][j] = board[t][j]
                            board[t][j] = 0
                            t -= 1
    elif idx == 1:
        for i in range(N):
            added = []
            for j in range(N - 2, -1, -1):
                if board[i][j] != 0:
                    t = j
                    while t < N - 1:
                        if board[i][t + 1] == board[i][t] and t + 1 not in added:
                            board[i][t + 1] = 2 * board[i][t]
                            max_num = max(board[i][t + 1], max_num)
                            board[i][t] = 0
                            added.append(t + 1)
                            break
                        elif board[i][t + 1] == board[i][t] and t + 1 in added:
                            break
                        elif board[i][t + 1] != 0 and board[i][t] != board[i][t + 1]:
                            break
                        else:
                            board[i][t + 1] = board[i][t]
                            board[i][t] = 0
                            t += 1
    elif idx == 2:
        for i in range(N):
            added = []
            for j in range(1, N):
                if board[i][j] != 0:
                    t = j
                    while t > 0:
                        if board[i][t - 1] == board[i][t] and t - 1 not in added:
                            board[i][t - 1] = 2 * board[i][t]
                            max_num = max(board[i][t - 1], max_num)
                            board[i][t] = 0
                            added.append(t - 1)
                            break
                        elif board[i][t - 1] == board[i][t] and t - 1 in added:
                            break
                        elif board[i][t - 1] != 0 and board[i][t] != board[i][t - 1]:
                            break
                        else:
                            board[i][t - 1] = board[i][t]
                            board[i][t] = 0
                            t -= 1
    else:
        for j in range(N):
            added = []
            for i in range(N - 2, -1, -1):
                if board[i][j] != 0:
                    t = i
                    while t < N - 1:
                        if board[t + 1][j] == board[t][j] and t + 1 not in added:
                            board[t + 1][j] += board[t][j]
                            max_num = max(board[t + 1][j], max_num)
                            board[t][j] = 0
                            added.append(t + 1)
                            break
                        elif board[t + 1][j] == board[t][j] and t + 1 in added:
                            break
                        elif board[t + 1][j] != 0 and board[t][j] != board[t + 1][j]:
                            break
                        else:
                            board[t + 1][j] = board[t][j]
                            board[t][j] = 0
                            t += 1
    return


def solve(idx):
    global board, extra_board
    if idx == 5:
        return
    extra_board[idx] = deepcopy(board)
    for i in range(4):
        move(i)
        solve(idx + 1)
        board = deepcopy(extra_board[idx])


max_num = 0
N = int(input())
board = []
extra_board = [[] for _ in range(5)]
for _ in range(N):
    a = list(map(int, input().split()))
    max_num = max(max_num, max(a))
    board.append(a)
solve(0)
print(max_num)
