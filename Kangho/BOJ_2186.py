def find(r, c, pivot_idx):
    global pl
    if pivot_idx >= pl-1:
        return 1
    if cache[r][c][pivot_idx] != -1:
        return cache[r][c][pivot_idx]
    ret = 0
    for i in range(1, K+1):
        if r + i < N:
            if pivot[pivot_idx + 1] == board[r+i][c]:
                ret += find(r+i, c, pivot_idx + 1)
        if r - i >= 0:
            if pivot[pivot_idx + 1] == board[r-i][c]:
                ret += find(r-i, c, pivot_idx + 1)
    for j in range(1, K+1):
        if c + j < M:
            if pivot[pivot_idx + 1] == board[r][c+j]:
                ret += find(r, c+j, pivot_idx + 1)
        if c - j >= 0:
            if pivot[pivot_idx + 1] == board[r][c-j]:
                ret += find(r, c-j, pivot_idx + 1)
    cache[r][c][pivot_idx] = ret
    return ret


N, M, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input()))
pivot = list(input())
pl = len(pivot)
cache = [[[-1]*pl for _ in range(M)] for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == pivot[0]:
            ans += find(i, j, 0)
print(ans)
