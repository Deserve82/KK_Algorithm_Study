import sys
import heapq as hq
input = sys.stdin.readline
N, M, K, S = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

pq = [(0, S)]
distance = [float('inf')] * (N+1)
check = [False] * (N+1)
distance[S] = 0
check[S] = True
while pq:
    dis, curr = hq.heappop(pq)
    for nxt in graph[curr]:
        if not check[nxt] and distance[nxt] > dis+1:
            hq.heappush(pq, (dis + 1, nxt))
            distance[nxt] = dis+1
            check[nxt] = True
answer = []
for i, d in enumerate(distance):
    if d == K:
        answer.append(i)
if not answer:
    print(-1)
else:
    for a in answer:
        print(a)
