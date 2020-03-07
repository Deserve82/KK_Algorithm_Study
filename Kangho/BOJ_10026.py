n = int(input())
f = []
check = [[0] * n for _ in range(n)]
count = 0
rg_count = 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    f.append(list(input()))


def bfs_red_green_different(i, j):
    q = [[i, j]]
    while q:
        location = q.pop(0)
        for move in range(4):
            m_r = location[0] + dx[move]
            m_c = location[1] + dy[move]
            if -1 < m_r < n and -1 < m_c < n:
                if check[m_r][m_c] == 0 and f[i][j] == f[m_r][m_c]:
                    q.append([m_r, m_c])
                    check[m_r][m_c] = 1


for i in range(n):
    for j in range(n):
        if check[i][j] == 0:
            bfs_red_green_different(i, j)
            count += 1

for z in range(n):
    for x in range(n):
        if f[z][x] == 'R':
            f[z][x] = 'G'

check = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if check[i][j] == 0:
            bfs_red_green_different(i, j)
            rg_count += 1

print(count, rg_count)
