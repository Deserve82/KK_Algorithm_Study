import sys
from collections import deque

input = sys.stdin.readline
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))


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
    size[a] += size[b]


def dfs(row, col, k):
    S = [(row, col)]
    checker = [[False] * N for _ in range(N)]
    checker[row][col] = True
    piv = 1
    while S:
        r, c = S.pop()
        if piv == k:
            return True
        for d in directions:
            mr, mc = r + d[0], c + d[1]
            if 0 <= mr < N and 0 <= mc < N:
                if board[mr][mc] != 0 and not checker[mr][mc]:
                    piv += 1
                    S.append((mr, mc))
                    checker[mr][mc] = True
    return False


N, K = map(int, input().split())
board = [[0] * N for _ in range(N)]
parent = [i for i in range(K + 1)]
size = [0] * (K + 1)
total = K
q = deque()
for k in range(1, K + 1):
    x, y = map(int, input().split())
    row, col = N - y, x - 1
    board[row][col] = k
    q.append((row, col, k, 0))
    size[k] += 1
is_already_one = dfs(q[0][0], q[0][1], K)
if not is_already_one:
    while q:
        r, c, civil, cost = q.popleft()
        for d in directions:
            p = find(civil)
            mr, mc = r + d[0], c + d[1]
            if 0 <= mr < N and 0 <= mc < N:
                is_p = find(board[mr][mc])
                if board[mr][mc] != 0 and is_p != p:
                    union(p, board[mr][mc])
                    if size[p] >= total:
                        print(cost + 1)
                        exit(0)
                elif is_p == p:
                    continue
                else:
                    q.append((mr, mc, p, cost + 1))
                    board[mr][mc] = p
                    size[p] += 1
                    total += 1
                    for dd in directions:
                        mmr = mr + dd[0]
                        mmc = mc + dd[1]
                        if 0 <= mmr < N and 0 <= mmc < N:
                            if board[mmr][mmc] != 0 and p != find(board[mmr][mmc]):
                                union(p, board[mmr][mmc])
                                if size[p] >= total:
                                    print(cost + 1)
                                    exit(0)
else:
    print(0)

