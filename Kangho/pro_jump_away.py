import sys
sys.setrecursionlimit(10**6)
cache = [-1] * 3000


def dp(curr_loc, pivot):
    if curr_loc == pivot:
        return 1
    if curr_loc > pivot:
        return 0

    if cache[curr_loc] != -1:
        return cache[curr_loc]

    ret = 0
    ret += (dp(curr_loc + 1, pivot) % 1234567)
    ret += (dp(curr_loc + 2, pivot) % 1234567)
    ret %= 1234567
    cache[curr_loc] = ret
    return ret


def solution(n):
    answer = dp(0, n)
    return answer
