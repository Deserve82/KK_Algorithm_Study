n = int(input())
numbers = list(map(int, input().split()))
max_val = 0
answer = 0
dp_s = [0] * n
dp_b = [0] * n
dp_final = [0] * n
for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j] and dp_s[i] < dp_s[j]:
            dp_s[i] = dp_s[j]
    dp_s[i] += 1
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if numbers[i] > numbers[j] and dp_b[i] < dp_b[j]:
            dp_b[i] = dp_b[j]
    dp_b[i] += 1
for i in range(n):
    dp_final[i] = dp_s[i] + dp_b[i] - 1

print(max(dp_final))
