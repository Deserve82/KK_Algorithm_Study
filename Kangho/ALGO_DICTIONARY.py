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
