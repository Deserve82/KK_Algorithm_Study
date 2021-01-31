import sys

INF = float('inf')


def min_semestered_required(K, L, prerequisites, opened_lectures):
    N, S = len(prerequisites), len(opened_lectures)
    cache = [[None] * (1 << N) for _ in range(S)]

    def graduate(semester, taken):
        if bin(taken).count("1") >= K:
            return 0
        elif semester == S:
            return INF

        if cache[semester][taken] is not None:
            return cache[semester][taken]

        ret = INF
        # 아번 학기 중에 이미 들었던 것을 제외한 목록
        can_take = opened_lectures[semester] & ~taken

        # 선수과목 안들은 것들을 빼준다
        for i in range(N):
            if (can_take & (1 << i)) and (taken & prerequisites[i]) != prerequisites[i]:
                can_take &= ~(1 << i)

        # 집합의 모든 부분집합 순회
        take = can_take + 1

        while take:
            take = (take - 1) & can_take
            if bin(take).count("1") <= L:
                ret = min(ret, graduate(semester + 1, taken | take) + 1)

        # 아무것도 안 들을 경우
        ret = min(ret, graduate(semester + 1, taken))
        cache[semester][taken] = ret
        return ret

    aa = graduate(0, 0)
    return aa if aa != INF else "IMPOSSIBLE"


ans = []
for _ in range(int(sys.stdin.readline())):
    N, K, S, L = map(int, sys.stdin.readline().split())
    prerequisites = []
    opened_lectures = []

    for _ in range(N):
        pre_class = list(map(int, sys.stdin.readline().split()))
        pres_bit = 0
        for p in pre_class[1:]:
            pres_bit |= (1 << p)
        prerequisites.append(pres_bit)

    for _ in range(S):
        lectures = list(map(int, sys.stdin.readline().split()))
        check_sem = 0
        for s in lectures[1:]:
            check_sem |= (1 << s)
        opened_lectures.append(check_sem)

    ans.append(min_semestered_required(K, L, prerequisites, opened_lectures))
for ret in ans:
    print(ret)
