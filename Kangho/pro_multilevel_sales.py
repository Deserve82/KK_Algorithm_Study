parent = {}
points = {}


def get_money(person, amount):
    tithe = amount // 10
    points[person] += (amount - tithe)
    if parent[person] != '-':
        get_money(parent[person], tithe)


def solution(enroll, referral, seller, amount):
    answer = []
    for c, p in zip(enroll, referral):
        parent[c] = p
        points[c] = 0

    for sell, a in zip(seller, amount):
        get_money(sell, a * 100)

    for p in enroll:
        answer.append(points[p])
    return answer
