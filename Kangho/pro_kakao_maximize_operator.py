from itertools import permutations

def solution(expression):
    answer = 0
    opss = ['*', '+', '-']
    prior = list(permutations(opss))
    numbers = []
    operators = []
    num = ''
    for char in expression:
        if char in opss:
            operators.append(char)
            numbers.append(num)
            num = ''
        else:
            num += char
    numbers.append(num)

    for pr in prior:
        number = numbers
        ope = operators
        for i in range(3):
            stack = [number[0]]
            stack_op = []
            cnt = 1
            while cnt < len(number):
                stack.append(number[cnt])
                stack_op.append(ope[cnt-1])
                if stack_op[-1] == pr[i]:
                    b = stack.pop()
                    a = stack.pop()
                    op = stack_op.pop()
                    stack.append(str(eval(a+op+b)))
                cnt += 1
            number = stack
            ope = stack_op
        answer = max(answer, abs(int(number[0])))
    return answer

print(solution("100-200*300-500+20"))
