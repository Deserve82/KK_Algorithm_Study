from copy import deepcopy


def make_combinations(idx, ml):
    combis.append(deepcopy(candidate))
    if idx >= ml:
        return
    for i in range(idx, ml):
        candidate.append(i)
        make_combinations(i + 2, ml)
        candidate.pop()


N = int(input())
exp = input()
operators = ['*', '+', '-']
combis = []
candidate = []
ops = []
numbers = []
num = ''
for char in exp:
    if char in operators:
        numbers.append(num)
        ops.append(char)
        num = ''
    else:
        num += char
numbers.append(num)
answer = -9999999999
make_combinations(0, len(ops))
for commands in combis:
    nums = [numbers[0]]
    s_op = []
    for i, op in enumerate(ops):
        if i in commands:
            a = nums.pop()
            b = numbers[i + 1]
            nums.append(str(eval(a + op + b)))
        else:
            s_op.append(op)
            nums.append(numbers[i + 1])
    last_nums = [nums[0]]
    for i, op in enumerate(s_op):
        a = last_nums.pop()
        b = nums[i + 1]
        last_nums.append(str(eval(a + op + b)))
    answer = max(answer, int(last_nums[0]))
print(answer)
