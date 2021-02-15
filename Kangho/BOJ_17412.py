import sys

input = sys.stdin.readline


def make_flow(prv):
    curr = T
    flow = float('inf')
    while S != curr:
        flow = min(flow, c[prv[curr]][curr] - f[prv[curr]][curr])
        curr = prv[curr]

    curr = T
    while S != curr:
        f[prv[curr]][curr] += flow
        f[curr][prv[curr]] -= flow
        curr = prv[curr]
    return flow


def bfs():
    que = [S]
    prev = [-1] * (N + 1)
    for curr in que:
        for nxt in adj[curr]:
            if prev[nxt] < 0 and c[curr][nxt] > f[curr][nxt]:
                que.append(nxt)
                prev[nxt] = curr
                if nxt == T:
                    return make_flow(prev)
    return -1


N, P = map(int, input().split())
f = [[0] * (N + 1) for _ in range(N + 1)]
c = [[0] * (N + 1) for _ in range(N + 1)]
adj = [set() for _ in range(N + 1)]
S, T = 1, 2
for _ in range(P):
    s, e = map(int, input().split())
    adj[s].add(e)
    adj[e].add(s)
    c[s][e] = 1
total_flow = 0
while True:
    floww = bfs()
    if floww > 0:
        total_flow += floww
    else:
        break
print(total_flow)
