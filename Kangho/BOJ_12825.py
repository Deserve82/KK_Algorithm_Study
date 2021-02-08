from collections import deque


def bfs():
    q = deque()
    q.append([n, [n]])
    while q:
        number, history = q.popleft()
        if number == 1:
            print(len(history)-1)
            print(" ".join(map(str, history)))
            break
        if number % 3 == 0:
            tmp = number // 3
            if tmp not in checker:
                checker[tmp] = 1
                q.append([tmp, history + [tmp]])
        if number % 2 == 0:
            tmp = number // 2
            if tmp not in checker:
                checker[tmp] = 1
                q.append([tmp, history + [tmp]])
        if number - 1 not in checker:
            q.append([number - 1, history + [number - 1]])


n = int(input())
checker = {}
bfs()
