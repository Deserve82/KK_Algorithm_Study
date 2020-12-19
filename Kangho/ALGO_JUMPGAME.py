
def jump(row, col):
    if row == m-1 and col == m-1:
        return 1
    elif row >= m or col >= m:
        return 0

    if cache[row][col] != -1:
        return cache[row][col]
    else:
        cache[row][col] = jump(row + board[row][col], col) or jump(row, col + board[row][col])
    return cache[row][col]


n = int(input())
for _ in range(n):
    m = int(input())
    board = []
    for _ in range(m):
        board.append(list(map(int, input().split())))
    cache = [[-1]*m for _ in range(m)]
    if jump(0, 0):
        print("YES")
    else:
        print("NO")

