from collections import deque

board = []


def rotation(sr, sc, er, ec):
    q = deque()
    for i in range(sc, ec):
        q.append(board[sr][i])
    for i in range(sr, er):
        q.append(board[i][ec])
    for i in range(ec, sc, -1):
        q.append(board[er][i])
    for i in range(er, sr, -1):
        q.append(board[i][sc])
    q.rotate(1)
    min_val = min(q)
    q_idx = 0
    for i in range(sc, ec):
        board[sr][i] = q[q_idx]
        q_idx += 1
    for i in range(sr, er):
        board[i][ec] = q[q_idx]
        q_idx += 1
    for i in range(ec, sc, -1):
        board[er][i] = q[q_idx]
        q_idx += 1
    for i in range(er, sr, -1):
        board[i][sc] = q[q_idx]
        q_idx += 1
    return min_val


def solution(rows, columns, queries):
    global board
    answer = []
    board = [[0] * columns for _ in range(rows)]
    idx = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = idx
            idx += 1
    for query in queries:
        answer.append(rotation(query[0]-1, query[1]-1, query[2]-1, query[3]-1))
    return answer
