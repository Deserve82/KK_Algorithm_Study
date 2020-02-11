N, M = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
f = []
walls = []
answer_list = []
for i in range(N):
    temp = list(map(int, input()))
    f.append(temp)
distance = [[[0, 0] for _ in range(M)] for _ in range(N)]


def bfs():
    Q = []
    Q.append([0, 0, 0])
    distance[0][0][0] = 1

    while Q:
        location = Q.pop(0)
        if location[0] == N-1 and location[1] == M-1:
            return distance[location[0]][location[1]][location[2]]
        for i in range(4):
            nx, ny = location[0]+dx[i], location[1]+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if f[nx][ny] == 0:
                distance[nx][ny][location[2]] = distance[location[0]][location[1]][location[2]] + 1
                Q.append([nx, ny, location[2]])
            if f[nx][ny] == 1 and location[2] == 0:
                distance[nx][ny][1] = distance[location[0]][location[1]][location[2]] + 1
                Q.append([nx, ny, 1])
    return -1


print(bfs())
