import copy
r, c = map(int, input().split())

field = []
cheese = []
count = 0

for _ in range(r):
    temp = list(map(int, input().split()))
    field.append(temp)

check_field = copy.deepcopy(field)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs():
    global r, c
    Q = []
    Q.append([0, 0])
    melting = []
    while Q:
        location = Q.pop(0)
        for d in range(4):
            m_r = location[0]+dx[d]
            m_c = location[1]+dy[d]
            if -1 < m_r < r and -1 < m_c < c:
                if field[m_r][m_c] == 0 and check_field[m_r][m_c] == 0:
                    check_field[m_r][m_c] = 2
                    Q.append([m_r, m_c])
                elif field[m_r][m_c] == 1 and check_field[m_r][m_c] == 1:
                    melting.append([m_r, m_c])
    return melting


while True:
    gonna_melt = dfs()
    n_c = 0
    if gonna_melt:
        count += 1
        for part in gonna_melt:
            if field[part[0]][part[1]] == 1:
                n_c += 1
                field[part[0]][part[1]] = 0
                check_field[part[0]][part[1]] = 0
        cheese.append(n_c)
    else:
        break
    check_field = copy.deepcopy(field)
print(count, cheese[-1])