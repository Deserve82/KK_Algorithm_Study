from itertools import combinations


def check(relation, combi):
    if not combi:
        return False
    t = []
    for i in range(len(relation)):
        total = set()
        for can in combi:
            total.add(relation[i][can]+str(can))
        if total not in t:
            t.append(total)
    if len(t) == len(relation):
        return True
    else:
        return False


def solution(relation):
    answer = 0
    relation_col = len(relation[0])
    relation_row = len(relation)
    is_candidate = []
    for j in range(relation_col):
        t = set()
        for i in range(relation_row):
            t.add(relation[i][j])
        if len(t) != relation_row:
            is_candidate.append(j)
        else:
            answer += 1
    can_be_candi = []
    for i in range(2, len(is_candidate) + 1):
        can_be_candi.extend(list(combinations(is_candidate, i)))

    for con in can_be_candi:
        if check(relation, con):
            answer += 1
            for i in range(len(can_be_candi)):
                if set(con) & set(can_be_candi[i]) == set(con):
                    can_be_candi[i] = set()
    return answer
