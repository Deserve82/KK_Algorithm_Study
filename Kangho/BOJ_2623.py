from collections import deque
N, M = map(int, input().split())
in_degree = [0]*N
what_they_have = [set() for _ in range(N)]
r = [set() for _ in range(N)]
for _ in range(M):
    numbers = list(map(int, input().split()))[1:]
    for i, number in enumerate(numbers):
        what_they_have[number-1].update(numbers[:i])
        r[number-1].update(numbers[i+1:])
        in_degree[number-1] = len(what_they_have[number-1])
q = deque()
for i, node in enumerate(in_degree):
    if node == 0:
        q.append(i)
flag = False
ans = []
if not q:
    flag = True
else:
    while q:
        curr = q.popleft()
        ans.append(curr+1)
        for nxt in r[curr]:
            in_degree[nxt-1] -= 1
            if in_degree[nxt-1] == 0:
                q.append(nxt-1)
    for node in in_degree:
        if node > 0:
            flag = True
            break
if flag:
    print(0)
else:
    for a in ans:
        print(a)
