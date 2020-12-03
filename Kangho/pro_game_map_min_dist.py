from collections import deque

d = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def bfs(s, ma):
    row_size = len(ma)
    col_size = len(ma[0])
    check = [[False]*col_size for _ in range(row_size)]
    q = deque()
    q.append(s)
    while q:
        loc = q.popleft()
        for di in d:
            m_r = loc[0] + di[0]
            m_c = loc[1] + di[1]
            if -1 < m_c < col_size and -1 < m_r < row_size and not check[m_r][m_c] and ma[m_r][m_c] != 0:
                ma[m_r][m_c] = ma[loc[0]][loc[1]] + 1
                check[m_r][m_c] = True
                q.append((m_r, m_c))
    if check[row_size-1][col_size-1]:
        return ma[row_size-1][col_size-1]
    else:
        return -1


def solution(maps):
    answer = bfs((0, 0), maps)
    return answer
