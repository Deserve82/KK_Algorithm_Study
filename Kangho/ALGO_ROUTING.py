import sys
import heapq
for _ in range(int(input())):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V)]
    for _ in range(E):
        s, e, val = map(float, sys.stdin.readline().split())
        graph[int(s)].append((val, int(e)))
    weights = [float('inf')] * V
    weights[0] = 1
    pq = []
    heapq.heappush(pq, [1, 0])
    while pq:
        val, here = heapq.heappop(pq)
        for nxt_w, nxt_n in graph[here]:
            cost = nxt_w * weights[here]
            if weights[nxt_n] > cost:
                weights[nxt_n] = cost
                heapq.heappush(pq, [cost, nxt_n])
    print('%.10f' % weights[-1])
