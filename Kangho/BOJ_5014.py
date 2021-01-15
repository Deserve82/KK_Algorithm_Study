from collections import deque


def bfs():
    q = deque()
    q.append([S, 0])
    while q:
        here, cost = q.popleft()
        if here == G:
            return cost

        if here + U <= F:
            if not check[here + U]:
                check[here + U] = True
                q.append([here + U, cost + 1])
        if here - D > 0:
            if not check[here - D]:
                check[here - D] = True
                q.append([here - D, cost + 1])
    return -1


F, S, G, U, D = map(int, input().split())
check = [False] * (F+1)
check[S] = True
a = bfs()
if a == -1:
    print("use the stairs")
else:
    print(a)
