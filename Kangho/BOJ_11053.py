n = int(input())
numbers = list(map(int, input().split()))
result = [1] * n
for i in range(1, n):
    for j in range(i):
        if numbers[j] < numbers[i]:
            result[i] = max(result[i], result[j]+1)
    print(result)
