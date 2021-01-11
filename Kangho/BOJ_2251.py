from collections import deque

check = []


def bfs():
    q = deque()
    q.append(water)
    while q:
        node = q.popleft()
        (a, b, c) = node
        if a == 0:
            answer_c.add(c)
        if (a, b, c) in check:
            continue
        else:
            check.append((a, b, c))
            if a:
                if a + b > B:
                    q.append((a + b - B, B, c))
                else:
                    q.append((0, a + b, c))
                if a + c > C:
                    q.append((a + c - C, b, C))
                else:
                    q.append((0, b, a + c))
            if b:
                if a + b > A:
                    q.append((A, a + b - A, c))
                else:
                    q.append((a + b, 0, c))
                if b + c > C:
                    q.append((a, b + c - C, C))
                else:
                    q.append((a, 0, b + c))
            if c:
                if a + c > A:
                    q.append((A, b, a + c - A))
                else:
                    q.append((a + c, b, 0))
                if b + c > B:
                    q.append((a, B, b + c - B))
                else:
                    q.append((a, b + c, 0))


answer_c = set()
A, B, C = map(int, input().split())
water = (0, 0, C)
bfs()
answer_c = list(answer_c)
answer_c.sort()
print(" ".join(map(str, answer_c)))
