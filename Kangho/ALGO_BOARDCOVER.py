answer = 0
blocks = [((0, 1), (1, 1)),
          ((1, 0), (1, 1)),
          ((1, 0), (0, 1)),
          ((1, 0), (1, -1))]


def check():
    for i in range(row_len):
        for j in range(col_len):
            if b[i][j] == '.':
                return False
    return True


def bf():
    global answer
    if check():
        answer += 1
    for i in range(row_len):
        for j in range(col_len):
            if b[i][j] == ".":
                for block in blocks:
                    bi, bi2 = i + block[0][0], i + block[1][0]
                    cj, cj2 = j + block[0][1], j + block[1][1]
                    if -1 < bi < row_len and -1 < bi2 < row_len and -1 < cj < col_len and -1 < cj2 < col_len:
                        if b[bi][cj] == "." and b[bi2][cj2] == ".":
                            b[i][j], b[bi][cj], b[bi2][cj2] = "#", "#", "#"
                            bf()
                            b[i][j], b[bi][cj], b[bi2][cj2] = ".", ".", "."
                return


n = int(input())
for _ in range(n):
    b = []
    row_len, col_len = map(int, input().split())
    for _ in range(row_len):
        b.append(list(input().rstrip()))
    bf()
    print(answer)
    answer = 0
