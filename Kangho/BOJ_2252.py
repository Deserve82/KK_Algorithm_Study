from collections import deque
n, m = map(int, input().split())
in_degree = [0] * (n+1)
a = [[] for _ in range(n+1)]
for _ in range(m):
    fr, to = map(int, input().split())
    in_degree[to] += 1
    a[fr].append(to)
answer = []
q = deque()
for i in range(1, n+1):
    if in_degree[i] == 0:
        q.append(i)
        answer.append(str(i))
while q:
    x = q.popleft()
    for num in a[x]:
        in_degree[num] -= 1
        if in_degree[num] == 0:
            answer.append(str(num))
            q.append(num)
print(" ".join(answer))
