from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    clothes = defaultdict(list)
    for _ in range(n):
        a, c = input().split()
        clothes[c].append(a)
    total_val = 1
    for _, cloth in clothes.items():
        bb = len(cloth)
        total_val *= (bb+1)
    total_val -= 1
    print(total_val)
