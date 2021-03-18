from copy import deepcopy
import sys
sys.setrecursionlimit(10**6)

movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]
board = []
tags = []
parents = []
ll = 0
H = 0


def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    parents[b] = a


def dfs(sr, sc, curr_num):
    stack = [(sr, sc)]
    while stack:
        sr, sc = stack.pop()
        for move in movements:
            mr = sr + move[0]
            mc = sc + move[1]
            if 0 <= mr < ll and 0 <= mc < ll:
                if tags[mr][mc] == 0 and abs(board[sr][sc] - board[mr][mc]) <= H:
                    tags[mr][mc] = curr_num
                    stack.append((mr, mc))


def solution(land, height):
    global board, tags, ll, H, parents
    H = height
    answer = 0
    board = deepcopy(land)
    ll = len(land)
    tags = [[0] * ll for _ in range(ll)]
    idx = 1
    for i in range(ll):
        for j in range(ll):
            if tags[i][j] == 0:
                tags[i][j] = idx
                dfs(i, j, idx)
                idx += 1
    parents = [i for i in range(idx + 1)]
    length = set()
    for i in range(ll):
        for j in range(ll):
            cur = land[i][j]
            for d in movements:
                mr = i + d[0]
                mc = j + d[1]
                if 0 <= mr < ll and 0 <= mc < ll:
                    if tags[i][j] != tags[mr][mc]:
                        length.add((abs(cur - land[mr][mc]), tags[i][j], tags[mr][mc]))
    length = list(length)
    length.sort()
    for l in length:
        dis, f, t = l
        if find(f) != find(t):
            answer += dis
            union(f, t)
    return answer
