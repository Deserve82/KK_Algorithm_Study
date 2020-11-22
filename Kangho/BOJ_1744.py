n = int(input())
p_numbers = []
n_numbers = []
z = 0
sum_of_value = 0
for _ in range(n):
    number = int(input())
    if number > 0:
        p_numbers.append(number)
    elif number < 0:
        n_numbers.append(number)
    else:
        z += 1

p_numbers.sort(reverse=True)
if len(p_numbers) % 2 == 0:
    while p_numbers:
        a = p_numbers.pop()
        b = p_numbers.pop()
        if a == 1 or b == 1:
            sum_of_value += (a + b)
        else:
            sum_of_value += a * b
else:
    sum_of_value += p_numbers.pop()
    while p_numbers:
        a = p_numbers.pop()
        b = p_numbers.pop()
        if a == 1 or b == 1:
            sum_of_value += (a + b)
        else:
            sum_of_value += a * b

n_numbers.sort()
if len(n_numbers) % 2 == 0:
    while n_numbers:
        a = n_numbers.pop()
        b = n_numbers.pop()
        sum_of_value += a * b
else:
    if z > 0:
        n_numbers.pop()
    else:
        sum_of_value += n_numbers.pop()
    while n_numbers:
        a = n_numbers.pop()
        b = n_numbers.pop()
        sum_of_value += a * b

print(sum_of_value)
