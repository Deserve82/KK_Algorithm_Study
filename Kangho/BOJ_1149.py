n = int(input())
field = []
for _ in range(n):
    field.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(3):
        if j == 0:
            field[i][j] += min(field[i-1][1], field[i-1][2])
        elif j == 1:
            field[i][j] += min(field[i - 1][0], field[i - 1][2])
        else:
            field[i][j] += min(field[i - 1][0], field[i - 1][1])

print(min(field[n-1]))