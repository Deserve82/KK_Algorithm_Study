left_stroke = [1, -1]
right_stoke = [1, 1]


def calculate_space(r, c, dis, space):
    district_sum = 0
    if space == 1:
        for i in range(0, r + dis):
            if i >= r:
                c -= 1
            for j in range(0, c+1):
                district_sum += board[i][j]
    elif space == 2:
        for i in range(0, r+dis+1):
            if i > r:
                c += 1
            for j in range(c+1, N):
                district_sum += board[i][j]
    elif space == 3:
        for i in range(r, N):
            for j in range(0, c):
                district_sum += board[i][j]
            if dis > 0:
                c += 1
                dis -= 1
    else:
        for i in range(r+1, N):
            for j in range(c, N):
                district_sum += board[i][j]
            if dis > 0:
                c -= 1
                dis -= 1
    return district_sum


def choose_length(row, col):
    global answer
    for d1 in range(1, N):
        for d2 in range(1, N):
            if 0 <= col - d1 and d2 + col <= N - 1 and row + d1 + d2 <= N - 1 and col + d2 <= N - 1:
                s1 = calculate_space(row, col, d1, 1)
                s2 = calculate_space(row, col, d2, 2)
                s3 = calculate_space(row+d1, col-d1, d2, 3)
                s4 = calculate_space(row+d2, col+d2, d1, 4)
                s5 = total_pop - (s1+s2+s3+s4)
                maxv = max(s1, s2, s3, s4, s5)
                minv = min(s1, s2, s3, s4, s5)
                answer = min(answer, maxv - minv)


answer = 987654321
N = int(input())
board = []
total_pop = 0
for _ in range(N):
    a = list(map(int, input().split()))
    board.append(a)
    total_pop += sum(a)
# choose start point
for i in range(N):
    for j in range(N):
        if i < N - 2 and 1 <= j < N - 1:
            choose_length(i, j)
print(answer)
