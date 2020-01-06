size = int(input())
noa = int(input())
loa = []
for i in range(noa):
    loa.append(list(map(int, input().split())))
movenum = int(input())
smove = []
for i in range(movenum):
    smove.append(list(map(str, input().split())))

F = [[0 for i in range(size)] for j in range(size)]

"""
  3
2   0
  1 
"""

direction = 0
for i in loa:
    F[i[0]-1][i[1]-1] = -1
count = 0
snake = [0, 0]
snake_body = []
idx = 0
while True:
    if idx < len(smove):
        if int(smove[idx][0]) == count:
            if smove[idx][1] == 'D':
                direction += 1
                if direction > 3:
                    direction = 0
            else:
                direction -= 1
                if direction < 0:
                    direction = 3
            idx += 1

    bf = 0
    count += 1

    if direction == 0:
        snake[1] += 1
        if snake[1] >= size:
            bf = 1
            break

    elif direction == 1:
        snake[0] += 1
        if snake[0] >= size:
            bf = 1
            break

    elif direction == 2:
        snake[1] -= 1
        if snake[1] < 0:
            bf = 1
            break

    elif direction == 3:
        snake[0] -= 1
        if snake[0] < 0:
            bf = 1
            break

    if snake in snake_body:
        bf = 1
    if direction == 0:
        snake_body.append([snake[0], snake[1]-1])
    elif direction == 1:
        snake_body.append([snake[0]-1, snake[1]])
    elif direction == 2:
        snake_body.append([snake[0], snake[1]+1])
    elif direction == 3:
        snake_body.append([snake[0]+1, snake[1]])
    if F[snake[0]][snake[1]] == -1:
        F[snake[0]][snake[1]] = 0
    else:
        snake_body.pop(0)

    if bf == 1:
        break

print(count)