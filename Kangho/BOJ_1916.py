import sys
from queue import PriorityQueue


def dijkstra(start):
    d[start] = 0
    q = PriorityQueue()
    q.put((0, start))
    while not q.empty():
        bus_cost, current = q.get()
        if d[current] < bus_cost:
            continue
        for cos, goal in city[current]:
            next_goal = goal
            next_distance = d[current] + cos
            if next_distance < d[next_goal]:
                d[next_goal] = next_distance
                q.put((next_distance, next_goal))


MAX_VALUE = 100000000
city_count = int(sys.stdin.readline())
bus_count = int(sys.stdin.readline())
d = [MAX_VALUE] * (city_count+1)
city = [[] for _ in range(city_count+1)]
for _ in range(bus_count):
    s, e, cost = map(int, sys.stdin.readline().split())
    city[s].append((cost, e))
start_idx, end_idx = map(int, sys.stdin.readline().split())
d[start_idx] = 0
dijkstra(start_idx)
print(d[end_idx])
