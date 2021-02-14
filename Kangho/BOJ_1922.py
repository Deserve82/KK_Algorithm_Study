import sys

input = sys.stdin.readline


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = parent[a]
    b = parent[b]
    if a == b:
        return
    parent[a] = b


N = int(input())
M = int(input())
parent = [i for i in range(N)]
edges = []
for _ in range(M):
    r, c, w = map(int, input().split())
    edges.append((w, r - 1, c - 1))
edges.sort()
total_val = 0
for edge in edges:
    cost, f, t = edge
    if find(f) != find(t):
        union(f, t)
        total_val += cost
print(total_val)
