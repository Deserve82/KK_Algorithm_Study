import sys

sys.setrecursionlimit(10 ** 9)

N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]
check = [False] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)


def DFS(curr):
    check[curr] = True
    dp[curr][0] = 0
    dp[curr][1] = 1
    for nxt in tree[curr]:
        if not check[nxt]:
            DFS(nxt)
            dp[curr][0] += max(dp[nxt][0], dp[nxt][1])
            dp[curr][1] += dp[nxt][0]

DFS(1)
print(N - max(dp[1][1], dp[1][0]))
