n, k = map(int, input().split())
sums = [0]*(k+1)
coins = []
for _ in range(n):
    coins.append(int(input()))
sums[0] = 1
for i in range(n):
    for w in range(k+1):
        if w >= coins[i]:
            sums[w] += sums[w-coins[i]]
print(sums[k])
