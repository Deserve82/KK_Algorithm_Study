n = int(input())
numbers = list(map(int, input().split()))
result = [0]*n
result[0] = numbers[0]
for i in range(1, n):
    for j in range(i+1):
        if numbers[i] > numbers[j]:
            result[i] = max(numbers[i]+result[j], result[i])
        else:
            result[i] = max(result[i], numbers[i])
print(max(result))
