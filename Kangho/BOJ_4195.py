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
    size[a] += size[b]


for _ in range(int(input())):
    N = int(input())
    parent = {}
    size = {}
    for _ in range(N):
        first, second = input().split()

        if first not in parent:
            parent[first] = first
            size[first] = 1

        if second not in parent:
            parent[second] = second
            size[second] = 1

        union(first, second)
        print(size[find(first)])
