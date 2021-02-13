import sys

input = sys.stdin.readline


def find(a):
    if p[a] == a:
        return a
    p[a] = find(p[a])
    return p[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if cost[a] > cost[b]:
        p[a] = b
    else:
        p[b] = a


N, M, k = map(int, input().split())
cost = list(map(int, input().split()))
p = [i for i in range(N)]
friends = []
for _ in range(M):
    f, s = map(int, input().split())
    friends.append((f, s))
    union(f - 1, s - 1)
for f, s in friends:
    union(f-1, s-1)
total = 0
for i in set(p):
    total += cost[i]
if total > k:
    print("Oh no ")
else:
    print(total)

