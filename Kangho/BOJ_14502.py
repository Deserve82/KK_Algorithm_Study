import copy
N, M = map(int, input().split())
field = []
for i in range(N):
    field.append(list(map(int, input().split())))
wall_count = 0
answer = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def wall_set(field):
    global wall_count
    global answer
    if wall_count == 3:
        t = copy.deepcopy(field)
        temp = spread_virus(t)
        con = 0
        for i in temp:
            for k in i:
                if k == 0:
                    con += 1
        if con > answer:
            answer = con
        return
    for i in range(N):
        for j in range(M):
            if field[i][j] == 0:
                field[i][j] = 1
                wall_count += 1
                wall_set(field)
                wall_count -= 1
                field[i][j] = 0
            else:
                pass


def spread_virus(local_field):
    for i in range(N):
        for j in range(M):
            if local_field[i][j] == 2:
                Q = []
                Q.append([i, j])
                while Q:
                    for k in range(4):
                        if N > Q[0][0] + dx[k] > -1 and M > Q[0][1] + dy[k] > -1:
                            n_row = Q[0][0] + dx[k]
                            n_column = Q[0][1] + dy[k]
                            if local_field[n_row][n_column] == 0:
                                local_field[n_row][n_column] = 2
                                Q.append([n_row, n_column])
                    Q.pop(0)
    return local_field


wall_set(field)
print(answer)
