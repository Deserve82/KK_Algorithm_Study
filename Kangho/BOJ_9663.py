# 내가 푼 느린 코드
n = int(input())
row_check = [False] * n
col_check = [False] * n
cnt = 0
daegaks = []


def check_daegak(i, j):
    for d in daegaks:
        if abs(d[0] - i) == abs(d[1] - j):
            return True
    return False


def queen(qn, r):
    global n, cnt
    if qn == n:
        cnt += 1
        return
    else:
        for i in range(r, n):
            for j in range(n):
                if not row_check[i] and not col_check[j]:
                    on_daegak = check_daegak(i, j)
                    if not on_daegak:
                        row_check[i], col_check[j] = True, True
                        daegaks.append((i, j))
                        queen(qn + 1, i)
                        daegaks.pop()
                        row_check[i], col_check[j] = False, False


queen(0, 0)
print(cnt)


# 최적화를 적용한 코드
n = int(input())
row_check = [False] * n
left = [False] * (2*n-1)
right = [False] * (2*n-1)
cnt = 0


def queen(qn):
    global n, cnt
    if qn == n:
        cnt += 1
        return
    else:
        for j in range(n):
            if not row_check[j] and not left[j + qn] and not right[n-1 + qn - j]:
                row_check[j] = left[j + qn] = right[n-1 + qn - j] = True
                queen(qn + 1)
                row_check[j] = left[j + qn] = right[n-1 + qn - j] = False


queen(0)
print(cnt)
