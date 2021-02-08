import sys
from collections import defaultdict

d = defaultdict(int)
total = 0
while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break

    d[tree] += 1
    total += 1
answer = []
for tree, num in d.items():
    answer.append((tree, num/total))
answer.sort()
for ans in answer:
    print(" ".join([ans[0], str(format(round(ans[1] * 100, 4), ".4f"))]))
