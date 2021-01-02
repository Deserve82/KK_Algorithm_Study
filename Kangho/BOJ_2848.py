from collections import defaultdict


def dfs(node):
    checker[node] = "op"
    if node in graph:
        for nn in graph[node]:
            if checker[nn] == "op":
                print("!")
                exit(0)
            elif checker[nn] == "nc":
                dfs(nn)
    checker[node] = "cd"


n = int(input())
words = []
for _ in range(n):
    words.append(input())
alph = set()
for w in words:
    alph.update(set(list(w)))
indegree = defaultdict(int)
checker = {}
graph = {}
prev = ""
for word in words:
    for prev_c, word_c in zip(prev, word):
        if prev_c != word_c:
            if prev_c not in graph.keys():
                graph[prev_c] = [word_c]
            else:
                graph[prev_c].append(word_c)
            indegree[word_c] += 1
            checker[prev_c] = "nc"
            checker[word_c] = "nc"
            break
        else:
            if len(prev) > len(word) and word in prev:
                print("!")
                exit(0)
    prev = word
for cc in checker.keys():
    if checker[cc] == "nc":
        dfs(cc)

Q = []
for c in alph:
    if c not in indegree:
        Q.append(c)
ans = []
while Q:
    if len(Q) > 1:
        print("?")
        exit(0)
    sc = Q.pop()
    ans.append(sc)
    if sc in graph:
        for n in graph[sc]:
            indegree[n] -= 1
            if indegree[n] == 0:
                Q.append(n)
print("".join(ans))
