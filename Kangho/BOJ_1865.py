def send_to_universe():
    is_update = False
    for i in range(N):
        for j in range(N):
            for nx, nxw in graph[j]:
                cost = weights[j] + nxw
                if weights[nx] > cost:
                    weights[nx] = cost
                    if i == N-1:
                        is_update = True
    return is_update


for _ in range(int(input())):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        s, e, val = map(int, input().split())
        s -= 1
        e -= 1
        graph[s].append((e, val))
        graph[e].append((s, val))
    for _ in range(W):
        s, e, val = map(int, input().split())
        s -= 1
        e -= 1
        graph[s].append((e, -val))

    weights = [2200000000] * N
    a = False
    for i in range(N):
        if graph[i]:
            weights[i] = 0
            if send_to_universe():
                print("YES")
            else:
                print("NO")
            break
