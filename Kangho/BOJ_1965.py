n = int(input())
box_list = list(map(int, input().split()))
numbers = [1]*(n+1)
for i in range(1, n):
    for j in range(i):
        if box_list[j] < box_list[i]:
            numbers[i] = max(numbers[j]+1, numbers[i])

print(max(numbers))