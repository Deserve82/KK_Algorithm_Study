import sys


def dfs(start):
    global pivot_v, min_v, count, first_start
    if count == 0:
        first_start = start
        checker[start] = True
    elif count == n-1:
        if pivot_v + board[start][first_start] < min_v and board[start][first_start] != 0:
            min_v = pivot_v + board[start][first_start]
            return
        else:
            return
    for i, next_t in enumerate(board[start]):
        if next_t != 0 and not checker[i]:
            pivot_v += next_t
            count += 1
            checker[i] = True
            dfs(i)
            count -= 1
            pivot_v -= next_t
            checker[i] = False


n = int(input())
first_start = 0
pivot_v = 0
min_v = sys.maxsize - 1
count = 0
board = []
checker = [False] * n
for _ in range(n):
    board.append(list(map(int, input().split())))
for j in range(n):
    dfs(j)
print(min_v)
