import sys

input = sys.stdin.readline
n = int(input())
inf = 2 ** 32
board = [[inf] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    board[i][i] = 0
e = int(input())
for _ in range(e):
    s, e, w = map(int, input().split())
    board[s][e] = min(w, board[s][e])

for k in range(n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])
for i in range(n + 1):
    for j in range(n + 1):
        if board[i][j] == inf:
            board[i][j] = 0
for i in range(1, n + 1):
    print(*board[i][1:])
