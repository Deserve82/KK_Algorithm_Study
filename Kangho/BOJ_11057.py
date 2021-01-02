import sys
sys.setrecursionlimit(10000)
MOD = 10007


def hill_num(idx):
    if sum_dp[idx] != 0:
        return sum_dp[idx]

    sums = 0
    prev_sum = hill_num(idx-1)
    for i in range(10):
        tmp = curr_dp[i]
        curr_dp[i] = prev_sum
        prev_sum = curr_dp[i] - tmp
    for i in range(10):
        sums += curr_dp[i]
        sums %= MOD
    sum_dp[idx] = sums % MOD
    return sum_dp[idx]


n = int(input())
curr_dp = [1] * 10
sum_dp = [0] * 1001
sum_dp[0] = 10
print(hill_num(n-1))
