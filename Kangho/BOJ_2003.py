import sys
n, goal = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
s, e = 0, 0
count = 0
w = 0
while s <= e and s < n:
    if w == goal:
        count += 1
        w -= numbers[s]
        s += 1
    elif w < goal and e < n:
        w += numbers[e]
        e += 1
    else:
        w -= numbers[s]
        s += 1
print(count)
