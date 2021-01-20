from collections import deque
for _ in range(int(input())):
    N = int(input())
    answer = 0
    russia = deque(list(map(int, input().split())))
    korea = deque(list(map(int, input().split())))
    while russia:
        rv = russia.popleft()
        min_gap = 5000
        idx = -1
        for i, k in enumerate(korea):
            if rv <= k and min_gap > k - rv:
                min_gap = k - rv
                idx = i
        if min_gap == 5000 and idx == -1:
            korea.remove(min(korea))
        else:
            del korea[idx]
            answer += 1
    print(answer)
