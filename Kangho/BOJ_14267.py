import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
save = [0] * N
points = [0] * N
boss = list(map(int, input().split()))
for i in range(N):
    if boss[i] == -1:
        continue
    graph[boss[i]-1].append(i)
for _ in range(M):
    emnum, com = map(int, input().split())
    save[emnum-1] += com
prop = 0
def dfs(cur):
    global prop
    prop += save[cur]
    points[cur] = prop
    for nxt in graph[cur]:
        dfs(nxt)
    prop -= save[cur]
dfs(0)
print(" ".join(list(map(str, points))))
