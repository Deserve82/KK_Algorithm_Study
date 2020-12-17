n = int(input())
numbers = list(map(int, input().split()))
checker = [False] * n
max_vals = []
answers = []


def cal(permutated_numbers):
    t = 0
    for i in range(1, n):
        t += abs(permutated_numbers[i - 1] - permutated_numbers[i])
    return t


def permu(cnt):
    if cnt == n:
        answers.append(cal(max_vals))
        return
    for i in range(n):
        if not checker[i]:
            checker[i] = True
            max_vals.append(numbers[i])
            permu(cnt + 1)
            max_vals.pop()
            checker[i] = False


permu(0)
print(max(answers))
