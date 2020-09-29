from collections import deque
n = int(input())
a = [[] for _ in range(501)]
times = [0] * n
in_degree = [0] * n
ans = [0] * n
q = deque()
for i in range(n):
    inp = list(map(int, input().split()))
    times[i] = inp[0]
    ans[i] = times[i]
    if len(inp) == 2:
        q.append(i)
    else:
        for num in inp[1:-1]:
            a[num-1].append(i)
            in_degree[i] += 1
while q:
    ind_of_t = q.popleft()
    trunks = a[ind_of_t]
    for i in trunks:
        ans[i] = max(ans[i], ans[ind_of_t]+times[i])
        in_degree[i] -= 1
        if in_degree[i] == 0:
            q.append(i)
for an in ans:
    print(an)
