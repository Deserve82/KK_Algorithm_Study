import sys
t = int(sys.stdin.readline())


def dfs(start):
    f = [start]
    while f:
        x = f.pop()
        visited[x - 1] = True
        if colors[x-1] == 'n':
            colors[x - 1] = 'r'
        if colors[x-1] == 'r':
            c = 'b'
        else:
            c = 'r'
        for node in field[x]:
            if not visited[node-1]:
                if colors[node-1] != colors[x-1]:
                    colors[node-1] = c
                    f.append(node)
                else:
                    return False
    return True


for _ in range(t):
    ff = False
    v, e = map(int, sys.stdin.readline().split())
    colors = ['n']*v
    visited = [False]*v
    field = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        field[a].append(b)
        field[b].append(a)
    for i, f in enumerate(visited):
        if not f:
            ff = dfs(i+1)
            if not ff:
                break
    if ff:
        print("YES")
    else:
        print("NO")
