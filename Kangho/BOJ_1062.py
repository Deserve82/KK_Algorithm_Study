import sys


def checker(val):
    cnt = 0
    for word in words:
        if word & val == word:
            cnt += 1
    return cnt


def bf(idx, k):
    global bit, answer
    if k == K:
        answer = max(answer, checker(bit))
        return

    for i in range(idx, 21):
        if not bit & (1 << i):
            bit |= (1 << i)
            bf(i+1, k+1)
            bit &= ~(1 << i)
    return


N, K = map(int, sys.stdin.readline().split())
words = []
alpha_checker = [False] * len('bdefghjklmopqrsuvwxyz')
alpha_num = {}
for i, a in enumerate('bdefghjklmopqrsuvwxyz'):
    alpha_num[a] = i
for _ in range(N):
    tmp = sys.stdin.readline().rstrip()[4:-4]
    w = 0
    for t in tmp:
        if t not in 'antic':
            w |= (1 << alpha_num[t])
    words.append(w)
bit = 0
answer = 0
if K < 5:
    print(0)
else:
    K -= 5
    bf(0, 0)
    print(answer)
