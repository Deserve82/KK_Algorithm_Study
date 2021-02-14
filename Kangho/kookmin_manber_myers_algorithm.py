# 맨버 마이어스 알고리즘.. make suffix array time complexity O(nlogn^2)
import sys
s = sys.stdin.readline().strip()

n = len(s)
sa = [i for i in range(n)]
g = [0] * (n + 1)  # 순위
ng = [0] * (n + 1)  # 새로운 순위(순위를 갱신할 때 이용할 배열)

for i in range(n):
    g[i] = ord(s[i])

g[n] = -1
ng[sa[0]] = 0
ng[n] = -1
t = 1

while t < n:
    sa.sort(key=lambda x: (g[x], g[min(x + t, n)]))

    for i in range(1, n):
        p, q = sa[i - 1], sa[i]
        if g[p] != g[q] or g[min(p + t, n)] != g[min(q + t, n)]:
            ng[q] = ng[p] + 1
        else:
            ng[q] = ng[p]

    if ng[n - 1] == n - 1:
        break

    t = t * 2
    g = ng[:]
print(sa)
