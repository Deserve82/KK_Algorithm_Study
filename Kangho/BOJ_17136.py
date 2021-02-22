def is_complete():
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                return False
    return True


def is_oversize(row, col, size):
    if row + size > 10 or col + size > 10:
        return -1, -1
    for i in range(row, row + size):
        for j in range(col, col + size):
            if board[i][j] == 0:
                return -1, -1
    return row, col


def cover(row, col, size, is_back):
    for i in range(row, row + size):
        for j in range(col, col + size):
            if is_back:
                board[i][j] = 1
            else:
                board[i][j] = 0


def brute(cnt):
    global answer
    if answer <= cnt:
        return

    if is_complete():
        answer = min(answer, cnt)
        return

    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                for s in range(5, 0, -1):
                    a, b = is_oversize(i, j, s)
                    if a != -1 and b != -1 and left_papers[s-1] > 0:
                        cover(i, j, s, False)
                        left_papers[s-1] -= 1
                        brute(cnt + 1)
                        cover(i, j, s, True)
                        left_papers[s-1] += 1
                return


board = []
for _ in range(10):
    board.append(list(map(int, input().split())))
left_papers = [5, 5, 5, 5, 5]
answer = 26
brute(0)
if answer >= 26:
    print(-1)
else:
    print(answer)
