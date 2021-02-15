import sys

input = sys.stdin.readline


def make_flow(prev):
    global S, T
    cur = T
    flow = float('inf')
    while cur != S:
        flow = min(flow, c[prev[cur]][cur] - f[prev[cur]][cur])
        cur = prev[cur]

    cur = T
    while cur != S:
        f[prev[cur]][cur] += flow
        f[cur][prev[cur]] -= flow
        cur = prev[cur]
    return flow


def bfs():
    global S, T
    q = [S]
    prv = [-1] * (M + N + 2)
    for node in q:
        for nxt in adj[node]:
            if c[node][nxt] > f[node][nxt] and prv[nxt] < 0:
                q.append(nxt)
                prv[nxt] = node
                if nxt == T:
                    return make_flow(prv)
    return -1


N, M = map(int, input().split())
f = [[0] * (M + N + 2) for _ in range(M + N + 2)]
c = [[0] * (M + N + 2) for _ in range(M + N + 2)]
adj = [set() for _ in range(M + N + 2)]
S, T = 0, M + N + 1
for i in range(1, N + 1):
    info = list(map(int, input().split()))
    adj[S].add(i)
    adj[i].add(S)
    c[S][i] = 1
    c[i][S] = 0
    for information in info[1:]:
        adj[i].add(information + N)
        adj[information + N].add(i)
        c[i][information + N] = 1
        c[information + N][i] = 0

        adj[T].add(information + N)
        adj[information + N].add(T)
        c[T][information + N] = 0
        c[information + N][T] = 1

total_flow = 0
while True:
    flow = bfs()
    if flow > 0:
        total_flow += flow
    else:
        break
print(total_flow)
