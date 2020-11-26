def dfs(signs, start):
    s = [start]
    m = len(signs)
    check = [False] * m
    answer = [0] * m
    while s:
        start_node = s.pop()
        for i in range(m):
            if signs[start_node][i] == 1 and not check[i]:
                s.append(i)
                check[i] = True
                answer[i] = 1
    return answer


def solution(n, signs):
    answer = []
    for i in range(n):
        answer.append(dfs(signs, i))
    return answer
