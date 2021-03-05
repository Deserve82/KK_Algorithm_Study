import sys
from collections import deque
input = sys.stdin.readline
movements = [(0, 1), (1, 0), (-1, 0), (0, -1)]
R, C, K = map(int, input().rstrip().split())
board = []
for _ in range(R):
    board.append(list(map(int, list(input().rstrip()))))
answer = -1
q = deque()
q.append((0, 0, 0))
check = [[[-1] * (K+1) for _ in range(C)] for _ in range(R)]
check[0][0][0] = 0
while q:
    row, col, broken_wall = q.popleft()
    if row == R-1 and col == C-1:
        answer = check[row][col][broken_wall] + 1
        break
    for move in movements:
        mr, mc = row + move[0], col + move[1]
        if 0 <= mr < R and 0 <= mc < C:
            if board[mr][mc] == 1 and broken_wall < K and check[mr][mc][broken_wall] == -1:
                check[mr][mc][broken_wall+1] = 1 + check[row][col][broken_wall]
                q.append((mr, mc, broken_wall + 1))
            elif board[mr][mc] == 0 and check[mr][mc][broken_wall] == -1:
                check[mr][mc][broken_wall] = 1 + check[row][col][broken_wall]
                q.append((mr, mc, broken_wall))
print(answer)
