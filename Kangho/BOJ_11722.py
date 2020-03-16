n = int(input())
numbers = list(map(int, input().split()))
result = [1]*n

for i in range(1, n):
    for j in range(i):
        if numbers[i] < numbers[j]:
            result[i] = max(result[j]+1, result[i])

print(max(result))