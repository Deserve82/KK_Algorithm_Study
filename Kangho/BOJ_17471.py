from itertools import combinations
from collections import deque
def bfs(ls):
    checker = {ls[0]}
    q = deque()
    q.append(ls[0])
    total_weight = weight[ls[0]]
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if nxt not in checker and nxt in ls:
                total_weight += weight[nxt]
                q.append(nxt)
                checker.add(nxt)
    return total_weight, len(checker)

N = int(input())
weight = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for i in range(N):
    nodes = list(map(int, input().split()))
    for node in nodes[1:]:
        graph[i].append(node-1)
answer = 1000000000
for i in range(1, N//2 + 1):
    combis = list(combinations([num for num in range(N)], i))
    for combi in combis:
        fir_w, f_nodes = bfs(combi)
        rest = []
        for k in range(N):
            if k not in combi:
                rest.append(k)
        sec_w, s_nodes = bfs(rest)
        if f_nodes + s_nodes == N:
            answer = min(answer, abs(fir_w - sec_w))
if answer == 1000000000:
    print(-1)
else:
    print(answer)
