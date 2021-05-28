from collections import deque
A, B = map(int, input().split())
q = deque()
q.append([A, 1])
answer = -1
while q:
    v, c = q.popleft()
    if int(v) > B:
        continue
    if int(v) == B:
        answer = c
        break
    if 2 * int(v) <= B:
        q.append([2*int(v), c+1])
    q.append([str(v)+'1', c+1])
print(answer)
