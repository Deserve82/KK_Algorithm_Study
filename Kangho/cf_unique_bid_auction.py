n = int(input())
answer = []
for _ in range(n):
    participants = int(input())
    numbers = [0 for _ in range(participants)]
    choose_numbers = list(map(int, input().split()))
    for number in choose_numbers:
        numbers[number-1] += 1
 
    min_counter = 20000001
    for number in numbers:
        if min_counter > number != 0:
            min_counter = number
    min_number = 0
    for i, number in enumerate(numbers):
        if min_counter == number:
            min_number = i + 1
            break
    has_answer = True
    real_answer = 0
    for i, number in enumerate(choose_numbers):
        if number == min_number and has_answer:
            has_answer = False
            real_answer = i + 1
        elif number == min_number and not has_answer:
            real_answer = -1
            break
    answer.append(real_answer)
for a in answer:
    print(a)
