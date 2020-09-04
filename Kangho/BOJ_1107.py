import math


def min_checker(number):
    if buttons:
        mv = 10
        n = 0
        for b in buttons:
            if abs(b-number) < mv:
                mv = abs(b-number)
                n = b
        return n


def make_max_and_move(want, l):
    val = [str(buttons[0])]*l
    w = want
    mv = 50000001
    for i in range(l, 0, -1):
        for b in buttons:
            if abs(w - b*math.pow(10, i-1)) < mv:
                mv = abs(w - b*math.pow(10, i-1))
                val[l-i] = str(b)
        if len(str(w)) > 1:
            w = int(str(w)[1:])
        else:
            return ''.join(val)
    return ''.join(val)


want_c = int(input())
l = len(str(want_c))
n = int(input())
del_buttons = list(map(int, input().split()))
buttons = [i for i in range(10)]
c = 100
for d in del_buttons:
    buttons.remove(d)

answer = 5000001
if buttons:
    pivot = ''
    a = 0
    for wc in str(want_c):
        pivot += str(min_checker(int(wc)))
        a += 1
    if pivot != str(want_c):
        a += abs(int(pivot)-want_c)
    if a < answer:
        answer = a
    t = int(make_max_and_move(want_c, l))
    if abs(want_c - t) + l < answer:
        answer = abs(want_c - t) + l
    if l > 1:
        t = int(make_max_and_move(want_c, l-1))
        if abs(want_c - t) + l-1 < answer:
            answer = abs(want_c - t) + l-1
    t = int(make_max_and_move(want_c, l+1))
    if abs(t - want_c) + l + 1 < answer:
        answer = abs(t - want_c) + l + 1
if abs(want_c-c) < answer:
    answer = abs(want_c-c)
print(answer)
