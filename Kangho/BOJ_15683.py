movements = (
    # 1번 카메라
    ((-1, 0), (0, 1), (1, 0), (0, -1)),
    # 2번 카메라
    (("r", 0), (0, "c")),
    # 3번 카메라
    ((-1, 1), (1, 1), (1, -1), (-1, -1)),
    # 4번 카메라
    ((-1, "c"), ("r", 1), (1, "c"), ("r", -1)),
    # 5번 카메라
    [("r", "c")]
)


def check():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if count_board[i][j] > 0:
                cnt += 1
    return N*M - cnt


def cover(r, c, index, zero_or_sharp):
    row, col = index
    t = row
    if r == "r":
        for i in range(row, N):
            if count_board[i][col] == 10000:
                break
            if board[i][col] == 0:
                count_board[i][col] += zero_or_sharp
        for i in range(row, -1, -1):
            if count_board[i][col] == 10000:
                break
            if board[i][col] == 0:
                count_board[i][col] += zero_or_sharp
    else:
        while 0 <= row < N:
            if count_board[row][col] == 10000 or r == 0:
                break
            if board[row][col] == 0:
                count_board[row][col] += zero_or_sharp
            row += r
    row = t
    if c == "c":
        for i in range(col, M):
            if count_board[row][i] == 10000:
                break
            if board[row][i] == 0:
                count_board[row][i] += zero_or_sharp
        for i in range(col, -1, -1):
            if count_board[row][i] == 10000:
                break
            if board[row][i] == 0:
                count_board[row][i] += zero_or_sharp
    else:
        while 0 <= col < M:
            if count_board[row][col] == 10000 or c == 0:
                break
            if board[row][col] == 0:
                count_board[row][col] += zero_or_sharp
            col += c


def solve(spot_idx):
    global groovy_area
    if spot_idx >= return_num:
        groovy_area = min(groovy_area, check())
        return

    row, col = spots[spot_idx]
    how_to_move = movements[board[row][col]-1]
    for r, c in how_to_move:
        cover(r, c, (row, col), 1)
        solve(spot_idx + 1)
        cover(r, c, (row, col), -1)


N, M = map(int, input().split())
groovy_area = N * M
count_board = [[0] * M for _ in range(N)]
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
spots = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 6:
            count_board[i][j] = 10000
        elif board[i][j] != 0:
            spots.append((i, j))
            count_board[i][j] = board[i][j]
return_num = len(spots)
solve(0)
print(groovy_area)
