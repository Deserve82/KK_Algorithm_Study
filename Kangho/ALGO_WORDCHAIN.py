import sys
from collections import defaultdict


def dfs(start, word):
    while graph[start]:
        next_char, next_word = graph[start].pop()
        dfs(next_char, next_word)
    ans.append(word)


for _ in range(int(input())):
    N = int(input())
    words = []
    for _ in range(N):
        words.append(sys.stdin.readline().rstrip())
    graph = defaultdict(list)
    in_edge = defaultdict(int)
    out_edge = defaultdict(int)

    for word in words:
        graph[word[0]].append((word[-1], word))
        # 꼭 간선을 이렇게 봐야 하는 군.. 어차피 다른 것들이랑 연결이 되는 건 알파벳 노드별로 되니까
        out_edge[word[0]] += 1
        in_edge[word[-1]] += 1

    candies = set()
    for word in words:
        if in_edge[word[0]] != out_edge[word[0]]:
            candies.add(word[0])
        if in_edge[word[-1]] != out_edge[word[-1]]:
            candies.add(word[-1])

    ans = []
    if len(candies) == 2:
        start, end = None, None
        for word in words:
            if in_edge[word[0]] + 1 == out_edge[word[0]]:
                start = word[0]
            if in_edge[word[-1]] + 1 == out_edge[word[-1]]:
                start = word[-1]

            if in_edge[word[0]] == out_edge[word[0]] + 1:
                end = word[0]
            if in_edge[word[-1]] == out_edge[word[-1]] + 1:
                end = word[-1]
        if start and end:
            dfs(start, "")

    elif len(candies) == 0:
        dfs(words[0][0], "")

    if ans:
        ans.reverse()
        print(" ".join(ans).lstrip())
    else:
        print("IMPOSSIBLE")
