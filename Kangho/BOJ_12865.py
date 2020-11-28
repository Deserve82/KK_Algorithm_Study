import sys
n, k = map(int, sys.stdin.readline().split())
weight = []
value = []
dp = [[0]*(k+1) for _ in range(n+1)]
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    weight.append(w)
    value.append(v)

for i in range(n):
    for w in range(1, k+1):
        if w >= weight[i]:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i])
        else:
            dp[i][w] = dp[i-1][w]
print(dp[n-1][k])
