import sys


def dfs(node):
    global mv
    hw = [0]
    check[node] = True
    for nn, nw in tree[node]:
        if not check[nn]:
            tt = dfs(nn)
            hw.append(tt + nw)
    if len(hw) >= 2:
        hw.sort()
        aa = hw[-1] + hw[-2]
        mv = max(aa, mv)
    return hw[-1]


mv = 0
G = int(input())
tree = [[] for _ in range(G)]
check = [False] * G
for _ in range(G):
    t = list(map(int, sys.stdin.readline().split()))
    lt = len(t)
    for i in range(1, lt - 1, 2):
        tree[t[0] - 1].append((t[i] - 1, t[i + 1]))
dfs(0)
print(mv)
