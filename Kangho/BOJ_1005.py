import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    building_time = list(map(int, input().split()))
    total_time = [0] * N
    graph = [[] for _ in range(N)]
    indegree = [0] * N
    for _ in range(K):
        start, end = map(int, input().split())
        graph[start - 1].append(end - 1)
        indegree[end - 1] += 1
    winning_build = int(input()) - 1
    q = deque()
    for i in range(N):
        if indegree[i] == 0:
            q.append(i)
    flag = True
    while q and flag:
        curr = q.popleft()
        for nxt in graph[curr]:
            indegree[nxt] -= 1
            total_time[nxt] = max(total_time[nxt], total_time[curr] + building_time[curr])
            if indegree[nxt] == 0:
                q.append(nxt)
                if nxt == winning_build:
                    flag = False
                    break
    total_time[winning_build] += building_time[winning_build]
    print(total_time[winning_build])
