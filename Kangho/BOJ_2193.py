n = int(input())
dp = [0]*100
dp[1] = 1
dp[2] = 1


def pibo(idx):
    if dp[idx] != 0:
        return dp[idx]
    else:
        dp[idx] = pibo(idx-1) + pibo(idx-2)
        return dp[idx]


print(pibo(n))