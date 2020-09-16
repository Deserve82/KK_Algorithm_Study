import sys


def dfs(s):
    global count
    count += 1
    st = [s]
    while st:
        k = st.pop()
        for node in graph:
            if node[0] == k:
                if node[1] not in visited:
                    st.append(node[1])
                    visited.append(node[1])
            elif node[1] == k:
                if node[0] not in visited:
                    st.append(node[0])
                    visited.append(node[0])

count = 0
visited = []
nodes = set()
n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(m):
    a, b = map(int, input().split())
    nodes.add(a)
    nodes.add(b)
    graph.append((a, b))

for node in graph:
    if node[0] in visited:
        pass
    else:
        visited.append(node[0])
        dfs(node[0])

count += n - len(nodes)
print(count)
