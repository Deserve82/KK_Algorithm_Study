def solution(n, s):
    answer = []
    pivot = s // n
    if pivot == 0:
        return [-1]
    for _ in range(n):
        answer.append(pivot)
    sv = s - pivot*n
    for i in range(sv):
        answer[i % n] += 1
    answer.sort()
    return answer
