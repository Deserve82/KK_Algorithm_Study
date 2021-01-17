import sys

sys.setrecursionlimit(1000000)


def dfs(idx):
    check[idx] = True
    for node in graph[idx]:
        if not check[node]:
            dfs(node)


V, E = map(int, input().split())
in_degree = [0] * (V + 1)
check = [False] * (V + 1)
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    in_degree[start] += 1
    in_degree[end] += 1
candidates = 0
num = 0
for i in range(1, V + 1):
    if not check[i]:
        num += 1
        dfs(i)

for i in range(1, V + 1):
    if in_degree[i] % 2 != 0:
        candidates += 1
if num == 1 and (candidates == 0 or candidates == 2):
    print("YES")
else:
    print("NO")
