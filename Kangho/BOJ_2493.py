from collections import deque
N = int(input())
towers = [0]
a = list(map(int, input().split()))
towers.extend(a)
q = deque()
answer = [0] * (N+1)
for i in range(N, 0, -1):
    if not q:
        q.append((towers[i], i))
    else:
        while q and towers[i] > q[0][0]:
            _, tow_idx = q.popleft()
            answer[tow_idx] = i
        q.appendleft((towers[i], i))
print(" ".join(map(str, answer[1:])))
