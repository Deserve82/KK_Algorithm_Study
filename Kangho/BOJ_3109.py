movements = [(-1, 1), (0, 1), (1, 1)]


def re_dfs(x, y):
    checker[x][y] = True
    if y == C - 1:
        return 1
    for move_row, move_col in movements:
        mr, mc = move_row + x, move_col + y
        if 0 <= mr < R and 0 <= mc < C:
            if not checker[mr][mc] and board[mr][mc] == '.':
                v = re_dfs(mr, mc)
                if v:
                    return v
    return 0


R, C = map(int, input().split())
board = []
checker = [[False] * C for _ in range(R)]
answer = 0
wrong_answer = 0
for _ in range(R):
    board.append(list(input()))
for i in range(R):
    answer += re_dfs(i, 0)
print(answer)
