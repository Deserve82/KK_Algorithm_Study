import sys
sys.setrecursionlimit(10**6)
cache = []


def dp(curr, n, vals):
    if curr >= n:
        return 0
    if cache[curr] != -1:
        return cache[curr]
    ret = max(dp(curr + 2, n, vals) + vals[curr], dp(curr + 1, n, vals))
    cache[curr] = ret
    return ret


def solution(sticker):
    global cache
    ls = len(sticker)
    cache = [-1] * (ls+1)
    answer = dp(1, ls, sticker)
    cache = [-1] * (ls+1)
    answer = max(answer, dp(2, ls - 1, sticker) + sticker[0])
    return answer
