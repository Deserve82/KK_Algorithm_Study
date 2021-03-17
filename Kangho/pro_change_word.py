from collections import deque

def how_many_have(a, b):
    ls = len(a)
    val = 0
    for i in range(ls):
        if a[i] == b[i]:
            val += 1
    return val

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append((begin, 0))
    checker = {begin: 1}
    pivot_length = len(words[0])
    while q:
        curr, cost = q.popleft()
        if curr == target:
            answer = cost
            break
        for word in words:
            if how_many_have(curr, word) == pivot_length - 1 and word not in checker:
                checker[word] = 1
                q.append((word, cost + 1))
    return answer
