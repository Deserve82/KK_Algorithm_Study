import sys
from queue import PriorityQueue


def dijkstra(start, ret_val):
    d = [MAX_VAL] * (v + 1)
    d[start] = 0
    q = PriorityQueue()
    q.put((0, start))
    while not q.empty():
        cost, current = q.get()
        for next_cost, next_idx in a[current]:
            if d[current] < cost:
                continue
            else:
                if d[next_idx] > next_cost + d[current]:
                    d[next_idx] = next_cost + d[current]
                    q.put((next_cost, next_idx))
    return d[ret_val]


MAX_VAL = 100000000
v, e = map(int, sys.stdin.readline().split())
a = [[] for _ in range(v + 1)]
for _ in range(e):
    s, e, c = map(int, sys.stdin.readline().split())
    a[s].append((c, e))
    a[e].append((c, s))
first_goal, second_goal = map(int, sys.stdin.readline().split())
fi = dijkstra(1, first_goal)
se = dijkstra(first_goal, second_goal)
th = dijkstra(second_goal, v)
if fi == MAX_VAL or se == MAX_VAL or th == MAX_VAL:
    print(-1)
else:
    answer = (fi+se+th)
    tho_da_ruen = dijkstra(1,second_goal) + dijkstra(second_goal, first_goal) + dijkstra(first_goal, v)
    if tho_da_ruen < answer:
        print(tho_da_ruen)
    else:
        print(answer)
