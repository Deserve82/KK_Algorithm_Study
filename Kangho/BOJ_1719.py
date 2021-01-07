G, V = map(int, input().split())
coupang = [[float('inf')]*G for _ in range(G)]
before = [["-"]*G for _ in range(G)]
for i in range(G):
    coupang[i][i] = 0
for _ in range(V):
    s, e, w = map(int, input().split())
    if w < coupang[s-1][e-1]:
        coupang[s-1][e-1] = w
        before[s-1][e-1] = str(e)
    if w < coupang[e-1][s-1]:
        coupang[e-1][s-1] = w
        before[e-1][s-1] = str(s)
for k in range(G):
    for i in range(G):
        for j in range(G):
            tmp = coupang[i][k] + coupang[k][j]
            if coupang[i][j] > tmp:
                coupang[i][j] = tmp
                before[i][j] = before[i][k]
for c in before:
    print(" ".join(c))
