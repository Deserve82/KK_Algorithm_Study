def min_checker(number):
    mv = 10
    n = 0
    for b in buttons:
        if abs(b-number) < mv:
            mv = abs(b-number)
            n = b
    return n


want_c = int(input())
n = int(input())
del_buttons = list(map(int, input().split()))
buttons = [i for i in range(10)]
c = 100
for d in del_buttons:
    buttons.remove(d)

answer = 0
if c != want_c:
    pivot = ''
    for wc in str(want_c):
        pivot += str(min_checker(int(wc)))
        answer += 1
    if pivot != str(want_c):
        answer += abs(int(pivot)-want_c)
print(answer)
