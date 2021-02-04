from copy import deepcopy

GREEN = [[0] * 4 for _ in range(6)]
BLUE = [[0] * 6 for _ in range(4)]
point = 0


def cnt():
    s = 0
    for i in range(6):
        for j in range(6):
            if i >= 2 and j < 4:
                s += GREEN[i][j]
            if j >= 2 and i < 4:
                s += BLUE[i][j]
    return s


def check_green_line(is_point):
    global point
    for i in range(2, 6):
        is_line = True
        for j in range(4):
            if GREEN[i][j] == 0:
                is_line = False
                break
        if is_line:
            if is_point:
                point += 1
            for k in range(i - 1, -1, -1):
                for j in range(4):
                    GREEN[k + 1][j] = GREEN[k][j]
            for k in range(4):
                GREEN[0][k] = 0


def check_blue_line(is_point):
    global point
    for i in range(2, 6):
        is_line = True
        for j in range(4):
            if BLUE[j][i] == 0:
                is_line = False
                break
        if is_line:
            if is_point:
                point += 1
            for k in range(i - 1, -1, -1):
                for j in range(4):
                    BLUE[j][k + 1] = BLUE[j][k]
            for k in range(4):
                BLUE[k][0] = 0


def check_mint():
    have = 0
    for i in range(2):
        for j in range(4):
            if GREEN[i][j] != 0:
                have += 1
                break
    if have:
        for _ in range(have):
            for k in range(4):
                GREEN[5][k] = 1
            check_green_line(False)

        for i in range(2):
            for j in range(4):
                GREEN[i][j] = 0


def check_sky():
    have = 0
    for i in range(2):
        for j in range(4):
            if BLUE[j][i] != 0:
                have += 1
                break
    if have:
        for _ in range(have):
            for k in range(4):
                BLUE[k][5] = 1
            check_blue_line(False)

        for i in range(2):
            for j in range(4):
                BLUE[j][i] = 0


def move_green(blocks):
    can_go = True
    if len(blocks) == 1:
        blocks[0][0] = -1
    else:
        if blocks[0][0] == blocks[1][0]:
            blocks[0][0], blocks[1][0] = -1, -1
        elif blocks[0][1] == blocks[0][1]:
            blocks[0][0], blocks[1][0] = -1, 0

    while can_go:
        for block in blocks:
            row, col = block
            if row + 1 < 6:
                if GREEN[row + 1][col] == 0:
                    continue
            can_go = False
        if can_go:
            for block in blocks:
                block[0] += 1
        else:
            for block in blocks:
                GREEN[block[0]][block[1]] = 1


def move_blue(blocks):
    can_go = True
    if len(blocks) == 1:
        blocks[0][1] = -1
    else:
        if blocks[0][0] == blocks[1][0]:
            blocks[0][1], blocks[1][1] = -1, 0
        elif blocks[0][1] == blocks[1][1]:
            blocks[0][1], blocks[1][1] = -1, -1

    while can_go:
        for block in blocks:
            row, col = block
            if col + 1 < 6:
                if BLUE[row][col + 1] == 0:
                    continue
            can_go = False
        if can_go:
            for block in blocks:
                block[1] += 1
        else:
            for block in blocks:
                BLUE[block[0]][block[1]] = 1


N = int(input())
commands = []
for _ in range(N):
    t, row, col = map(int, input().split())
    if t == 1:
        commands.append([[row, col]])
    elif t == 2:
        commands.append([[row, col], [row, col + 1]])
    else:
        commands.append([[row, col], [row + 1, col]])

for command in commands:
    move_green(deepcopy(command))
    check_green_line(True)
    check_mint()

    move_blue(deepcopy(command))
    check_blue_line(True)
    check_sky()


print(point)
print(cnt())
