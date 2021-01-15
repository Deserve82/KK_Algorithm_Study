import sys
from collections import deque
directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]]
N, M, YEAR = map(int, sys.stdin.readline().split())
board = [[5]*N for _ in range(N)]
winter_bonus = []
for _ in range(N):
    winter_bonus.append(list(map(int, sys.stdin.readline().split())))
trees = [
    [deque() for _ in range(N)] for _ in range(N)
]
tree_num = [[0]*N for _ in range(N)]
for _ in range(M):
    r, c, age = map(int, sys.stdin.readline().split())
    trees[r-1][c-1].append(age)
    tree_num[r-1][c-1] += 1

while YEAR > 0:
    summer_nutrition = []
    # 봄, 여름
    for i in range(N):
        for j in range(N):
            if tree_num[i][j] > 0:
                r, c, num = i, j, tree_num[i][j]
                if num == 0:
                    continue
                tree_len = num
                bp = num
                for k in range(tree_len):
                    if board[r][c] < trees[r][c][k]:
                        bp = k
                        break
                    else:
                        board[r][c] -= trees[r][c][k]
                        trees[r][c][k] += 1
                while bp < tree_len:
                    cannot_breed = trees[r][c].pop()
                    cannot_breed //= 2
                    board[r][c] += cannot_breed
                    bp += 1
                    tree_num[r][c] -= 1
    # 가을
    for i in range(N):
        for j in range(N):
            c = 0
            if tree_num[i][j] > 0:
                for tree in trees[i][j]:
                    if tree % 5 == 0:
                        c += 1
            if c > 0:
                for d in range(8):
                    mr = i+directions[d][0]
                    mc = j+directions[d][1]
                    if 0 <= mr < N and 0 <= mc < N:
                        for _ in range(c):
                            trees[mr][mc].appendleft(1)
                            tree_num[mr][mc] += 1

    for i in range(N):
        for j in range(N):
            board[i][j] += winter_bonus[i][j]
    YEAR -= 1
ans = 0
for a in tree_num:
    ans += sum(a)
print(ans)
