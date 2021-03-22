def solution(n, lost, reserve):
    answer = n - len(lost)
    reserve.sort()
    lost.sort()
    for k, size in enumerate(reserve):
        for i, ls in enumerate(lost):
            if size == ls:
                lost[i] = -1
                answer += 1
                reserve[k] = -1
                break

    for size in reserve:
        for i, ls in enumerate(lost):
            if abs(ls - size) == 1:
                answer += 1
                lost[i] = -1
                break
    return answer
