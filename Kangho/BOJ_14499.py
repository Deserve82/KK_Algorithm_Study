def move(cc):
    if cc == 1:
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]
    elif cc == 2:
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]
    elif cc == 3:
        t = dice[3][1]
        for i in range(2, -1, -1):
            dice[i + 1][1] = dice[i][1]
        dice[0][1] = t
    else:
        t = dice[0][1]
        for i in range(1, 4):
            dice[i - 1][1] = dice[i][1]
        dice[3][1] = t


directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

dice = [
    [-1, 0, -1],
    [0,  0,  0],
    [-1, 0, -1],
    [-1, 0, -1],
]
board = []
N, M, r, c, K = map(int, input().split())
for _ in range(N):
    board.append(list(map(int, input().split())))
commands = list(map(int, input().split()))

for command in commands:
    if 0 <= r + directions[command-1][0] < N and 0 <= c + directions[command-1][1] < M:
        move(command)
        r = r + directions[command-1][0]
        c = c + directions[command-1][1]
        if board[r][c] == 0:
            board[r][c] = dice[3][1]
        else:
            dice[3][1] = board[r][c]
            board[r][c] = 0
        print(dice[1][1])
