import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
move = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def dp(row, col):
    if 0 <= row < N and 0 <= col < N:
        if cache[row][col] != -1:
            return cache[row][col]

        ret = 0
        for ri, ci in move:
            mr, mc = row + ri, col + ci
            if 0 <= mr < N and 0 <= mc < N:
                if board[row][col] < board[mr][mc]:
                    ret = max(ret, dp(mr, mc) + 1)
        cache[row][col] = ret
        return ret
    else:
        return 0


N = int(input())
board = []
cache = [[-1] * N for _ in range(N)]
for _ in range(N):
    board.append(list(map(int, input().split())))
answer = 0
for i in range(N):
    for j in range(N):
        answer = max(answer, dp(i, j))
print(answer+1)
