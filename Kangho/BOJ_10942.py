import sys
sys.setrecursionlimit(100000)


def is_palindrome(start, end):
    if start >= end:
        return 1

    if cache[start][end] != -1:
        return cache[start][end]

    if numbers[start] == numbers[end]:
        cache[start][end] = is_palindrome(start+1, end-1)
    else:
        cache[start][end] = 0
    return cache[start][end]


N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
cache = [[-1]*N for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(is_palindrome(a-1, b-1))
