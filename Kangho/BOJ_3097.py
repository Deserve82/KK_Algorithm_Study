import sys
N, M = map(int, sys.stdin.readline().split())
immigrations = []
for _ in range(N):
    immigrations.append(int(sys.stdin.readline()))
left = 0
right = immigrations[0] * M
while left < right:
    mid = (left + right) // 2
    ret = 0
    for i in immigrations:
        ret += (mid // i)
    if ret < M:
        left = mid + 1
    else:
        right = mid
print(left)
