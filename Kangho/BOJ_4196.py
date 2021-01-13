import sys
sys.setrecursionlimit(1000000)


def dfs(curr):
    global cnt, SN
    cnt += 1
    dfsn[curr] = cnt
    S.append(curr)

    result = dfsn[curr]
    for nxt in graph[curr]:
        if dfsn[nxt] == 0:
            result = min(result, dfs(nxt))
        elif not finished[nxt]:
            result = min(result, dfsn[nxt])

    if result == dfsn[curr]:
        while True:
            t = S.pop()
            finished[t] = True
            sn[t] = SN
            if t == curr:
                break
        SN += 1

    return result


for _ in range(int(input())):
    cnt = 0
    SN = 0
    N, M = map(int, sys.stdin.readline().split())
    dfsn = [0] * N
    sn = [0] * N
    S = []
    finished = [False] * N
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a - 1].append(b - 1)
    for i in range(N):
        if dfsn[i] == 0:
            dfs(i)
    out_degree = [0] * 100000
    for i in range(N):
        for j in graph[i]:
            if sn[i] != sn[j]:
                out_degree[sn[j]] += 1
    ret = 0
    for i in range(SN):
        if out_degree[i] == 0:
            ret += 1
    print(ret)
