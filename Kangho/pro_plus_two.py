def solution(numbers):
    answer = set()
    ln = len(numbers)
    for i in range(ln):
        for j in range(ln):
            if i != j:
                answer.add(numbers[i] + numbers[j])
    answer = list(answer)
    answer.sort()
    return answer
