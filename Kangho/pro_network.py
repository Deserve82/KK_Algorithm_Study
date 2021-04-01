def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    for i, computer in enumerate(computers):
        for j, node in enumerate(computer):
            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
    check = [False] * n
    for i in range(n):
        if not check[i]:
            answer += 1

            stack = [i]
            check[i] = True
            while stack:
                curr = stack.pop()
                for nxt in graph[curr]:
                    if not check[nxt]:
                        stack.append(nxt)
                        check[nxt] = True
    return answer
