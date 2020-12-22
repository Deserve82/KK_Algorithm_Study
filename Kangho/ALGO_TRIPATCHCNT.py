def triangle(row, col):
    if row >= n:
        return 0
    if cnt_tri[row][col]:
        return cnt_tri[row][col]
    ret = tri[row][col]
    ret += max(triangle(row + 1, col), triangle(row + 1, col + 1))
    cnt_tri[row][col] = ret
    return cnt_tri[row][col]


def back_to_the_zero(row, col):
    if row == n-1:
        return 1
    if cache[row][col] != -1:
        return cache[row][col]
    cnt = 0
    if cnt_tri[row][col] - cnt_tri[row + 1][col] == tri[row][col]:
        cnt += back_to_the_zero(row + 1, col)
    if cnt_tri[row][col] - cnt_tri[row + 1][col + 1] == tri[row][col]:
        cnt += back_to_the_zero(row + 1, col + 1)
    cache[row][col] = cnt
    return cache[row][col]


for _ in range(int(input())):
    n = int(input())
    tri = []
    cnt_tri = []
    cache = []
    for i in range(n):
        tri.append(list(map(int, input().split())))
        cnt_tri.append([0] * (i + 1))
        cache.append([-1] * (i + 1))
    max_val = triangle(0, 0)
    print(back_to_the_zero(0, 0))
