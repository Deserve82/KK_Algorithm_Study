s = "abcabcabcabcdededededede"
answer = len(s)
l = len(s)
for i in range(1, l):
    length = len(s)
    pivot = s[0:i]
    change_flag = False
    time_stack = 0
    for j in range(1, int(length/i)):
        if pivot == s[j*i:j*i+i]:
            length -= len(pivot)
            if not change_flag:
                length += 1
                change_flag = True
            else:
                time_stack += 1
        else:
            pivot = s[j*i:j*i+i]
            change_flag = False
            if 9 < time_stack < 100:
                length += 1
            if 99 < time_stack < 1000:
                length += 2
            if 999 < time_stack < 10000:
                length += 3
            time_stack = 1
    if 9 < time_stack < 100:
        length += 1
    if 99 < time_stack < 1000:
        length += 2
    if 999 < time_stack < 10000:
        length += 3
    if length < answer:
        answer = length

print(answer)