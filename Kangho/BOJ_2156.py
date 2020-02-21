n = int(input())
wines = [0]
for _ in range(n):
    wines.append(int(input()))
result = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if i == 1:
        result[1] = wines[1]
    elif i == 2:
        result[2] = wines[2]+wines[1]
    else:
        result[i] = max(result[i-3] + wines[i-1] + wines[i], result[i-2] + wines[i], result[i-1])

print(result[n])
