from collections import Counter


def solution(a):
    ele = Counter(a)
    answer = -1

    for k in ele.keys():
        if ele[k] <= answer:
            continue
        common_cnt = 0
        idx = 0
        while idx < len(a) - 1:
            if (a[idx] != k and a[idx + 1] != k) or a[idx] == a[idx + 1]:
                idx += 1
                continue
            common_cnt += 1
            idx += 2
        answer = max(common_cnt, answer)
    if answer == -1:
        return 0
    else:
        return answer * 2
