from queue import PriorityQueue
import sys

input = sys.stdin.readline


def dijkstra(c, n, roads):
    Q.put((0, c))
    wn = [100001] * (n + 1)
    wn[c] = 0
    while not Q.empty():
        snode = Q.get()
        for i in range(n + 1):
            if roads[snode[1]][i] != 0:
                q = roads[snode[1]][i] + wn[snode[1]]
                if wn[i] > q:
                    Q.put((q, i))
                    wn[i] = q
    return wn


Q = PriorityQueue()
n, m, c = map(int, input().split())
roads = [[0] * (n + 1) for _ in range(n + 1)]
back_to_home_roads = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    roads[s][e] = w
    back_to_home_roads[e][s] = w
first_ls = dijkstra(c, n, roads)
secend_ls = dijkstra(c, n, back_to_home_roads)
m_val = 0
for i in range(1, n + 1):
    t = first_ls[i] + secend_ls[i]
    if m_val < t:
        m_val = t
print(m_val)
