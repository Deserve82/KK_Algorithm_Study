def solution(brown, yellow):
    answer = [0, 0]
    sums = brown+yellow
    for i in range(1, sums):
        if sums % i == 0:
            if (sums // i - 2) * (i - 2) == yellow:
                answer[0], answer[1] = sums//i, i
                break
    return answer
