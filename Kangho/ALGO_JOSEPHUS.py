def josepus():
    m = n
    idx = 0
    while m != 2:
        army.pop(idx)
        idx += k - 1
        m -= 1
        idx %= m


if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().split())
        army = [str(a) for a in range(1, n+1)]
        josepus()
        print(" ".join(army))
        
        
# queue를 이용한 풀이
from collections import deque


def josepus():
    q = deque(army)
    m = n
    while m != 2:
        q.popleft()
        m -= 1
        for _ in range(k - 1):
            q.append(q.popleft())
    return q


if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().split())
        army = [str(a) for a in range(1, n + 1)]
        print(" ".join(josepus()))
