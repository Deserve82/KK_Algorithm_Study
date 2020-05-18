n, lot = map(int, input().split())
dp = [1]*201
dp2 = [1]*201
for i in range(int(lot/2)):
    for j in range(1, 201):
        dp[j] = (dp[j-1] % 1000000000 + dp2[j] % 1000000000) % 1000000000
    for k in range(1, 201):
        dp2[k] = (dp2[k-1] % 1000000000 + dp[k] % 1000000000) % 1000000000
if lot % 2 == 0:
    print(dp[n] % 1000000000)
else:
    print(dp2[n] % 1000000000)
