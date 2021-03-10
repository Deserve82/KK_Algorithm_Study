import sys
N = int(input())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

one_val = {}
for i in range(N):
    for j in range(N):
        val = A[i] + B[j]
        if one_val.get(val):
            one_val[val] += 1
        else:
            one_val[val] = 1
answer = 0

for i in range(N):
    for j in range(N):
        val = C[i] + D[j]
        if one_val.get(-val):
            answer += one_val[-val]

print(answer)
