from collections import deque


def cal(string):
    global K
    answer = deque()
    string = string[::-1]
    answer.append(str(K))
    for char in string:
        if char == '*':
            K //= 2
        elif char == '+':
            K -= 1
        else:
            K += 1
        answer.appendleft(str(K))
    print(" ".join(answer))


N, K = map(int, input().split())
q = deque()
q.append((N, ''))
checker = [False] * 100001
while q:
    cur, his = q.popleft()
    if cur == K:
        print(len(his))
        cal(his)
        break
    if 2 * cur <= 100000:
        if not checker[2 * cur]:
            checker[cur * 2] = True
            q.append((2 * cur, his + "*"))
    if cur + 1 <= 100000:
        if not checker[cur + 1]:
            checker[cur + 1] = True
            q.append((cur + 1, his + "+"))
    if cur - 1 >= 0:
        if not checker[cur - 1]:
            checker[cur - 1] = True
            q.append((cur - 1, his + "-"))
