from collections import deque
movements = [(0, 1), (1, 0), (-1, 0), (0, -1)]
rotations = [1, -1]


def move(t, h, nb):
    value_lists = []
    tr, tc = t
    hr, hc = h
    for i in range(4):
        mr, mc = movements[i]
        if nb[tr+mr][tc+mc] == 0 and nb[hr+mr][hc+mc] == 0:
            value_lists.append(((tr+mr, tc+mc), (hr+mr, hc+mc)))

    for i in range(2):
        side = rotations[i]
        if hr == tr:
            if nb[tr+side][tc] == 0 and nb[hr+side][hc] == 0:
                value_lists.append(((tr, tc), (tr+side, tc)))
                value_lists.append(((hr, hc), (hr+side, hc)))
        else:
            if nb[tr][tc+side] == 0 and nb[hr][hc+side] == 0:
                value_lists.append(((tr, tc+side), (tr, tc)))
                value_lists.append(((hr, hc), (hr, hc+side)))
    return value_lists


def bfs(b, pivot):
    q = deque()
    q.append(((1, 1), (1, 2), 0))
    check = {((1, 1), (1, 2)): 1}
    while q:
        tail, head, cost = q.popleft()

        if tail == (pivot, pivot) or head == (pivot, pivot):
            return cost

        ml = move(tail, head, b)
        for a in ml:
            if a not in check:
                check[a] = 1
                t, h = a
                q.append((t, h, cost+1))


def solution(board):
    N = len(board)
    new_board = [[0]*(N+2) for _ in range(N+2)]

    for i in range(N):
        for j in range(N):
            new_board[i+1][j+1] = board[i][j]
    for i in range(N+2):
        new_board[0][i] = 1
        new_board[N+1][i] = 1
        new_board[i][0] = 1
        new_board[i][N+1] = 1

    answer = bfs(new_board, N)
    return answer


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
