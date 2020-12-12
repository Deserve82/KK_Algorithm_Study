from itertools import combinations
nl, goal = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0
left = numbers[:nl//2]
right = numbers[nl//2:]
left_sum = []
for i in range(1, nl//2+1):
    cs = list(combinations(left, i))
    for c in cs:
        sc = sum(c)
        if sc == goal:
            cnt += 1
        left_sum.append(sc)
right_sum = []
for i in range(1, nl//2+2):
    cs = list(combinations(right, i))
    for c in cs:
        sc = sum(c)
        if sc == goal:
            cnt += 1
        right_sum.append(sc)
left_sum.sort()
right_sum.sort(reverse=True)
i = 0
j = 0
lc = len(left_sum)
rc = len(right_sum)
while i < lc and j < rc:
    p = left_sum[i] + right_sum[j]
    if p > goal:
        j += 1
    elif p < goal:
        i += 1
    else:
        ls, rs = 1, 1
        left_idx = i + 1
        right_idx = j + 1
        while left_idx < lc and left_sum[left_idx] == left_sum[i]:
            ls += 1
            left_idx += 1
        while right_idx < rc and right_sum[right_idx] == right_sum[j]:
            rs += 1
            right_idx += 1
        i = left_idx
        j = right_idx
        cnt += ls*rs
print(cnt)
