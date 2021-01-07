n_test = int(input())
for _ in range(n_test):
    V, W = map(int, input().split())
    answer = [0, 0]
    dist = [-float('inf') for i in range(V)]
    dist[0] = 0
    adj_1 = [[] for i in range(V)]

    for i in range(W):
        a, b, d = map(int, input().split())
        adj_1[a].append((b, d))

    upper_1 = [float('inf') for i in range(V)]
    upper_1[0] = 0
    for i in range(V):
        isUpdated = False
        for here in range(V):
            for there, cost in adj_1[here]:
                if upper_1[there] > upper_1[here] + cost:
                    upper_1[there] = upper_1[here] + cost
                    isUpdated = True
        if not isUpdated:
            break

    if isUpdated:
        answer[0] = "INFINITY"
    else:
        answer[0] = upper_1[1]

    upper_2 = [-float('inf') for i in range(V)]
    upper_2[0] = 0
    for i in range(V):
        isUpdated = False
        for here in range(V):
            for there, cost in adj_1[here]:
                if upper_2[there] < upper_2[here] + cost:
                    upper_2[there] = upper_2[here] + cost
                    isUpdated = True
        if not isUpdated:
            break

    if isUpdated:
        answer[1] = "INFINITY"
    else:
        answer[1] = upper_2[1]

    if answer[0] == float('inf') and answer[1] == -float('inf'):
        print("UNREACHABLE")
    else:
        print(' '.join(map(str, answer)))
