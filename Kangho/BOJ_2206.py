from sys import stdin
from collections import deque
input = stdin.readline
N, M = map(int, input().split())
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
f = []
for i in range(N):
    f.append(list(input()))
distance = [[[0, 0] for _ in range(M)] for _ in range(N)]


def bfs():
    Q = deque()
    Q.append((0, 0, 0))
    distance[0][0][0] = 1

    while Q:
        x, y, w = Q.popleft()
        if x == N-1 and y == M-1:
            return distance[x][y][w]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if distance[nx][ny][w]:
                continue
            if f[nx][ny] == '0':
                distance[nx][ny][w] = distance[x][y][w] + 1
                Q.append((nx, ny, w))
            if f[nx][ny] == '1' and w == 0:
                distance[nx][ny][1] = distance[x][y][w] + 1
                Q.append((nx, ny, 1))
    return -1


print(bfs())
