import sys

sys.setrecursionlimit(1000000)


def dynamic(number):
    if number == 1:
        return 0
    if dp[number] != 10000001:
        return dp[number]
    if number % 3 == 0:
        dp[number] = min(dynamic(number // 3) + 1, dp[number])
    if number % 2 == 0:
        dp[number] = min(dynamic(number // 2) + 1, dp[number])
    if number % 6 != 0:
        dp[number] = min(dynamic(number - 1) + 1, dp[number])
    return dp[number]


n = int(input())
dp = [10000001] * (n + 1)
print(dynamic(n))
