for _ in range(int(input())):
    m = int(input())
    numbers = []
    cache = [[0]*i for i in range(1, m+1)]

    for _ in range(m):
        numbers.append(list(map(int, input().split())))

    cache[0][0] = numbers[0][0]
    cache[1][0] = numbers[0][0] + numbers[1][0]
    cache[1][1] = numbers[1][1] + numbers[0][0]
    for i in range(1, m):
        for j in range(i+1):
            if j == i:
                cache[i][j] = max(cache[i-1][j-1] + numbers[i][j], cache[i][j])
            elif j == 0:
                cache[i][j] = max(cache[i-1][j] + numbers[i][j], cache[i][j])
            else:
                cache[i][j] = max(cache[i-1][j] + numbers[i][j], cache[i-1][j-1] + numbers[i][j], cache[i][j])
    print(max(cache[m-1]))
