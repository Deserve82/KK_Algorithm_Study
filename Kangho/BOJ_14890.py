N, L = map(int, input().split())
field = []
for _ in range(N):
    temp = list(map(int, input().split()))
    field.append(temp)
answer = 0
second_field = [[0]*N for i in range(N)]
for r in range(N):
    for c in range(N):
        second_field[r][c] = field[c][r]


def haha(field):
    global answer
    for i in range(N):
        temp_checker = 0
        index_saver = [-1, ""]
        status = ""
        for j in range(1, N):
            if field[i][j-1] == field[i][j]:
                temp_checker += 1
            elif abs(field[i][j-1]-field[i][j]) == 1:
                if field[i][j-1] - field[i][j] > 0:
                    status = "dsc"
                if field[i][j-1] - field[i][j] < 0:
                    status = "asc"
                if temp_checker+1 >= L and index_saver[0] < 0:
                    index_saver[0] = j
                    temp_checker += 1
                    index_saver[1] = status
                elif index_saver[0] < 0 and status == "dsc":
                    index_saver[0] = j
                    temp_checker += 1
                    index_saver[1] = status
                elif temp_checker+1 >= L and index_saver[0] > 0:
                    if index_saver[1] == status:
                        if j-index_saver[0] >= L:
                            temp_checker += 1
                            index_saver[0] = j
                            index_saver[1] = status
                    elif status == "dsc" and index_saver[1] == "asc":
                        temp_checker += 1
                        index_saver[0] = j
                        index_saver[1] = status
                    else:
                        if j-index_saver[0] >= 2*L:
                            temp_checker += 1
                            index_saver[0] = j
                            index_saver[1] = status
            else:
                break
        if N - index_saver[0] < L and status == "dsc":
            temp_checker -= 1
        if temp_checker == N-1:
            answer += 1


haha(field)
haha(second_field)
print(answer)