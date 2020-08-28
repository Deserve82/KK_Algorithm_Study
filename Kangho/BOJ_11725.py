import sys


def dfs(n):
    pivots = [0]
    while pivots:
        pivot = pivots.pop()
        for child in board[pivot]:
            if visited[child-1] == 0:
                pivots.append(child-1)
                answers[child-1] = pivot + 1
        visited[pivot] = 1


n = int(sys.stdin.readline())
board = [[] for _ in range(n)]
answers = [0] * n
visited = [0] * n
visited[0] = 1
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    board[b - 1].append(a)
    board[a - 1].append(b)
dfs(n)
for i in range(1, n):
    print(answers[i])
