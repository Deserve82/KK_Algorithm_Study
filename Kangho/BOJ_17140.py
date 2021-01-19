r, c, k = map(int, input().split())
board = [[0] * 100 for _ in range(100)]
arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))
for i in range(3):
    for j in range(3):
        board[i][j] = arr[i][j]
R, C = 3, 3
time = 0
while time <= 100 and board[r-1][c-1] != k:
    checker = {}
    if R >= C:
        for i in range(R):
            for j in range(C):
                if board[i][j] != 0:
                    if board[i][j] in checker:
                        checker[board[i][j]] += 1
                    else:
                        checker[board[i][j]] = 1
            checker = sorted(checker.items())
            checker = sorted(checker, key=lambda x: x[1])
            idx = 0
            for num, cnt in checker:
                board[i][idx] = num
                board[i][idx+1] = cnt
                idx += 2
            for d in range(idx, 100):
                if board[i][d] != 0:
                    board[i][d] = 0
            C = max(idx, C)
            checker = {}
    else:
        for j in range(C):
            for i in range(R):
                if board[i][j] != 0:
                    if board[i][j] in checker:
                        checker[board[i][j]] += 1
                    else:
                        checker[board[i][j]] = 1
            checker = sorted(checker.items())
            checker = sorted(checker, key=lambda x: x[1])
            idx = 0
            for num, cnt in checker:
                board[idx][j] = num
                board[idx+1][j] = cnt
                idx += 2
            for d in range(idx, 100):
                if board[d][j] != 0:
                    board[d][j] = 0
            R = max(idx, R)
            checker = {}
    time += 1
if time >= 101:
    print(-1)
else:
    print(time)
