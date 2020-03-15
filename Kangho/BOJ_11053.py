# 내가 만든 허접한 풀이
n = int(input())
numbers = list(map(int, input().split()))
num = [[0, 0]]
answer = 0
for number in numbers:
    for i in num:
        if number > i[0]:
            if num[-1][1] >= i[1]+1 and num[-1][0] <= number:
                pass
            else:
                num.append([number, i[1] + 1])
            if i[1]+1 > answer:
                answer = i[1]+1
print(answer)


# 정확한 풀이
n = int(input())
numbers = list(map(int, input().split()))
result = [1] * n
for i in range(1, n):
    for j in range(i):
        if numbers[j] < numbers[i]:
            result[i] = max(result[i], result[j]+1)
print(max(result))
