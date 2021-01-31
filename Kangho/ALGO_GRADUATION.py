def dynamic(sem, taken):
    if bin(taken).count("1") >= K:
        return 0
    if sem == M:
        return float('inf')

    if cache[sem][taken] is not None:
        return cache[sem][taken]

    can_take = semesters[sem] & ~taken
    for i in range(N):
        if (can_take & (1 << i)) and (pre_require[i] & taken) != pre_require[i]:
            can_take &= ~(1 << i)

    ret = float('inf')
    take = can_take + 1
    while take:
        take = (take - 1) & can_take
        if bin(take).count("1") <= L:
            ret = min(ret, dynamic(sem + 1, taken | take) + 1)

    ret = min(ret, dynamic(sem+1, taken))
    cache[sem][taken] = ret
    return ret


for _ in range(int(input())):
    N, K, M, L = map(int, input().split())
    pre_require = []
    semesters = []
    for _ in range(N):
        requires = list(map(int, input().split()))
        cla = 0
        for r in requires[1:]:
            cla |= (1 << r)
        pre_require.append(cla)

    for _ in range(M):
        semester = list(map(int, input().split()))
        w = 0
        for s in semester[1:]:
            w |= (1 << s)
        semesters.append(w)

    cache = [[None] * (1 << N) for _ in range(M)]
    ans = dynamic(0, 0)
    if ans == float('inf'):
        print("IMPOSSIBLE")
    else:
        print(ans)
