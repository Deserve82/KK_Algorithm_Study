import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())
G = [{} for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int, input().split())
    if v in G[u]:
        G[u][v] = min(G[u][v], w)
    else:
        G[u][v] = w

def dji(G, start):
    prev = [-1]*(len(G)+1)
    dist = [INF]*(len(G)+1)
    dist[start] = 0

    priority_queue = []
    heapq.heappush(priority_queue, [0, start])

    while priority_queue:
        current_dist, here = heapq.heappop(priority_queue)

        for there, length in G[here].items():
            next_dist = dist[here] + length

            if next_dist < dist[there]:
                dist[there] = next_dist
                prev[there] = here
                heapq.heappush(priority_queue, [next_dist, there])
    return dist, prev


dist, prev = dji(G, start)
for i in dist[1:]:
    print(i if i != INF else "INF")