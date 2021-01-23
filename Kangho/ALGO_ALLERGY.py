import sys


def brute_force(chosen):
    global answer
    if chosen >= answer:
        return
    first = ''
    for name, cnt in checker.items():
        if cnt == 0:
            first = name
            break
    if first == '':
        answer = min(answer, chosen)
        return
    for candidate in pp[first]:
        for f_name in candidate[1:]:
            checker[f_name] += 1
        brute_force(chosen + 1)
        for f_name in candidate[1:]:
            checker[f_name] -= 1


for _ in range(int(input())):
    answer = 100
    N, M = map(int, sys.stdin.readline().split())
    people = list(sys.stdin.readline().split())
    checker = {}
    pp = {}
    for person in people:
        checker[person] = 0
        pp[person] = []
    foods = []
    mv = 0
    for i in range(M):
        food = list(sys.stdin.readline().split())
        foods.append(food)
        for f in food[1:]:
            pp[f].append(food)
    brute_force(0)
    print(answer)
