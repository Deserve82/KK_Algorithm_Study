def partial_sum(row1, col1, row2, col2):
    a = cache[row2][col2]
    if row1 > 0:
        a -= cache[row1-1][col2]
    if col1 > 0:
        a -= cache[row2][col1-1]
    if row1 > 0 and col1 > 0:
        a += cache[row1-1][col1-1]
    return a


R, C = map(int, input().split())
board = []
cache = [[0] * C for _ in range(R)]
for _ in range(R):
    board.append(list(map(int, input().split())))

for i in range(R):
    for j in range(C):
        if i == 0 and j == 0:
            cache[i][j] = board[i][j]
        elif i == 0:
            cache[i][j] += cache[i][j - 1] + board[i][j]
        elif j == 0:
            cache[i][j] += cache[i - 1][j] + board[i][j]
        else:
            cache[i][j] += cache[i - 1][j] + (cache[i][j - 1] - cache[i - 1][j - 1]) + board[i][j]

answer = -10000
for r1 in range(R):
    for c1 in range(C):
        for r2 in range(r1, R):
            for c2 in range(c1, C):
                answer = max(answer, partial_sum(r1, c1, r2, c2))
print(answer)
