import math
from itertools import combinations
n = int(input())

for _ in range(n):
    ls = list(map(int, input().split()))
    ls.pop(0)
    z = list(combinations(ls, 2))
    su = 0
    for c in z:
        su += math.gcd(c[0], c[1])
    print(su)
