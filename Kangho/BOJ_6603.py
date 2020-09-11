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
    
