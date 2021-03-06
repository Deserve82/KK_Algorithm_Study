n = int(input())
answer = []


def rec(idx, friends_list):
    global count
    if len(answer) == n:
        count += 1
        return
    else:
        for i in range(idx, m):
            if friends_list[i * 2] not in answer and friends_list[i * 2 + 1] not in answer:
                answer.extend([friends_list[i * 2], friends_list[i * 2 + 1]])
                rec(i, friends_list)
                answer.pop()
                answer.pop()
        return


for _ in range(n):
    count = 0
    n, m = map(int, input().split())
    friends_list = list(map(int, input().split()))
    rec(0, friends_list)
    print(count)
    
    
 # 12/16 다시 풀었음
cnt = 0


def make_couple(r):
    global cnt, nof
    if False not in checker:
        cnt += 1
        return
    else:
        for i in range(r, nof):
            for j in range(nof):
                if couples[i][j] and not checker[i] and not checker[j] and i > j:
                    checker[i] = checker[j] = True
                    make_couple(i)
                    checker[i] = checker[j] = False


n = int(input())
for _ in range(n):
    nof, cc = map(int, input().split())
    couples = [[False] * nof for _ in range(nof)]
    checker = [False]*nof
    cl = list(map(int, input().split()))
    for _ in range(cc):
        a, b = cl.pop(), cl.pop()
        couples[a][b] = True
        couples[b][a] = True
    make_couple(0)
    print(cnt)
    cnt = 0
    
# 종만북 풀이 - 내 원래 풀이보다 3배 빠름
def make_couple():
    global nof

    first_free = -1
    for i in range(nof):
        if not checker[i]:
            first_free = i
            break
    if first_free == -1:
        return 1
    
    ret = 0
    for j in range(first_free+1, nof):
        if not checker[j] and couples[first_free][j]:
            checker[j] = checker[first_free] = True
            ret += make_couple()
            checker[j] = checker[first_free] = False
    return ret


n = int(input())
for _ in range(n):
    nof, cc = map(int, input().split())
    couples = [[False] * nof for _ in range(nof)]
    checker = [False]*nof
    cl = list(map(int, input().split()))
    for _ in range(cc):
        a, b = cl.pop(), cl.pop()
        couples[a][b] = True
        couples[b][a] = True
    print(make_couple())
