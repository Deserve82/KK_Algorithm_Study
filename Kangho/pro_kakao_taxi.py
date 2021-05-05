def solution(n, s, a, b, fares):
    s -= 1
    a -= 1
    b -= 1
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for fare in fares:
        fare[0] -= 1
        fare[1] -= 1
        dist[fare[0]][fare[1]] = min(fare[2], dist[fare[0]][fare[1]])
        dist[fare[1]][fare[0]] = min(fare[2], dist[fare[1]][fare[0]])

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

    answer = dist[s][a] + dist[s][b]
    for i in range(n):
        answer = min(answer, dist[s][i]+dist[i][a]+dist[i][b])

    return answer
