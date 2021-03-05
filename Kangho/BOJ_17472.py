movements = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    parent[b] = a


def dfs(r, c):
    s = [(r, c)]
    while s:
        curr = s.pop()
        for movement in movements:
            mr = curr[0] + movement[0]
            mc = curr[1] + movement[1]
            if 0 <= mr < R and 0 <= mc < C:
                if board[mr][mc] != 0 and not checker[mr][mc]:
                    checker[mr][mc] = True
                    board[mr][mc] = square_idx
                    s.append((mr, mc))


def add_dis(r, c):
    pivot = board[r][c]
    for i in range(r - 1, -1, -1):
        if board[i][c] == pivot:
            break
        elif board[i][c] != 0:
            if r - i - 1 >= 2:
                distances.append((r - i - 1, pivot, board[i][c]))
            break

    for i in range(r, R):
        if board[i][c] == pivot:
            break
        elif board[i][c] != 0:
            if i - r - 1 >= 2:
                distances.append((i - r - 1, pivot, board[i][c]))
            break

    for j in range(c - 1, -1, -1):
        if board[r][j] == pivot:
            break
        elif board[r][j] != 0:
            if c - j - 1 >= 2:
                distances.append((c - j - 1, pivot, board[r][j]))
            break

    for j in range(c, C):
        if board[r][c] == pivot:
            break
        elif board[r][j] != 0:
            if j - c - 1 >= 2:
                distances.append((j - c - 1, pivot, board[r][j]))
            break


R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(map(int, input().split())))
checker = [[False] * C for _ in range(R)]
square_idx = 1
for i in range(R):
    for j in range(C):
        if board[i][j] != 0 and not checker[i][j]:
            checker[i][j] = True
            board[i][j] = square_idx
            dfs(i, j)
            square_idx += 1
parent = [i for i in range(square_idx-1)]
distances = []
for i in range(R):
    for j in range(C):
        if board[i][j] != 0:
            add_dis(i, j)
distances = list((set(distances)))
distances.sort(key=lambda x: x[0])
answer = 0
for distance in distances:
    dis, f, t = distance
    if find(f-1) != find(t-1):
        union(f-1, t-1)
        answer += dis
for p in range(square_idx-1):
    find(p)
if len(set(parent)) != 1:
    print(-1)
else:
    print(answer)
