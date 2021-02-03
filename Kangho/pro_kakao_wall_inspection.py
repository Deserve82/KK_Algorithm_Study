from itertools import permutations


def calculate(left_idx, weak_length, dist_length, fix_number, distance, weak):
    fixed_cnt = 0
    d_idx = 0
    right_idx = left_idx + 1
    while right_idx < weak_length and d_idx < dist_length and fixed_cnt < fix_number:
        while weak[left_idx] + distance[d_idx] >= weak[right_idx]:
            right_idx += 1
            fixed_cnt += 1
            if right_idx == dist_length:
                break
            if fixed_cnt == fix_number:
                break

        left_idx = right_idx
        right_idx = left_idx + 1
        d_idx += 1
        fixed_cnt += 1

    if fixed_cnt != fix_number:
        return 99999
    else:
        return d_idx


def solution(n, weak, dist):
    answer = 99999
    g = len(weak)
    extend_weak = [i + n for i in weak]
    weak.extend(extend_weak)
    permus = permutations(dist)
    N = len(weak)
    D = len(dist)

    for p in permus:
        for i in range(N//2-1):
            answer = min(answer, calculate(i, N, D, g, p, weak))
    if answer == 99999:
        return -1
    return answer
