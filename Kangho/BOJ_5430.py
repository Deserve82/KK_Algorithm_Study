import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    command = input().rstrip()
    n = int(input())
    numbers = input().rstrip()[1:-1].split(',')
    if '' in numbers:
        numbers.remove('')
    q = deque(numbers)
    err_flag = False
    ori_flag = True
    for c in command:
        if c == "R":
            ori_flag = not ori_flag
        else:
            if not q:
                err_flag = True
                break
            if ori_flag:
                q.popleft()
            else:
                q.pop()

    if err_flag:
        print("error")
    else:
        if not ori_flag:
            q.reverse()
        print("[" + ",".join(q) + "]")
