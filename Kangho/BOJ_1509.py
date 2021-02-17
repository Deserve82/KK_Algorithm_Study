import sys

sys.setrecursionlimit(10**6)


def is_palindrome(start, end):
    if start >= end:
        return 1

    if cache[start][end] != -1:
        return cache[start][end]

    if s[start] == s[end]:
        cache[start][end] = is_palindrome(start + 1, end - 1)
    else:
        cache[start][end] = 0
    return cache[start][end]


def get_min_val(pos):
    if pos >= ls:
        return 0
    if dp[pos] != -1:
        return dp[pos]

    ret = ls
    for i in range(ls):
        if cache[pos][i] == 1:
            ret = min(ret, 1 + get_min_val(i+1))
    dp[pos] = ret
    return ret


s = input()
ls = len(s)
cache = [[-1] * ls for _ in range(ls)]
for i in range(ls):
    for j in range(i, ls):
        cache[i][j] = is_palindrome(i, j)
dp = [-1] * ls
print(get_min_val(0))
