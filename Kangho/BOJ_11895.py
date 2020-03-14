n = int(input())
numbers = list(map(int, input().split()))
x = 0
answer = 0
for number in numbers:
    x ^= number
    answer += number
numbers.sort()
if x == 0:
    print(answer - numbers[0])
else:
    print(0)