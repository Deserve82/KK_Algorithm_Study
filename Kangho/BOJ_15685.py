movements = ((0, 1), (-1, 0), (0, -1), (1, 0))


def count_square():
    s = 0
    for i in range(100):
        for j in range(100):
            if board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
                s += 1
    print(s)


def cover(gen):
    global g
    if gen == g:
        return
    tl = len(t)
    for i in range(tl-1, -1, -1):
        t.append((t[i]+1) % 4)
    cover(gen+1)


board = [[False] * 101 for _ in range(101)]
for _ in range(int(input())):
    c, r, d, g = map(int, input().split())
    board[r][c] = True
    t = [d]
    cover(0)
    for di in t:
        r += movements[di][0]
        c += movements[di][1]
        board[r][c] = True

count_square()
