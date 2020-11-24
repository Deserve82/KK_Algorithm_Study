from queue import PriorityQueue
import sys
sys.setrecursionlimit(1000000000)
v, e = map(int, sys.stdin.readline().split())
vert_time = PriorityQueue()
check = [False] * (v + 1)
edges = [[] for _ in range(e + 1)]
reversed_edges = [[] for _ in range(e + 1)]
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)
    reversed_edges[b].append(a)
time = 0
answer = []


def dfs_with_time(starting_point):
    global time
    time += 1
    for edge in edges[starting_point]:
        if not check[edge]:
            check[edge] = True
            dfs_with_time(edge)
    time += 1
    vert_time.put((-time, starting_point))


def dfs(s):
    basket = []
    q = [s]
    check[s] = True
    while q:
        sp = q.pop()
        basket.append(sp)
        for edge in reversed_edges[sp]:
            if not check[edge]:
                check[edge] = True
                q.append(edge)
    basket.sort()
    return basket


for i in range(1, v + 1):
    if not check[i]:
        check[i] = True
        dfs_with_time(i)

for i in range(v + 1):
    check[i] = False

while not vert_time.empty():
    node = vert_time.get()[1]
    if not check[node]:
        answer.append(dfs(node))

answer.sort()
print(len(answer))
for a in answer:
    print(" ".join(map(str, a)) + " -1")
