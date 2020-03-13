n = int(input())
dps = [[0 for i in range(10)] for j in range(101)]
for i in range(1, 10):
    dps[1][i] = 1
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dps[i][j] = dps[i - 1][1]
        elif j == 9:
            dps[i][j] = dps[i - 1][8]
        else:
            dps[i][j] = dps[i - 1][j - 1] + dps[i - 1][j + 1]
print(sum(dps[n]) % 1000000000)
