import sys

input = sys.stdin.readline
directions = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}

N, M, k = map(int, input().split())
sharks = [[] for _ in range(M + 1)]
shark_priority = [[] for _ in range(M + 1)]
shark_board = []
# 사실 상 샤크 보드는 상관 없지만 만약 가는 곳에 자기 보다 작은 녀석이 있다면 그냥 나가면 됌
board = [[[0, 0] for _ in range(N)] for _ in range(N)]
total_shark = 0
for i in range(N):
    she = list(map(int, input().split()))
    for j in range(N):
        if she[j] != 0:
            sharks[she[j]] = [i, j, 0]
            total_shark += 1
    shark_board.append(she)
s_d = list(map(int, input().split()))
for i, a in enumerate(s_d):
    sharks[i + 1][2] = a
for i in range(1, M + 1):
    sp = []
    for _ in range(4):
        sp.append(list(map(int, input().split())))
    shark_priority[i] = sp

time = 0
while time <= 1000 and total_shark != 1:

    # 냄새 뿌리기
    for i, shark in enumerate(sharks):
        if i == 0 or shark == [-1, -1, -1]:
            continue
        s_row, s_col, d = shark
        board[s_row][s_col][0], board[s_row][s_col][1] = i, k

    # 이동하기, 적은 상어 삭제 잊지 말기
    # 먼저 빈칸 찾기, 없다면 다시 돌면서 자기 냄새 찾기
    for i, shark in enumerate(sharks):
        if i == 0 or shark == [-1, -1, -1]:
            continue
        s_row, s_col, d = shark
        spin = shark_priority[i][d - 1]
        # 빈칸 먼저 찾기, 찾으면 상어와 보드의 값 둘다 바꾸어 주어야 한다.
        has_empty = False
        for move in spin:
            m_row, m_col = s_row + directions[move][0], s_col + directions[move][1]
            if 0 <= m_row < N and 0 <= m_col < N:
                if board[m_row][m_col] == [0, 0] and shark_board[m_row][m_col] == 0:
                    sharks[i] = [m_row, m_col, move]
                    shark_board[s_row][s_col], shark_board[m_row][m_col] = 0, i
                    has_empty = True
                    break
                elif board[m_row][m_col] == [0, 0] and shark_board[m_row][m_col] != 0:
                    total_shark -= 1
                    if i > shark_board[m_row][m_col]:
                        sharks[i] = [-1, -1, -1]
                        shark_board[s_row][s_col] = 0
                    else:
                        sharks[shark_board[m_row][m_col]] = [-1, -1, -1]
                        shark_board[s_row][s_col], shark_board[m_row][m_col] = 0, i
                    has_empty = True
                    break

        # 빈 칸이 없을 때
        if not has_empty:
            for move in spin:
                m_row, m_col = s_row + directions[move][0], s_col + directions[move][1]
                if 0 <= m_row < N and 0 <= m_col < N:
                    if board[m_row][m_col][0] == i:
                        sharks[i] = [m_row, m_col, move]
                        shark_board[s_row][s_col], shark_board[m_row][m_col] = 0, i
                        break
    # 냄새 옅어짐
    for i in range(N):
        for j in range(N):
            if board[i][j] != [0, 0]:
                board[i][j][1] -= 1
                if board[i][j][1] == 0:
                    board[i][j][0] = 0
    time += 1
if time > 1000:
    print(-1)
else:
    print(time)
