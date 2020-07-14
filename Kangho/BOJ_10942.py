import sys

count = 0
def is_palindrom(s, e):
    while s < e:
        if numbers[s] != numbers[e]:
            return False
        s += 1
        e -= 1
    return True


n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    if is_palindrom(start-1, end-1):
        print(1)
    else:
        print(0)
