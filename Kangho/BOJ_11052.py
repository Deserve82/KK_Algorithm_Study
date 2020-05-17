n = int(input())
cards = [0]
cards.extend(list(map(int, input().split())))

dp = [0] * (n+1)
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i-j]+cards[j], cards[i], dp[i])
print(dp[n])