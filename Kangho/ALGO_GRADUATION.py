import sys
input = sys.stdin.readline


def dp(sem, studied):
    if bin(studied).count("1") >= K and sem <= M:
        return 0
    elif sem >= M:
        return 9999

    if cache[sem][studied] != -1:
        return cache[sem][studied]
    ret = 9999
    can_take = 0
    classes = semesters[sem]
    for c in classes:
        if studied & (1 << c) == 0 and pre_require[c] & studied == pre_require[c]:
            can_take |= (1 << c)

    subset = can_take + 1
    while subset:
        subset = (subset-1) & can_take
        if bin(subset).count("1") <= L:
            ret = min(ret, dp(sem+1, studied | subset) + 1)

    ret = min(ret, dp(sem+1, studied))
    cache[sem][studied] = ret
    return ret


for _ in range(int(input())):
    N, K, M, L = map(int, input().split())
    pre_require = [0] * N
    for i in range(N):
        pre = list(map(int, input().split()))
        for num in pre[1:]:
            pre_require[i] |= (1 << num)
    semesters = []
    for _ in range(M):
        semesters.append(list(map(int, input().split()))[1:])
    cache = [[-1] * (1 << N) for _ in range(M+1)]
    answer = dp(0, 0)
    if answer == 9999:
        print("IMPOSSIBLE")
    else:
        print(answer)
