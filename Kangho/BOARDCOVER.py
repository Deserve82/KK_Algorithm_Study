import sys
sys.setrecursionlimit(10000)

blocks = [((0, 0), (0, 1), (1, 1)),
          ((0, 0), (1, 0), (1, 1)),
          ((0, 0), (1, 0), (0, 1)),
          ((0, 0), (1, 0), (1, -1))]


def check_all():
    global r, c
    for i in range(r):
        for j in range(c):
            if board[i][j] == 0:
                return False
    return True


def check_block():
    global r, c, count
    if check_all():
        count += 1
    for i in range(r):
        for j in range(c):
            if board[i][j] == 0:
                for block in blocks:
                    f = False
                    for a, b in block:
                        if -1 < i + a < r and -1 < j + b < c:
                            if board[i + a][j + b] == 0:
                                continue
                            else:
                                f = True
                        else:
                            f = True
                    if not f:
                        for a, b in block:
                            board[i+a][j+b] = 1
                        check_block()
                        for a, b in block:
                            board[i+a][j+b] = 0
                    else:
                        continue
                if board[i][j] == 0:
                    return


n = int(input())
for _ in range(n):
    count = 0
    dot_counter = 0
    r, c = map(int, input().split())
    board = [[0] * c for _ in range(r)]
    for i in range(r):
        sen = input()
        for j in range(c):
            if sen[j] == '#':
                board[i][j] = 1
            else:
                dot_counter += 1
    if dot_counter % 3 != 0:
        print(0)
    else:
        check_block()
        print(count)
