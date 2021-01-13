from collections import deque


def bfs():
    global ans
    q = deque()
    x = ''.join(numbers)
    check[x] = 1
    q.append([x, 0])
    while q:
        curr, cost = q.popleft()
        if curr == ans:
            return cost
        for i in range(N-K+1):
            a = list(curr)
            aa = a[i:i+K]
            aa.reverse()
            a = a[:i] + aa + a[i+K:]
            nx = ''.join(a)
            if nx not in check:
                check[nx] = 1
                q.append([nx, cost + 1])
    return -1


N, K = map(int, input().split())
ans = ''
for i in range(1, N+1):
    ans += str(i)
numbers = list(input().split())
check = {}
print(bfs())
