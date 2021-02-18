import sys

input = sys.stdin.readline


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    parent[b] = a


N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
edges = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort(key=lambda x: x[0])
total_val = 0
max_val = 0
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        total_val += cost
        if cost > max_val:
            max_val = cost
        union(a, b)
print(total_val - max_val)
