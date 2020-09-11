from itertools import combinations
while True:
    numbers = list(input().split())
    if len(numbers) == 1:
        break
    num = numbers[0]
    numbers.pop(0)
    combis = list(combinations(numbers, 6))
    for c in combis:
        print(" ".join(c))
    print("")
    
# 내가 구현한 combination code
# def combinations(start):
#     global answer, cnt
#     if cnt == 6:
#         print(" ".join(answer))
#         return
#     for i, number in enumerate(numbers):
#         if not checker[i] and start <= int(number):
#             answer.append(number)
#             checker[i] = True
#             cnt += 1
#             combinations(int(number))
#             answer.pop()
#             checker[i] = False
#             cnt -= 1
#     return


# while True:
#     answer = []
#     cnt = 0
#     numbers = list(input().split())
#     if len(numbers) == 1:
#         break
#     num = int(numbers[0])
#     checker = [False]*num
#     numbers.pop(0)
#     combinations(int(numbers[0]))
#     print("")
