import sys
import heapq as hq
input = sys.stdin.readline
for _ in range(int(input())):
    n, d, start = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((s, a))

    pq = [(0, start)]
    weight = [float('inf')] * (n+1)
    weight[start] = 0

    while pq:
        dis, curr_node = hq.heappop(pq)
        for nxt in graph[curr_node]:
            if weight[nxt[1]] > dis + nxt[0]:
                hq.heappush(pq, (dis+nxt[0], nxt[1]))
                weight[nxt[1]] = dis+nxt[0]
    sec_ans, cnt_ans = 0, 0
    for w in weight:
        if w != float('inf'):
            cnt_ans += 1
            sec_ans = max(w, sec_ans)

    print(cnt_ans, sec_ans)
