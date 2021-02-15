import sys

input = sys.stdin.readline
h = lambda x: ord(x) - ord('A') if x <= 'Z' else ord(x) - ord('a') + 26
f = [[0] * 52 for _ in range(52)]
c = [[0] * 52 for _ in range(52)]
adj = [set() for _ in range(52)]
S = h('A')
T = h('Z')


def make_flow(prv):
    global S, T
    flow = float('inf')
    cur = T
    while cur != S:
        flow = min(flow, c[prv[cur]][cur] - f[prv[cur]][cur])
        cur = prv[cur]
    cur = T
    while cur != S:
        f[prv[cur]][cur] += flow
        f[cur][prv[cur]] -= flow
        cur = prv[cur]
    return flow


def bfs():
    global S, T
    prev = [-1] * 52
    que = [S]
    for cur in que:
        for nxt in adj[cur]:
            if c[cur][nxt] > f[cur][nxt] and prev[nxt] < 0:
                que.append(nxt)
                prev[nxt] = cur
                if nxt == T: return make_flow(prev)
    return -1


N = int(input())
for _ in range(N):
    u, v, C = input().split()
    u, v, C = h(u), h(v), int(C)
    c[u][v] += C
    c[v][u] += C
    adj[u].add(v)
    adj[v].add(u)
total_flow = 0
while True:
    flow = bfs()
    if flow > 0:
        total_flow += flow
    else:
        break
print(total_flow)
