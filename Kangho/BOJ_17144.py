import sys
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def spread(row, col, val):
    global R, C
    spreading_val = val // 5
    cnt = 0
    for i in range(4):
        mr = directions[i][0] + row
        mc = directions[i][1] + col
        if R > mr > -1 and -1 < mc < C:
            if room[mr][mc] != -1:
                cnt += 1
                room[mr][mc] += spreading_val
    room[row][col] -= spreading_val * cnt


def circulate():
    g1_r, g1_c = green_factory[0]
    g2_r, g2_c = green_factory[1]
    # 위쪽 공기 청정기
    for i in range(g1_r, 0, -1):
        if room[i][0] == -1:
            continue
        room[i][0] = room[i-1][0]
    for i in range(0, C-1):
        if room[0][i] == -1:
            continue
        room[0][i] = room[0][i+1]
    room[0][C-1] = 0
    for i in range(0, g1_r):
        room[i][-1] = room[i+1][-1]
    for i in range(C-1, 0, -1):
        if room[g1_r][i-1] == -1:
            room[g1_r][i] = 0
        else:
            room[g1_r][i] = room[g1_r][i-1]

    # 아래쪽 공기 청정기
    for i in range(g2_r, R-1):
        if room[i][0] == -1:
            continue
        room[i][0] = room[i+1][0]
    for i in range(0, C-1):
        room[-1][i] = room[-1][i+1]
    for i in range(R-1, g2_r-1, -1):
        room[i][-1] = room[i-1][-1]
    for i in range(C-1, 0, -1):
        if room[g2_r][i-1] == -1:
            room[g2_r][i] = 0
        else:
            room[g2_r][i] = room[g2_r][i-1]


R, C, T = map(int, sys.stdin.readline().split())
room = []
for _ in range(R):
    room.append(list(map(int, sys.stdin.readline().split())))
green_factory = []
for i in range(R-1):
    if room[i][0] == -1:
        green_factory.append((i, 0))
        green_factory.append((i+1, 0))
        break

while T > 0:
    T -= 1
    should_spread = []
    for i in range(R):
        for j in range(C):
            if room[i][j] != 0 and room[i][j] != -1:
                should_spread.append((i, j, room[i][j]))
    for ss in should_spread:
        spread(ss[0], ss[1], ss[2])
    circulate()

sum_of_dust = 0
for i in range(R):
    for j in range(C):
        if room[i][j] != -1:
            sum_of_dust += room[i][j]
print(sum_of_dust)
