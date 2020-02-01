N = int(input())
field = []
for i in range(N):
    field.append(list(map(int, input().split())))
# 가로 -> 0, 대각선 -> 1, 세로 -> 2
location = [0, 1, 0]
answer_list = []

# 가로 to 가로, 가로 to 대각선
def move(location, field):
    # location[0] == x, location[1] == y
    if location[0] == N-1 and location[1] == N-1:
        answer_list.append(1)
    if location[2] == 0:
        if location[0]+1 < N and location[1]+1 < N:
            if field[location[0]+1][location[1]+1] == 0 and field[location[0]+1][location[1]] == 0 and field[location[0]][location[1]+1] == 0:
                location[0] += 1
                location[1] += 1
                location[2] = 1
                move(location, field)
                location[0] -= 1
                location[1] -= 1
                location[2] = 0
        if location[1]+1 < N:
            if field[location[0]][location[1]+1] == 0:
                location[1] += 1
                move(location, field)
                location[1] -= 1
    elif location[2] == 1:
        if location[0]+1 < N and location[1]+1 < N:
            if field[location[0]+1][location[1]+1] == 0 and field[location[0]+1][location[1]] == 0 and field[location[0]][location[1]+1] == 0:
                location[0] += 1
                location[1] += 1
                move(location, field)
                location[0] -= 1
                location[1] -= 1
        if location[1]+1 < N:
            if field[location[0]][location[1]+1] == 0:
                location[1] += 1
                location[2] = 0
                move(location, field)
                location[1] -= 1
                location[2] = 1
        if location[0]+1 < N:
            if field[location[0]+1][location[1]] == 0:
                location[0] += 1
                location[2] = 2
                move(location, field)
                location[0] -= 1
                location[2] = 1

    elif location[2] == 2:
        if location[0]+1 < N and location[1]+1 < N:
            if field[location[0]+1][location[1]+1] == 0 and field[location[0]+1][location[1]] == 0 and field[location[0]][location[1]+1] == 0:
                location[0] += 1
                location[1] += 1
                location[2] = 1
                move(location, field)
                location[0] -= 1
                location[1] -= 1
                location[2] = 2
        if location[0]+1 < N:
            if field[location[0]+1][location[1]] == 0:
                location[0] += 1
                move(location, field)
                location[0] -= 1



move(location, field)
print(len(answer_list))