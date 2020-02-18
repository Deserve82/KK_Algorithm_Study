n = int(input())
numbers = list(map(int, input().split()))
max_v = numbers[0]
answer = [max(numbers)]
for number in numbers[1:]:
    if max_v < 0 < number:
        max_v = number
    elif max_v + number > max_v:
        max_v += number
        answer.append(max_v)
    elif max_v + number > 0:
        max_v += number
    else:
        max_v = 0

print(max(answer))
