import sys
sys.setrecursionlimit(10**6)
MOD = 1000000007


def dp(curr_loc, time):
    if time == D:
        if curr_loc == 0:
            return 1
        else:
            return 0
    if cache[curr_loc][time] != -1:
        return cache[curr_loc][time]
    ret = 0
    for node in s[curr_loc]:
        ret += dp(node, time + 1)
        ret %= MOD
    cache[curr_loc][time] = ret
    return ret


D = int(input())
s = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4, 5], [2, 3, 5, 6], [3, 4, 7], [4, 7], [5, 6]]
cache = [[-1] * (D + 1) for _ in range(8)]
print(dp(0, 0))
