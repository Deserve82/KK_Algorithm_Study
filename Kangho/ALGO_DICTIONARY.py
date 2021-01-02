# dfs 사용하는 방법
from collections import defaultdict


def dfs(n):
    global flag
    visited[n] = "on_process"
    for m in graph[n]:
        if visited[m] == "on_process":
            flag = False
        elif visited[m] == "not_checked":
            dfs(m)
    visited[n] = "checked"
    sq.append(n)


for _ in range(int(input())):
    N = int(input())
    words = []
    for _ in range(N):
        words.append(input())
    graph = defaultdict(set)
    visited = {}

    prev = ""
    for word in words:
        for i in range(min(len(prev), len(word))):
            if prev[i] != word[i]:
                graph[prev[i]].add(word[i])
                visited[prev[i]] = "not_checked"
                visited[word[i]] = "not_checked"
                break
        prev = word

    answer = []
    for node in visited.keys():
        if visited[node] == "not_checked":
            sq = []
            flag = True
            dfs(node)
            if flag:
                answer.extend(sq)
            else:
                break

    if flag:
        alph = [a if a not in answer else "" for a in "abcdefghijklmnopqrstuvwxyz"]
        answer.reverse()
        answer = "".join(answer + alph)
        print(answer)
    else:
        print("INVALID HYPOTHESIS")

        
# 밑에는 접한 노드 개수로 알아보는 방법
from collections import defaultdict, deque
for _ in range(int(input())):
    n = int(input())
    words = []
    alpha = set()
    for _ in range(n):
        ss = input()
        words.append(ss)
        alpha.union(set(list(ss)))

    graph = defaultdict(list)
    indegree = defaultdict(int)
    prev = ""
    for word in words:
        for prev_c, word_c in zip(prev, word):
            if prev_c != word_c:
                graph[prev_c].append(word_c)
                indegree[word_c] += 1
                break
        prev = word

    Q = deque()
    ans = []
    for c in graph.keys():
        if c not in indegree:
            Q.append(c)
    f = True
    for _ in range(len(graph)+1):
        if len(Q) == 0:
            f = False
            break
        else:
            c = Q.popleft()
            ans.append(c)
            for node in graph[c]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    Q.append(node)
    if f:
        alpha = [a for a in "abcdefghijklmnopqrstuvwxyz" if a not in ans]
        print("".join(ans) + "".join(alpha))
    else:
        print("INVALID HYPOTHESIS")
