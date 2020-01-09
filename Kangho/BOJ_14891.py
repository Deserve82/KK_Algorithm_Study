gear = []
rotate = []
answer = 0
for i in range(4):
    gear.append(list(input()))
rotate_number = int(input())
for i in range(rotate_number):
    temp = list(map(int, input().split()))
    rotate.append(temp)


def rotating(a, dir):
    if dir == 1:
        t = a[-1]
        for i in range(len(a)-1, 0, -1):
            a[i] = a[i-1]
        a[0] = t
    else:
        t = a.pop(0)
        a.append(t)

def d(a):
    if a == 1:
        return -1
    else:
        return 1


def how_many_gear_rotate(gear):
    move = [0, 0, 0]
    for g in range(3):
        if gear[g][2] != gear[g+1][6]:
            move[g] = 1
    return move


for r in rotate:
    m = how_many_gear_rotate(gear)
    if r[0] == 1 and m[0] == 0:
        rotating(gear[0], r[1])
    elif r[0] == 1 and m[0] == 1 and m[1] == 0:
        rotating(gear[0], r[1])
        rotating(gear[1], d(r[1]))
    elif r[0] == 1 and m[0] == 1 and m[1] == 1 and m[2] == 0:
        rotating(gear[0], r[1])
        rotating(gear[1], d(r[1]))
        rotating(gear[2], r[1])
    elif r[0] == 1 and m[0] == 1 and m[1] == 1 and m[2] == 1:
        rotating(gear[0], r[1])
        rotating(gear[1], d(r[1]))
        rotating(gear[2], r[1])
        rotating(gear[3], d(r[1]))

    if r[0] == 2 and m[0] == 0 and m[1] == 0:
        rotating(gear[1], r[1])
    elif r[0] == 2 and m[0] == 0 and m[1] == 1 and m[2] == 0:
        rotating(gear[1], r[1])
        rotating(gear[2], d(r[1]))
    elif r[0] == 2 and m[0] == 0 and m[1] == 1 and m[2] == 1:
        rotating(gear[1], r[1])
        rotating(gear[2], d(r[1]))
        rotating(gear[3], r[1])
    elif r[0] == 2 and m[0] == 1 and m[1] == 0:
        rotating(gear[1], r[1])
        rotating(gear[0], d(r[1]))
    elif r[0] == 2 and m[0] == 1 and m[1] == 1 and m[2] == 0:
        rotating(gear[1], r[1])
        rotating(gear[0], d(r[1]))
        rotating(gear[2], d(r[1]))
    elif r[0] == 2 and m[0] == 1 and m[1] == 1 and m[2] == 1:
        rotating(gear[1], r[1])
        rotating(gear[0], d(r[1]))
        rotating(gear[2], d(r[1]))
        rotating(gear[3], r[1])

    if r[0] == 3 and m[2] == 0 and m[1] == 0:
        rotating(gear[2], r[1])
    elif r[0] == 3 and m[2] == 0 and m[1] == 1 and m[0] == 0:
        rotating(gear[2], r[1])
        rotating(gear[1], d(r[1]))
    elif r[0] == 3 and m[2] == 0 and m[1] == 1 and m[0] == 1:
        rotating(gear[2], r[1])
        rotating(gear[1], d(r[1]))
        rotating(gear[0], r[1])
    elif r[0] == 3 and m[2] == 1 and m[1] == 0:
        rotating(gear[2], r[1])
        rotating(gear[3], d(r[1]))
    elif r[0] == 3 and m[2] == 1 and m[1] == 1 and m[0] == 0:
        rotating(gear[2], r[1])
        rotating(gear[1], d(r[1]))
        rotating(gear[3], d(r[1]))
    elif r[0] == 3 and m[2] == 1 and m[1] == 1 and m[0] == 1:
        rotating(gear[2], r[1])
        rotating(gear[1], d(r[1]))
        rotating(gear[3], d(r[1]))
        rotating(gear[0], r[1])

    if r[0] == 4 and m[2] == 0:
        rotating(gear[3], r[1])
    elif r[0] == 4 and m[2] == 1 and m[1] == 0:
        rotating(gear[3], r[1])
        rotating(gear[2], d(r[1]))
    elif r[0] == 4 and m[2] == 1 and m[1] == 1 and m[0] == 0:
        rotating(gear[3], r[1])
        rotating(gear[2], d(r[1]))
        rotating(gear[1], r[1])
    elif r[0] == 4 and m[0] == 1 and m[1] == 1 and m[2] == 1:
        rotating(gear[3], r[1])
        rotating(gear[2], d(r[1]))
        rotating(gear[1], r[1])
        rotating(gear[0], d(r[1]))

if gear[0][0] == '1':
    answer += 1
if gear[1][0] == '1':
    answer += 2
if gear[2][0] == '1':
    answer += 4
if gear[3][0] == '1':
    answer += 8

print(answer)