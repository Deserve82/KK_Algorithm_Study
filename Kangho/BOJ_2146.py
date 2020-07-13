m_r = [0, 1, 0, -1]
m_c = [1, 0, -1, 0]


def dfs(loc):
    s = [loc]
    rv = [loc]
    while s:
        r, c = s.pop()
        for d in range(4):
            moved_row = r + m_r[d]
            moved_col = c + m_c[d]
            if moved_row > n-1 or moved_row < 0 or moved_col > n-1 or moved_col < 0:
                continue
            else:
                if world_map[moved_row][moved_col] == 1:
                    world_map[moved_row][moved_col] = 0
                    s.append((moved_row, moved_col))
                    rv.append((moved_row, moved_col))
    return rv


n = int(input())
min_dis = 1000000
world_map = []
islands = []
for _ in range(n):
    world_map.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if world_map[i][j] == 1:
            world_map[i][j] = 0
            islands.append(dfs((i, j)))
checker = [False for _ in range(len(islands))]
for j, selected in enumerate(islands):
    checker[j] = True
    for loc in selected:
        for k, left in enumerate(islands):
            if selected != left and not checker[k]:
                for i in left:
                    if abs(loc[0]-i[0]) + abs(loc[1]-i[1]) - 1 < min_dis:
                        min_dis = abs(loc[0]-i[0]) + abs(loc[1]-i[1]) - 1
print(min_dis)
