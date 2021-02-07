def solution(number, k):
    S = []
    for num in number:
        while S and S[-1] < num and k != 0:
            S.pop()
            k -= 1
            if k == 0:
                break
        S.append(num)
    while k != 0:
        S.pop()
        k -= 1
    answer = "".join(S)
    return answer
