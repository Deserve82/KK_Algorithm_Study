import sys
sys.setrecursionlimit(10**6)
movement = [(0, 1), (1, 0), (-1, 0), (0, -1)]
R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(map(int, input().split())))
cache = [[-1] * C for _ in range(R)]
answer = 0


def dfs(row, col):
    if row == R-1 and col == C-1:
        return 1
    if cache[row][col] != -1:
        return cache[row][col]

    curr = board[row][col]
    ret = 0
    for r, c in movement:
        mr, mc = row + r, col + c
        if 0 <= mr < R and 0 <= mc < C:
            if curr > board[mr][mc]:
                ret += dfs(mr, mc)

    cache[row][col] = ret
    return cache[row][col]


print(dfs(0, 0))
