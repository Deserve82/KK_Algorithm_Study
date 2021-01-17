N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
answer = 0
for pivot in range(N):
    left = 0
    right = N - 1
    while left < right:
        if left == pivot:
            left += 1
        if right == pivot:
            right -= 1
        if numbers[left] + numbers[right] == numbers[pivot]:
            answer += 1
            break
        elif numbers[left] + numbers[right] > numbers[pivot]:
            right -= 1
            if right == pivot:
                right -= 1
        elif numbers[left] + numbers[right] < numbers[pivot]:
            left += 1
            if left == pivot:
                left += 1
print(answer)
