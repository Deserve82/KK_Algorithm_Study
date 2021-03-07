import sys
from collections import deque
input = sys.stdin.readline
movements = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dp(start, what_we_have, val):
    global answer
    if what_we_have == all_have:
        answer = min(answer, val)

    for node in graph[start]:
        nxt, cos = node
        if what_we_have & (1 << nxt) == 0:
            dp(nxt, what_we_have | (1 << nxt), val+cos)


def bfs(r, c):
    q = deque()
    pivot = board[r][c]
    q.append((r, c, 0))
    checker = [[False] * C for _ in range(R)]
    while q:
        cr, cc, cost = q.popleft()
        if board[cr][cc] != pivot and board[cr][cc] != '.':
            graph[pivot].append((board[cr][cc], cost))
        for move in movements:
            mr, mc = move[0] + cr, move[1] + cc
            if 0 <= mr < R and 0 <= mc < C:
                if board[mr][mc] != 'x' and not checker[mr][mc]:
                    checker[mr][mc] = True
                    q.append((mr, mc, cost + 1))


while True:
    C, R = map(int, input().split())
    if C == 0 and R == 0:
        break
    board = []
    for _ in range(R):
        board.append(list(input().rstrip()))
    locations = []
    dirty_idx = 1
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'o':
                board[i][j] = 0
                locations.append((i, j))
            elif board[i][j] == '*':
                board[i][j] = dirty_idx
                dirty_idx += 1
                locations.append((i, j))

    graph = [[] for _ in range(dirty_idx)]
    for location in locations:
        bfs(location[0], location[1])
    all_have = 0
    for i in range(dirty_idx):
        all_have |= (1 << i)
    answer = 999999999
    dp(0, 1, 0)
    if answer >= 999999999:
        print(-1)
    else:
        print(answer)
