n = int(input())
answer = 0
check_field = [[0]*n for _ in range(n)]
number_of_queen = 0
check = []


def garo(a):
    for c in check:
        if c[0] == a:
            return False
    return True


def sero(b):
    for c in check:
        if c[1] == b:
            return False
    return True


def daegak(d):
    # 2, 0
    for c in check:
        if abs(c[0]-d[0]) == abs(c[1]-d[1]):
            return False
    return True


def bt(r, c):
    global answer
    global number_of_queen
    if number_of_queen == n:
        print(check)
        answer += 1
    else:
        for i in range(n):
            for j in range(n):
                if garo(i) and sero(j) and daegak([i, j]):
                    number_of_queen += 1
                    check.append([i, j])
                    bt(i, j)
                    check.pop()
                    number_of_queen -= 1


bt(0, 0)
print(answer)
