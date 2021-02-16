import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
directions = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
fire_balls = {}
board = [[[] for _ in range(N)] for _ in range(N)]
total_idx = M+1
for i in range(1, M+1):
    row, col, mas, spd, direction = map(int, input().split())
    fire_balls[i] = [row-1, col-1, mas, spd, direction]
    board[row-1][col-1].append(i)
while K:
    K -= 1
    for idx, fb in fire_balls.items():
        r, c, m, s, d = fb
        board[r][c].remove(idx)
        mr, mc = r + directions[d][0] * s, c + directions[d][1] * s
        if 0 <= mr < N and 0 <= mc < N:
            pass
        else:
            while mr >= N:
                mr -= N
            while mr < 0:
                mr += N
            while mc >= N:
                mc -= N
            while mc < 0:
                mc += N
        fire_balls[idx][0], fire_balls[idx][1] = mr, mc
        board[mr][mc].append(idx)
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) > 1:
                sum_of_mas = 0
                sum_of_speed = 0
                has_even, has_odd = 0, 0
                num = len(board[i][j])
                while board[i][j]:
                    index = board[i][j].pop()
                    sum_of_mas += fire_balls[index][2]
                    sum_of_speed += fire_balls[index][3]
                    if fire_balls[index][4] % 2 == 1:
                        has_odd += 1
                    else:
                        has_even += 1
                    del fire_balls[index]

                mass = sum_of_mas // 5
                if mass != 0:
                    avg_spd = sum_of_speed // num
                    if has_even == 0 or has_odd == 0:
                        for direc in [0, 2, 4, 6]:
                            total_idx += 1
                            fire_balls[total_idx] = [i, j, mass, avg_spd, direc]
                            board[i][j].append(total_idx)
                    else:
                        for direc in [1, 3, 5, 7]:
                            total_idx += 1
                            fire_balls[total_idx] = [i, j, mass, avg_spd, direc]
                            board[i][j].append(total_idx)
answer = 0
for ff in fire_balls.values():
    answer += ff[2]
print(answer)
