s = input()
m_flag = False
number = ""
sums = 0
for i in s:
    if i == '-' or i == '+':
        if m_flag:
            sums -= int(number)
            number = ""
        else:
            sums += int(number)
            number = ""
            if i == "-":
                m_flag = True
    else:
        number += i
if m_flag:
    sums -= int(number)
else:
    sums += int(number)

print(sums)
