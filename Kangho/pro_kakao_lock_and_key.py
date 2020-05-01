def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret


def fit_check(startX, startY, key, lock, expandSize, start, end):
    expandList = [[0] * expandSize for _ in range(expandSize)]

    for i in range(len(key)):
        for j in range(len(key)):
            expandList[startX + i][startY+j] += key[i][j]

    for i in range(start, end):
        for j in range(start, end):
            expandList[i][j] += lock[i-start][j-start]
            if expandList[i][j] != 1:
                return False
    return True


def solution(key, lock):
    start = len(key) - 1
    end = start + len(lock)
    expandSize = len(lock) + start*2

    for a in range(4):
        for i in range(end):
            for j in range(end):
                if fit_check(i, j, key, lock, expandSize, start, end):
                    return True
        key = rotate_90(key)
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))