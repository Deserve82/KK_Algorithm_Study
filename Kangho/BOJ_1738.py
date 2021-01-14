from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
r = [[] for _ in range(N)]
weights = [1e9] * N
prev = [0] * N
for _ in range(M):
    s, e, val = map(int, input().split())
    graph[s-1].append([e-1, -val])
    r[e-1].append(s-1)


visited = [False] * N
q = deque()
q.append(N-1)
visited[N-1] = True
while q:
    here = q.popleft()
    for nxt in r[here]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)

weights[0] = 0
is_cycle = False
for i in range(N):
    for j in range(N):
        for next_node, next_weight in graph[j]:
            cost = weights[j] + next_weight
            if weights[next_node] > cost:
                weights[next_node] = cost
                prev[next_node] = j+1
                if i == N-1 and visited[next_node]:
                    is_cycle = True

if is_cycle:
    print("-1")
else:
    ans = []
    idx = N
    while True:
        ans.append(idx)
        if idx == 1:
            break
        else:
            idx = prev[idx-1]
    ans.reverse()
    print(" ".join(map(str, ans)))
