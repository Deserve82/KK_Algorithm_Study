import copy
N, M = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
field = []
walls = []
answer_list = []
for i in range(N):
    temp = list(map(int, input()))
    field.append(temp)


def bfs(f):
    visited_field = copy.deepcopy(f)
    visited_field[0][0] = 1
    distance = [[0 for _ in range(M)] for _ in range(N)]
    distance[0][0] = 1
    Q = []
    Q.append([0, 0])

    while Q:
        location = Q.pop(0)
        for k in range(4):
            m_row = location[0]+dx[k]
            m_column = location[1]+dy[k]
            if -1 < m_row < N and -1 < m_column < M:
                if f[m_row][m_column] == 0 and visited_field[m_row][m_column] == 0:
                    distance[m_row][m_column] = distance[location[0]][location[1]] + 1
                    visited_field[m_row][m_column] = 1
                    Q.append([m_row, m_column])
    return distance[N-1][M-1]

print(bfs(field))