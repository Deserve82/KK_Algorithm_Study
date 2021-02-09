from collections import deque

directions = ((-1, 0), (0, -1), (1, 0), (0, 1))


def find_customer():
    if board[taxi[0]][taxi[1]] > 0:
        idx = board[taxi[0]][taxi[1]]
        board[taxi[0]][taxi[1]] = 0
        return idx
    q = deque()
    q.append([taxi[0], taxi[1], 0])
    checker = [[False] * N for _ in range(N)]
    checker[taxi[0]][taxi[1]] = True
    have_customer = []
    idx = -1
    while q:
        tr, tc, cost = q.popleft()
        for r, c in directions:
            mr, mc = tr + r, tc + c
            if 0 <= mr < N and 0 <= mc < N:
                if board[mr][mc] > 0 and not checker[mr][mc]:
                    if not have_customer:
                        have_customer = [mr, mc, cost+1]
                    else:
                        if have_customer[0] > mr and cost+1 <= have_customer[2]:
                            have_customer = [mr, mc, cost+1]
                        elif have_customer[0] == mr and have_customer[1] > mc and cost+1 <= have_customer[2]:
                            have_customer = [mr, mc, cost+1]
                    checker[mr][mc] = True
                    q.append([mr, mc, cost + 1])
                elif board[mr][mc] == 0 and not checker[mr][mc]:
                    q.append([mr, mc, cost + 1])
                    checker[mr][mc] = True
    if have_customer:
        idx = board[have_customer[0]][have_customer[1]]
        board[have_customer[0]][have_customer[1]] = 0
        taxi[0], taxi[1] = have_customer[0], have_customer[1]
        taxi[2] -= have_customer[2]
        return idx
    return idx


def get_customer_to_goal(person_idx):
    pr, pc = people[person_idx-1]
    gr, gc = goal[person_idx-1]
    q = deque()
    q.append((pr, pc, 0))
    checker = [[False] * N for _ in range(N)]
    while q:
        tr, tc, cost = q.popleft()
        if tr == gr and tc == gc:
            return cost
        for r, c in directions:
            mr, mc = tr + r, tc + c
            if 0 <= mr < N and 0 <= mc < N:
                if board[mr][mc] != -1 and not checker[mr][mc]:
                    checker[mr][mc] = True
                    q.append((mr, mc, cost + 1))
    return -1


N, M, F = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
TR, TC = map(int, input().split())
taxi = [TR-1, TC-1, F]
people = []
goal = []
for _ in range(M):
    pr, pc, gr, gc = map(int, input().split())
    people.append([pr-1, pc-1])
    goal.append([gr-1, gc-1])
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            board[i][j] = -1
for i, person in enumerate(people):
    pr, pc = person
    board[pr][pc] = i + 1
f = False
for _ in range(M):
    most_close = find_customer()
    if most_close == -1 or taxi[2] < 0:
        f = True
        break
    cost_to_goal = get_customer_to_goal(most_close)
    if taxi[2] - cost_to_goal < 0 or cost_to_goal == -1:
        f = True
        break
    else:
        taxi[2] += cost_to_goal
        taxi[0], taxi[1] = goal[most_close-1][0], goal[most_close-1][1]
if f:
    print(-1)
else:
    print(taxi[2])
