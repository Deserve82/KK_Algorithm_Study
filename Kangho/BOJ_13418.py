import sys


def check(a):
    rv = 0
    for command in commands:
        s, e, h = command
        if get_parent(s) != get_parent(e):
            union_parent(s, e)
            rv += abs(h - 1)
    if a == 0:
        rv += 1
    return rv * rv


def get_parent(index):
    if parent[index] == index:
        return index
    else:
        parent[index] = get_parent(parent[index])
        return parent[index]


def union_parent(a, b):
    ap = get_parent(a)
    bp = get_parent(b)
    if ap < bp:
        parent[bp] = ap
    else:
        parent[ap] = bp


n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]
commands = []
add = 1
for j in range(m + 1):
    if j == 0:
        add = list(map(int, sys.stdin.readline().split()))[2]
    else:
        commands.append(tuple(map(int, sys.stdin.readline().split())))
commands.sort(key=lambda x: x[2])
cnt = check(add)
commands.sort(key=lambda x: x[2], reverse=True)
parent = [i for i in range(n + 1)]
se_cnt = check(add)
print(cnt - se_cnt)
