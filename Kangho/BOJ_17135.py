import sys
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline
N, M, D = map(int, input().split())
board = []
monsters = []
for _ in range(N):
    board.append(list(map(int, input().split())))
for i in range(N):
    for j in range(M):
        if board[i][j] != 0:
            monsters.append([i, j])
archers = [i for i in range(M)]
combis = combinations(archers, 3)
answer = 0
ori_monsters = deepcopy(monsters)
for combi in combis:
    candi_answer = 0
    monsters = deepcopy(ori_monsters)
    while monsters:
        monster_idx = set()
        for archer in combi:
            a_row, a_col = N, archer
            min_monster, min_dis = -1, D+1
            for i, monster in enumerate(monsters):
                distance = abs(a_row-monster[0]) + abs(a_col-monster[1])
                if distance < min_dis:
                    min_dis = distance
                    min_monster = i
                elif distance == min_dis and min_dis <= D:
                    if monsters[min_monster][1] > monster[1]:
                        min_monster = i
            if min_monster != -1:
                monster_idx.add(min_monster)
        not_deleted_monsters = []
        for i, monster in enumerate(monsters):
            if i in monster_idx:
                candi_answer += 1
                continue
            else:
                not_deleted_monsters.append(monster)
        monsters = not_deleted_monsters
        not_arrived = []
        while monsters:
            monster = monsters.pop()
            if monster[0] + 1 == N:
                continue
            else:
                monster[0] += 1
                not_arrived.append(monster)
        monsters = not_arrived
    answer = max(answer, candi_answer)
print(answer)
