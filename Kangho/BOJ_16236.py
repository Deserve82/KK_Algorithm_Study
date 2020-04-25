import copy

n = int(input())
sea = []
for _ in range(n):
    sea.append(list(map(int, input().split())))
shark_size = 2
eaten_fishes = 0
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
dis_list = [[0]*n for _ in range(n)]


def search_fish(i, j):
    global shark_size
    global eaten_fishes
    q = [[i, j]]
    fish_tank = []
    dis = copy.deepcopy(dis_list)
    temp_sea = copy.deepcopy(sea)
    temp_sea[i][j] = 0
    while q:
        location = q.pop(0)
        row = location[0]
        column = location[1]

        for k in range(4):
            m_row = row + dx[k]
            m_column = column + dy[k]
            if m_row < 0 or m_row > n - 1 or m_column < 0 or m_column > n - 1:
                pass
            else:
                dis[m_row][m_column] = dis[row][column] + 1
                if sea[m_row][m_column] == shark_size or sea[m_row][m_column] == 0 or sea[m_row][m_column] == 9:
                    if temp_sea[m_row][m_column] == 10:
                        pass
                    else:
                        q.append([m_row, m_column])
                        temp_sea[m_row][m_column] = 10
                elif sea[m_row][m_column] < shark_size:
                    temp_sea[m_row][m_column] = 10
                    fish_tank.append([m_row, m_column, dis[m_row][m_column]])

    value = 100000
    fish_row = i
    fish_column = j
    for fish in fish_tank:
        if fish[2] < value:
            value = fish[2]
            fish_row = fish[0]
            fish_column = fish[1]
        elif fish[2] == value:
            if fish[0] < fish_row:
                fish_row = fish[0]
                fish_column = fish[1]
            elif fish[0] == fish_row:
                if fish[1] < fish_column:
                    fish_column = fish[1]
    sea[fish_row][fish_column] = 0
    eaten_fishes += 1
    if shark_size == eaten_fishes:
        eaten_fishes = 0
        shark_size += 1
    return [fish_row, fish_column, value]


time = 0
for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            shark_loc = [i, j, 0]
            flag = True
            while flag:
                result = search_fish(shark_loc[0], shark_loc[1])
                if shark_loc[0] == result[0] and shark_loc[1] == result[1]:
                    flag = False
                else:
                    shark_loc = result
                    time += result[2]
            break
print(time)
