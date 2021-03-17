import sys
sys.setrecursionlimit(10**6)
d = [0]*5001


def solution(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    if n == 2:
        return 3
    if n == 3:
        return 0
    if n == 4:
        return 11
    if d[n] != 0:
        return d[n]
    else:
        b = int(n/2)
        for i in range(2, b+1):
            d[n] += 2*solution(n-2*i)
            d[n] %= 1000000007

        d[n] += 3*solution(n-2)
        d[n] %= 1000000007
        return d[n]
