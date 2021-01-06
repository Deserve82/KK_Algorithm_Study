import sys
import heapq as hq

INF = 987654321
for _ in range(int(input())):
    G, V, N, M = map(int, sys.stdin.readline().split())
    board = [[] for _ in range(G+1)]
    answers = [INF] * (G+1)
    for _ in range(V):
        s, e, w = map(int, sys.stdin.readline().split())
        board[s].append((w, e))
        board[e].append((w, s))

    fire_spots = list(map(int, sys.stdin.readline().split()))
    fire_stations = list(map(int, sys.stdin.readline().split()))

    for fire_station in fire_stations:
        check = [False] * (G + 1)
        pq = []
        answers[fire_station] = 0
        hq.heappush(pq, (0, fire_station))
        while pq:
            here_weight,  here = hq.heappop(pq)
            for next_weight, next_node in board[here]:
                cost = here_weight + next_weight
                if cost < answers[next_node] and not check[next_node]:
                    answers[next_node] = cost
                    hq.heappush(pq, (cost, next_node))
            check[here] = True

    cs = 0
    for fire_spot in fire_spots:
        cs += answers[fire_spot]
    print(cs)
