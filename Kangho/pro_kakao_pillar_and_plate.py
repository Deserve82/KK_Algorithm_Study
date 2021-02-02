def check_gidung(gidungs, boes, row, col, n):
    if row == n:
        return True
    elif gidungs[row + 1][col] == 1:
        return True
    elif boes[row][col - 1] == 1 or boes[row][col] == 1:
        return True
    return False


def check_boe(gidungs, boes, row, col):
    if gidungs[row + 1][col] == 1 or gidungs[row + 1][col + 1] == 1:
        return True
    elif boes[row][col - 1] == 1 and boes[row][col + 1] == 1:
        return True
    return False


def check_deletion(gidungs, boes, n):
    for i in range(n + 1):
        for j in range(n + 1):
            if gidungs[i][j] == 1:
                if not check_gidung(gidungs, boes, i, j, n):
                    return False
            if boes[i][j] == 1:
                if not check_boe(gidungs, boes, i, j):
                    return False
    return True


def solution(n, build_frame):
    answer = []
    boes = [[0] * (n + 1) for _ in range(n + 1)]
    gidungs = [[0] * (n + 1) for _ in range(n + 1)]
    for frame in build_frame:
        col, row, is_boe, is_installation = frame
        row = n - row

        if is_installation:
            if not is_boe:
                if check_gidung(gidungs, boes, row, col, n):
                    gidungs[row][col] = 1
            else:
                if check_boe(gidungs, boes, row, col):
                    boes[row][col] = 1
        else:
            if not is_boe:
                gidungs[row][col] = 0
            else:
                boes[row][col] = 0

            if not check_deletion(gidungs, boes, n):
                if not is_boe:
                    gidungs[row][col] = 1
                else:
                    boes[row][col] = 1

    for i in range(n + 1):
        for j in range(n + 1):
            if gidungs[i][j] == 1:
                answer.append([j, n - i, 0])
            if boes[i][j] == 1:
                answer.append([j, n - i, 1])
    answer.sort()
    return answer

print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
