n, L, R = map(int, input().split())
nations = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for _ in range(n):
    temp = list(map(int, input().split()))
    temp_list = []
    for z in temp:
        temp_list.append([z, False])
    nations.append(temp_list)
loop = 0
count = -1
while True:
    sums = 0
    count = 0
    for i in range(n):
        for j in range(n):
            for d in range(4):
                m_i = i+dx[d]
                m_j = j+dy[d]
                if -1 < m_i < n and -1 < m_j < n:
                    if L <= abs(nations[i][j][0]-nations[m_i][m_j][0]) <= R:
                        if not nations[i][j][1]:
                            nations[i][j][1] = True
                            count += 1
                        if not nations[m_i][m_j][1]:
                            nations[m_i][m_j][1] = True
                            count += 1

    if count == 0:
        break
    for i in range(n):
        for j in range(n):
            if nations[i][j][1]:
                Q = []
                even_list = []
                Q.append((i, j))
                even_list.append((i, j))
                group_count = 1
                sums += nations[i][j][0]
                nations[i][j][1] = False
                while Q:
                    location = Q.pop(0)
                    for d in range(4):
                        m_i = location[0] + dx[d]
                        m_j = location[1] + dy[d]
                        if -1 < m_i < n and -1 < m_j < n:
                            if nations[m_i][m_j][1] and L <= abs(nations[location[0]][location[1]][0]-nations[m_i][m_j][0]) <= R:
                                Q.append((m_i, m_j))
                                group_count += 1
                                sums += nations[m_i][m_j][0]
                                nations[m_i][m_j][1] = False
                                even_list.append((m_i, m_j))
                ev = int(sums/group_count)

                while even_list:
                    change_value = even_list.pop()
                    nations[change_value[0]][change_value[1]][0] = ev
    loop += 1
print(loop)