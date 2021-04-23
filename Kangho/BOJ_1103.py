import sys

sys.setrecursionlimit(10 ** 6)
movements = [[0, 1], [1, 0], [-1, 0], [0, -1]]
loop_flag = False


def dp(r, c):
    global loop_flag
    if 0 <= r < R and 0 <= c < C and not loop_flag:
        jump = board[r][c]
        if jump == "H":
            return 0
        if cache[r][c] != -1:
            return cache[r][c]
        if visited[r][c]:
            loop_flag = True
            return 0

        visited[r][c] = True
        ret = 0
        jump = int(jump)
        for rj, cj in movements:
            mr, mc = r + rj * jump, c + cj * jump
            if 0 <= mr < R and 0 <= mc < C:
                if board[mr][mc] != "H":
                    ret = max(dp(mr, mc) + 1, ret)
        cache[r][c] = ret
        return ret
    else:
        return 0


R, C = map(int, input().split())
cache = [[-1] * C for _ in range(R)]
board = []
visited = [[False] * C for _ in range(R)]
for _ in range(R):
    board.append(list(input()))
answer = dp(0, 0)
if loop_flag:
    print(-1)
else:
    print(answer + 1)
