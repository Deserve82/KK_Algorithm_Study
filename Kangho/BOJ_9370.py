import sys
import heapq as hq

input = sys.stdin.readline


def dijkstra(start):
    pq = []
    hq.heappush(pq, [0, start])
    distances = [10000000000000] * N
    distances[start] = 0
    while pq:
        dis, curr = hq.heappop(pq)
        for nxt, w in graph[curr]:
            if dis + w < distances[nxt]:
                distances[nxt] = dis + w
                hq.heappush(pq, (distances[nxt], nxt))
    return distances


for _ in range(int(input())):
    N, M, X = map(int, input().split())
    start, sfrom, sto = map(int, input().split())
    sfrom -= 1
    sto -= 1
    graph = [[] for _ in range(N)]
    suspcious_spot = set()
    candi_answer = set()
    for _ in range(M):
        a, b, d = map(int, input().split())
        graph[a - 1].append((b - 1, d))
        graph[b - 1].append((a - 1, d))

    for _ in range(X):
        suspcious_spot.add(int(input()))

    pivot = dijkstra(start-1)
    fs = dijkstra(sfrom)
    ts = dijkstra(sto)
    for spot in suspcious_spot:
        spot -= 1
        if pivot[sfrom] + fs[sto] + ts[spot] == pivot[spot] or pivot[sto] + ts[sfrom] + fs[spot] == pivot[spot]:
            candi_answer.add(spot+1)
    answer = list(suspcious_spot & candi_answer)
    answer.sort()
    print(" ".join(map(str, answer)))
