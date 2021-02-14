import sys

input = sys.stdin.readline


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return
    parent[b] = a


while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break
    parent = [i for i in range(M)]
    sums_of_total = 0
    edges = []
    for _ in range(N):
        f, t, cost = map(int, input().split())
        edges.append((cost, f, t))
        sums_of_total += cost

    edges.sort()
    what_we_have = 0
    for edge in edges:
        ct, fr, to = edge
        if find(fr) != find(to):
            union(fr, to)
            what_we_have += ct
    print(sums_of_total - what_we_have)
