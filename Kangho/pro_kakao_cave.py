def solution(n, path, order):
    answer = True
    graph = [[] for _ in range(n)]
    for p in path:
        graph[p[0]].append(p[1])
        graph[p[1]].append(p[0])
    key = {}
    is_opend = [True] * n
    checked = [False] * n
    for k, v in order:
        key[k] = v
        is_opend[v] = False

    is_check = True
    while is_check:
        is_check = False
        stack = []
        for i, candi in enumerate(checked):
            if not candi and is_opend[i]:
                stack.append(i)
                is_check = True
                checked[i] = True
                if i in key:
                    is_opend[key[i]] = True
                break
        while stack:
            curr = stack.pop()
            for nxt in graph[curr]:
                if not checked[nxt] and is_opend[nxt]:
                    stack.append(nxt)
                    checked[nxt] = True
                    if nxt in key:
                        is_opend[key[nxt]] = True
    for a in checked:
        if not a:
            answer = False
            break
    return answer
