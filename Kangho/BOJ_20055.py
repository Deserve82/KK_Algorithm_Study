from collections import deque

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robots = []
broken = 0
time = 0
while broken < K:
    belt.rotate(1)
    # rotation
    lr = len(robots)
    for i in range(lr-1, -1, -1):
        robots[i] += 1
        if robots[i] == N-1:
            robots.pop()

    lr = len(robots)
    # move themselves
    for i in range(lr-1, -1, -1):
        if robots[i] + 1 <= N - 1:
            if belt[robots[i] + 1] > 0 and robots[i] + 1 not in robots:
                robots[i] += 1
                belt[robots[i]] -= 1
                if belt[robots[i]] == 0:
                    broken += 1
                if robots[i] == N-1:
                    robots.pop()

    if robots and belt[0] > 0:
        if robots[0] != 0:
            belt[0] -= 1
            if belt[0] == 0:
                broken += 1
            robots.insert(0, 0)
    elif not robots and belt[0] > 0:
        belt[0] -= 1
        if belt[0] == 0:
            broken += 1
        robots.insert(0, 0)
    time += 1
print(time)
