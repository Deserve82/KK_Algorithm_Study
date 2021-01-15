N = int(input())
liquid = list(map(int, input().split()))
to_zero = 2100000000
liquid.sort()
i = 0
j = len(liquid) - 1
ans = [i, j]
while i < j:
    value = abs(liquid[i] + liquid[j])
    if to_zero > value:
        ans[0] = liquid[i]
        ans[1] = liquid[j]
        to_zero = value
    if value == 0:
        break
    elif liquid[i] + liquid[j] > 0:
        j -= 1
    else:
        i += 1
print(" ".join(map(str, ans)))
