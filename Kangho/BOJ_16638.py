from copy import deepcopy


def make_combis(idx):
    if idx >= lo:
        return

    combis.append(deepcopy(tmp))
    for i in range(idx, lo):
        tmp.append(i)
        make_combis(i+2)
        tmp.pop()


N = int(input())
O = ['*', '+', '-']
expression = input()
operators = []
numbers = []
num = ''
for char in expression:
    if char in O:
        operators.append(char)
        numbers.append(num)
        num = ''
    else:
        num += char
numbers.append(num)
lo = len(operators) + 2
tmp = []
combis = []
make_combis(0)
answer = -9999999999
for combi in combis:
    if combi:
        num_stack = [numbers[0]]
        op_stack = []

        for i in range(len(operators)):
            if i in combi:
                a, b = num_stack.pop(), numbers[i + 1]
                num_stack.append(str(eval(a + operators[i] + b)))
            else:
                op_stack.append(operators[i])
                num_stack.append(numbers[i + 1])
    else:
        num_stack = deepcopy(numbers)
        op_stack = deepcopy(operators)

    new_ex = num_stack[0]
    for i in range(len(op_stack)):
        new_ex += (op_stack[i] + num_stack[i+1])
    answer = max(answer, eval(new_ex))
print(answer)
