from itertools import permutations
N = int(input())
numbers = list(input().split())
operator = list(map(int, input().split()))
max_num = -1000000001
min_num = 1000000001
operators = []
for op in range(4):
    for idx in range(operator[op]):
        if op == 0:
            operators.append('+')
        elif op == 1:
            operators.append('-')
        elif op == 2:
            operators.append('*')
        else:
            operators.append('/')
operators_combination = list(permutations(operators))
for operate in operators_combination:
    temp = 0
    for i in range(len(operate)):
        if numbers[i+1] == '0' and operate[i] == '/':
            pass
        else:
            if i == 0:
                temp = str(int(eval(numbers[i]+operate[i]+numbers[i+1])))
            else:
                temp = str(int(eval(temp+operate[i]+numbers[i+1])))
    temp = int(temp)
    if temp < min_num:
        min_num = temp
    if temp > max_num:
        max_num = temp

print(max_num)
print(min_num)