from collections import deque
idx = [
    [1, 3], [0, 2, 4], [1, 5], [0, 4, 6], [1, 3, 5, 7], [2, 4, 8], [3, 7], [4, 6, 8], [5, 7]
]
P = '123456780'


def bfs():
    q = deque()
    zero_idx = -1
    for i in range(9):
        if board[i] == '0':
            zero_idx = i
            break
    x = ''.join(board)
    check = {x: 1}
    q.append([x, zero_idx, 0])
    while q:
        s_num, zi, cost = q.popleft()
        step = check.get(s_num)
        if s_num == P:
            return cost
        for i in idx[zi]:
            t = list(s_num)
            t[i], t[zi] = t[zi], t[i]
            t = ''.join(t)
            if not check.get(t):
                q.append([t, i, cost + 1])
                check[t] = step
    return -1


board = []
for _ in range(3):
    board.extend(list(input().split()))
print(bfs())
