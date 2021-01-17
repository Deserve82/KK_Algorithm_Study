def move(gear_num, is_clockwise):
    if is_clockwise:
        gears[gear_num] = gears[gear_num][-1] + gears[gear_num][:-1]
    else:
        gears[gear_num] = gears[gear_num][1:] + gears[gear_num][0]


def where_rotate(start, is_cloclwise):
    should_rotate = []
    t = start
    tc = is_cloclwise
    while t > 0:
        if gears[t][6] != gears[t-1][2]:
            should_rotate.append([t - 1, not tc])
            tc = not tc
            t -= 1
        else:
            break
    t = start
    tc = is_cloclwise
    while t < 3:
        if gears[t][2] != gears[t+1][6]:
            should_rotate.append([t + 1, not tc])
            tc = not tc
            t += 1
        else:
            break
    return should_rotate


gears = []
for _ in range(4):
    gears.append(input())
N = int(input())
commands = []
for _ in range(N):
    a, b = map(int, input().split())
    commands.append([a-1, b])
for g, c in commands:
    if c == 1:
        sr = where_rotate(g, True)
        move(g, True)
        for s in sr:
            move(s[0], s[1])
    else:
        sr = where_rotate(g, False)
        move(g, False)
        for s in sr:
            move(s[0], s[1])
points = [1, 2, 4, 8]
ans = 0
for i in range(4):
    if gears[i][0] == '1':
        ans += points[i]
    else:
        continue
print(ans)
