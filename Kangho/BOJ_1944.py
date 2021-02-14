import sys
from collections import deque
input = sys.stdin.readline

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    parent[b] = a


directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
N, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input()))
points = []
parent = [i for i in range(K + 2)]
k_val = 2
for i in range(N):
    for j in range(N):
        if board[i][j] == '1':
            board[i][j] = -1
        elif board[i][j] == 'S':
            board[i][j] = 1
            points.append((i, j, 1, 0))
        elif board[i][j] == 'K':
            board[i][j] = k_val
            points.append((i, j, k_val, 0))
            k_val += 1
        else:
            board[i][j] = 0
edges = []
for point in points:
    checker = [[False] * N for _ in range(N)]
    checker[point[0]][point[1]] = True
    q = deque()
    q.append(point)
    while q:
        row, col, idx, cost = q.popleft()
        for d in directions:
            mr, mc = row + d[0], col + d[1]
            if 0 <= mr < N and 0 <= mc < N:
                if board[mr][mc] > 0 and not checker[mr][mc]:
                    edges.append((cost + 1, idx, board[mr][mc]))
                    q.append((mr, mc, idx, cost + 1))
                    checker[mr][mc] = True
                elif not checker[mr][mc] and board[mr][mc] == 0:
                    q.append((mr, mc, idx, cost + 1))
                    checker[mr][mc] = True
edges.sort()
total_val = 0
for edge in edges:
    cost, f, t = edge
    if find(f) != find(t):
        total_val += cost
        union(f, t)
if len(set(parent)) > 2:
    print(-1)
else:
    print(total_val)
