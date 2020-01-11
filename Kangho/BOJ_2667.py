N = int(input())
Map = []
for i in range(N):
    Map.append(list(input()))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited_map = [['0' for i in range(N)] for j in range(N)]
Apartment_complex = []
idx = 0
for row in range(N):
    for column in range(N):
        if Map[row][column] == '1' and visited_map[row][column] != '1':
            visited_map[row][column] = '1'
            Q = []
            Q.append([row, column])
            count = 0
            while Q:
                for i in range(4):
                    if N > Q[0][0]+dx[i] > -1 and N > Q[0][1]+dy[i] > -1:
                        n_row = Q[0][0] + dx[i]
                        n_column = Q[0][1] + dy[i]
                        if visited_map[n_row][n_column] == '0' and Map[n_row][n_column] == '1':
                            Q.append([n_row, n_column])
                            visited_map[n_row][n_column] = '1'
                Q.pop(0)
                count += 1
            Apartment_complex.append(count)
print(len(Apartment_complex))
Apartment_complex.sort()
for i in Apartment_complex:
    print(i)